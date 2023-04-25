import os
import discord
from helper import Helper
from shopkeeper import ShopKeeper
from dotenv import load_dotenv

load_dotenv()

class MaestroDelCalabozo(discord.Client):
    def __init__(self, intents) -> None:
        super().__init__(intents=intents)
        self.helper = Helper()
        self.shopKeeper = ShopKeeper()
    
    async def on_ready(self):
        print('Logged in as {0.name}'.format(self.user))
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        print("Mensaje recibido")
        print(message.content)
        
        # Helper
        if message.content.startswith('!help'):
            await message.channel.send(embed=self.helper.on_message(message))
            return
            
        # ShopKeeper
        if message.content.startswith('!shop'):
            await message.channel.send(embed=self.shopKeeper.on_message(message))
            return


intents = discord.Intents(messages=True, members=True)
clnt = MaestroDelCalabozo(intents)
clnt.run(str(os.getenv('DISCORD_BOT_TOKEN')))