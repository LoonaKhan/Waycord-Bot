"""
All archived commands
"""
import asyncio
import discord
from utils.load_env import *
from bot_info import bot, c
from waycord_api.calls import getUserArchivesByTitle, getUserArchives, addArchive, delArchive

# delete an archive
@bot.command()
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

# get all user archives; todo: allows the user to search for an archive?

# get a specific archive