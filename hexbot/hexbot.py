#HexBot Created by TechnicSparks
#Bot created for the HexIT Discord server!

import discord
from discord.ext import commands 
import json

                                                       
def token_handle(fileDir):
    f = open(fileDir, "r")
    jstr = f.read()
    jsn = json.loads(jstr)
    return jsn["token"]

prefix = "."

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Logging in as: {0}".format(bot.user))

@bot.event
async def on_message(message):
    print("In {0.guild} - #{0.channel}, {0.author} sent: {0.content}".format(message))
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):

    latency = bot.latency
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def giverole(ctx, *, content:str):
    user = ctx.message.author

    for role in ctx.guild.roles:
        if role.name.lower() == content.lower():
            await user.add_roles(role)
            break


#Initzalizing Client and Running Client
botConfig = token_handle("/var/botcfg.json")
bot.run(botConfig)