#HexBot Created by TechnicSparks
#Bot created for the HexIT Discord server!



import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

#Initzalizing Client and Running Client
client = MyClient()
client.run('NDg3NDkxNjE2Mzc0Nzg0MDAw.DnOcvA.tRhKusrggXudLNtYW5Pwo00hxME')