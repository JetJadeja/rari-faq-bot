import os
from dotenv import load_dotenv

import wit
import discord

from responses import response, greetings
from random import choice

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")

discord_client = discord.Client()
wit_client = wit.Wit(WIT_ACCESS_TOKEN)

@discord_client.event
async def on_message(message):
    if message.author == discord_client.user:
        await message.edit(suppress=True)
        return

    res = wit_client.message(message.content)
    intent = res["intents"][0]["name"]
    greeting = choice(greetings) if intent in ["helpNeeded", "priceTalk"] else ""
    print(f'User asking a question. Intent: {intent}')

    await message.channel.send(f"{greeting} {response[intent]}", embed=None)

discord_client.run(DISCORD_TOKEN)


