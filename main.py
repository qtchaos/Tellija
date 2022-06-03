import asyncio
import logging
import os

import discord
from dotenv import load_dotenv

from api.articles import fetch
from commands.latest import latest

client = discord.Client()
load_dotenv()
PREFIX = "!"
logging.basicConfig(level=logging.INFO)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f"{PREFIX}ping"):
        await message.channel.send("Pong!")

    if message.content.startswith(f"{PREFIX}latest"):
        while True:
            data = fetch()
            if data:
                await message.channel.send(embed=latest(data))
            await asyncio.sleep(15)


client.run(os.getenv("TOKEN"))
