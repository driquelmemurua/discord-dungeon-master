import os
import discord
import requests

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents(messages=True, members=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!estado'):
        query = message.content[len('!estado '):].strip()
        response = requests.get('http://www.dnd5eapi.co/api/features/' + query)

        if response.status_code == 200:
            data = response.json()
            embed = discord.Embed(title=data['name'], description=data['desc'][0], color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('No se pudo encontrar información sobre ese estado.')

client.run(BOT_TOKEN)