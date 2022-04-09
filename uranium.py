import asyncio
import json
import random
import time
from asyncio.tasks import sleep
from datetime import *

import discord
from discord import (ChannelType, Color, Embed, Game, Status, activity,
                     channel, client, colour, embeds, message)
from discord.ext import commands, tasks
from discord.ext.commands.bot import AutoShardedBot
from discord.ext.commands.core import check
from paramiko import Channel
from pyfiglet import CharNotPrinted, Figlet
from gtts import gTTS
import io
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType


bot = commands.Bot(command_prefix= "!",intents=discord.Intents.all(), description= "Uranium a été dev par un_dieu#3173")
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands = True)

@bot.event
async def on_ready():
    activity = discord.Game(name = "Uranium", type = 1)
    await bot.change_presence(status = discord.Status.dnd, activity=activity)
    print("Bot prêt")


@bot.event
async def on_message(message):
    if message.content == "!authenticator":
        await message.author.send("https://cdn.discordapp.com/attachments/955059465751777290/956182588106616882/Noir_et_Blanc_Agence_Immobiliere_Paysage_Recto_Carte_de_visite.png")



bot.run("")
