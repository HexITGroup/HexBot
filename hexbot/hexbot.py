#HexBot Created by TechnicSparks
#Bot created for the HexIT Discord server!

import discord
from discord.ext import commands 
import json

class Configuration:                                                           #Bot Token Handler
    def __init__(self, fileDir):
        f = open(fileDir, "r")
        jstr = f.read()
        jsn = json.loads(jstr)
        self.botToken = jsn["token"]

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Logging in as: {0}".format(bot.user))

@bot.event
async def on_message(message):
    print("In {0.guild} - #{0.channel}, {0.author} sent: {0.content}".format(message))

#Initzalizing Client and Running Client
botConfig = Configuration("/var/botcfg.json")
bot.run(botConfig.botToken)