#This is not a functional bot *yet*.
print("Bot starting up...")
import discord
import os
import sys
token = "{token}"
client = discord.Client()
f1 = open("log", "a")
f2 = open("untrusted", "a")
@client.event
async def on_message(message):
    guy = "" #admin only command
    if guy2 == str(message.author):
        msgc = message.content
        f1.write(attavariable + "\n")
    if message.content.startswith("/"): #public command
        mgsc = message.content
client.run(token)
