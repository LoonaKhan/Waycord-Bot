import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='w;', help_command=None)
discord.AllowedMentions(replied_user=True)