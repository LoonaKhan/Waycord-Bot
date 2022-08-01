"""
All general commands here
"""
import asyncio
import discord
from bot_info import bot, c

# ping measurement
@bot.command()
async def ping(ctx):
    if ctx.author.bot: return # do not allow bots

    await ctx.send(f"Pong! \nBot latency: **{round(bot.latency*1000, 2)} ms**")