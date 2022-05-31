import discord
import random

TOKEN = "YOUR_TOKEN_HERE"

client = discord.Client()

randomLinks = ['https://www.youtube.com/watch?v=ugC9Yzd5E74','https://www.youtube.com/watch?v=6irJYI5ZK6k','https://www.youtube.com/watch?v=T0A_cm6DIGM','https://www.youtube.com/watch?v=42MMQVaoNtE','https://www.youtube.com/watch?v=8Scm09bwT_s','https://www.youtube.com/watch?v=zIJNRYxpppA','https://www.youtube.com/watch?v=rfsXvOFv6Ow'] 

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.content == ('pls baba'):
        random_message = randomLinks[random.randrange(0, len(randomLinks))]
        await message.channel.send(random_message)
    if message.content == ('pls help'):
        await message.channel.send("pls baba or pls code")
    if message.content == ('pls code'):
        await message.channel.send('https://github.com/KyzoCryptoboy/babaBot-discordBot')
        #Please Leave My link Here So Other People Can Add It To😘

client.run(TOKEN)