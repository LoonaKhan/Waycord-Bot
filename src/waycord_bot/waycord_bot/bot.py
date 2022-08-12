"""
Waycord bot bot.py file.
the main file/process.
"""

# general imports (discord, .env etc)
import discord
from utils.load_env import *

# bot info
from bot_info import *

# all commands
from commands.archives import *
from commands.general import *
from commands.help import *

# subprocesses imports




# runs when the bot connects
@bot.event
async def on_ready():
    print("online")


# runs the subprocesses



# runs the bot
bot.run(TOKEN)