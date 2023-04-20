import os
import discord
import requests


intents = discord.Intents(messages=True, members=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print("Mensaje recibido\n")
    # ShopKeeper
    if message.content.startswith('!shop'):
        print("SHOP: ")
        query = message.content[len('!shop '):].strip()
        api_url = 'https://www.dnd5eapi.co/api/equipment/' + query
        print(f"Query: {api_url}")
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            desc = f"""
Cost: {data['cost']['quantity']} {data['cost']['unit']}
Damage: {data['damage']['damage_dice']} de tipo \"{data['damage']['damage_type']['name']}\"
Rango normal:{data['range']['normal']}
Rango distancia: {data['range']['long'] if 'long' in data['range'].keys() else 'No aplica'}
Peso: {data['weight']} lb"""
            embed = discord.Embed(title=data['name'], description=desc, color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('No se pudo encontrar información sobre ese estado.')

os.getenv('DISCORD_BOT_TOKEN')