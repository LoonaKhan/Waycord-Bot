"""
All archive-related commands
"""
import discord
from utils.load_env import *
from bot_info import bot, c
from waycord_api.calls import *

# delete an archive
@bot.command(aliases=["del", "d"])
async def delete(ctx, id:int):
    """
    Deletes an archive by id.

    Makes an api call to the database to delete that archive

    todo:
        the user can only delete their own archives. verify that the user is not deleting someone else's archive.
    """

    if ctx.author.bot: return # does not answer to bots

    try:
        res = delArchive(key=KEY, id=id, creator=ctx.author.id)
        if res['affectedRows'] == 0:
            await ctx.send("**ERROR**: could not delete archive")
            return
        await ctx.send("deleted")
    except:
        await ctx.send("**ERROR**: could not delete archive")

# add an archive
@bot.command(aliases=["a"])
async def add(ctx, title:str):
    """
    Adds an archive

    Creates an message object and archive object in the database via API calls.

    The actual message object is always attempted to be created,
    but if it already exists in the database,
    it wont be duplicated, nor throw an error.

    We create the archive using the message data.
    """

    if ctx.author.bot: return # does not answer to bots

    try:
        try:
            msg = await ctx.fetch_message(ctx.message.reference.message_id)
        except:
            await ctx.send("You need to reply to a message to make an archive")
            return

        resAddMsg = addMsg(key=KEY,
                           id=str(msg.id),
                           author=str(msg.author.id),
                           contents=str(msg.content),
                           channel=str(msg.channel.id),
                           creation_date=str(msg.created_at))

        res = addArchive(key=KEY,
                         creator_id=str(ctx.author.id),
                         title=title,
                         message_id=str(msg.id), # requires message object to exist in the database
                         creation_date=str(ctx.message.created_at))

        if res['affectedRows'] == 0:
            await ctx.send("**ERROR**: could not create archive")
            return
        await ctx.send(f"Created archive, **{title}**, with ID: **{res['insertId']}**")

    except Exception as e:
        await ctx.send(f"**ERROR**: could not create archive: {e}")

# get all user archives
@bot.command(aliases=["l", "ls"])
async def list(ctx, filter="server"):
    """
    Lists all of a user's archives.

    Just runs the api request.

    todo:
        make embeds look better
        attachments
    """

    if ctx.author.bot: return  # does not answer to bots

    res = getUserArchives(key=KEY, creator_id=ctx.author.id)

    em = discord.Embed(title=f"{ctx.author.name}'s Archives")

    for a in res:
        # take the message id and make an api call to get that message
        msg = getMsg(key=KEY, id=a['message_id'])[0]

        em.add_field(name=f"**{a['title']}**",
                     value=f"**message**: {a['message_id']}\n"
                            f"**contents**: {msg['contents']}\n\n",
                     inline=False)

    dm_channel = await bot.fetch_user(ctx.author.id)
    await discord.DMChannel.send(dm_channel, embed=em)

    await ctx.send("DM'd you your archives!")

# get a specific archive
@bot.command(aliases=["s"])
async def search(ctx, title):
    """
    Selects all of a user's archives with the appropriate title.

    todo:
        make embeds look better
        show attachements
        include jump_url
    """
    if ctx.author.bot: return # does not answer to bots

    res = getUserArchivesByTitle(key=KEY, creator_id=ctx.author.id, title=title)

    em = discord.Embed(title=f"{ctx.author.name}'s Archives")

    for a in res:
        # take the message id and make an api call to get that message
        msg = getMsg(key=KEY, id=a['message_id'])[0]

        em.add_field(name=f"**{a['title']}**",
                     value=f"**id**: {a['id']}\n"
                           f"**message**: {a['message_id']}\n"
                           f"**creation date**: {a['creation_date']}\n"
                           f"**contents**: {msg['contents']}\n\n",
                     inline=False)

    dm_channel = await bot.fetch_user(ctx.author.id)
    await discord.DMChannel.send(dm_channel, embed=em)

    await ctx.send(res)

@bot.command()
async def stats(ctx):
    """
    Shows how many embeds a user has made
    :param ctx:
    :return:
    """
    if ctx.author.bot: return  # does not answer to bots

    em = discord.Embed(title=f"{ctx.author.name}'s statistics") # the embed
    archives = getUserArchives(key=KEY, creator_id=ctx.author.id) # the archives

    em.set_thumbnail(url=ctx.author.avatar_url)
    em.add_field(name="Archives count", value=str(len(archives)), inline=False)

    await ctx.send(embed=em)
