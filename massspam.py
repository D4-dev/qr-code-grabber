import discord
import random
import os

token = input('Entrer votre token > ')
guild = input('Entrer l id du serveur > ')
client = discord.Client(status=discord.Status.online)

sentList = []

@client.event
async def on_ready():
    print("Je suis connecté sur le compte {0.user}".format(client))
    print("J'attend qu'un message soit envoyé sur le serveur est j'enveraiss le QR Code")

@client.event
async def on_message(message):
    if message.guild.id == int(guild) and message.author.id not in sentList:
        sentList.append(message.author.id)
        print(f"sending -> {message.author.name}")
        await message.author.send("gift for uuu <3<3<3.")
        await message.author.send(file=discord.File(f"out/{random.choice(os.listdir('out'))}"))
client.run(token, bot=False)
