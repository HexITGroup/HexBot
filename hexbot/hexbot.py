# HexBot Created by TechnicSparks
# Bot created for the HexIT Discord server!

import discord
from discord.ext import commands
import discord.utils
import json


def token_handle(fileDir):
    with open(fileDir, "r") as f:
        return json.loads(f.read())["token"]


prefix = "."

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("Logging in as: {0}".format(bot.user))


@bot.event
async def on_message(message):
    """
    Command logger
    """
    print("In {0.guild} - #{0.channel}, {0.author} sent: {0.content}".format(message))
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    """
    Basic ping command
    """
    latency = bot.latency
    await ctx.send(f"Ponged at the speed of {latency:.2f} ms")


@bot.command()
async def echo(ctx, *, content: str):
    """
    Basic echo command
    """
    await ctx.send(content)


@bot.command()
async def giverole(ctx, *, content: str):
    """
    Grants sender the requested role, if it exists
    """
    user = ctx.message.author
    role = discord.utils.find(
        lambda x: x.name.lower() == content.lower(), ctx.guild.roles
    )
    if role:
        await user.add_roles(role)
        await ctx.send(f"You now have the role {role.name}")
    else:
        await ctx.send(f"Role {role.name} not found! Please double check")


@bot.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix: str = None):
    if prefix:
        bot.command_prefix = prefix
        await ctx.send(f"New prefix: {prefix}")
    else:
        await ctx.send("No prefix specified! Not changing")


@setprefix.error
async def setprefix_error(error, ctx):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permissions to change the prefix!")


# Initzalizing Client and Running Client
botConfig = token_handle("/var/botcfg.json")
bot.run(botConfig)
