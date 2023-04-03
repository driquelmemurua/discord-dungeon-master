import os
import discord
import requests
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents(messages=True, members=True, message_content=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content:
        await message.channel.send('Estoy trabajando en ello...')
        if message.content.startswith('!estado'):
            query = message.content[len('!estado '):].strip()
            response = requests.get('http://www.dnd5eapi.co/api/conditions/' + query)

            if response.status_code == 200:
                data = response.json()
                embed = discord.Embed(title=data['name'], description=data['desc'][0], color=0x00ff00)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('No se pudo encontrar información sobre ese estado.')

if __name__ == '__main__':
    client.run(os.getenv('DISCORD_BOT_TOKEN'))
