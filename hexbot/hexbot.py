#HexBot Created by TechnicSparks
#Bot created for the HexIT Discord server!



import discord
import json

class Configuration:
    def __init__(self, fileDir):
        f = open(fileDir, "r")
        jstr = f.read()
        jsn = json.loads(jstr)
        self.botToken = jsn["token"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

#Initzalizing Client and Running Client
clientConfig = Configuration("/var/botcfg.json")
client = MyClient()
client.run(clientConfig.botToken)