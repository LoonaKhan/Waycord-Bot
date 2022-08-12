import discord
from discord.ext import commands
from discord import Color as c

bot = commands.Bot(command_prefix='w;', help_command=None)
discord.AllowedMentions(replied_user=True)