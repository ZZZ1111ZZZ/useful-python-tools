print("Bot starting up...")
import discord
token = "{token}"
client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith("!fizz me up"): 
        n = 0
        while 0 == 0:
        n += 1
        if n % 3 == 0 and n % 5 == 0:
            await message.channel.send('fizzbuzz')
        elif n % 3 == 0:
            await message.channel.send('fizz')
        elif n % 5 == 0:
            await message.channel.send('buzz')
        else:
            await message.channel.send(n)
client.run(token)
#very standard, except as a discord bot
