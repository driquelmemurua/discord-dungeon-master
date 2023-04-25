from discord import Embed, Colour
import requests
from tabulate import tabulate

class ShopKeeper:
    def __init__(self) -> None:
           self.mainKey = '!shop'
           
    def on_message(self, message) -> Embed:
        ## Base Command
        if message.content == self.mainKey:
            title = "Shop Keeper Main Commands"
            desc = f"""
            {self.commands()}"""
            return Embed(title=title, description=desc)
        
        cmd = message.content.split("-")
        ## Equipment Information
        if cmd[1] == 'eqmt':
            return self.getEquipmentInfo(cmd)
            
        ## Magic Equipment Information
        if cmd[1] == 'mgeqmt':
            return self.getMagicEquipmentInfo(cmd)
        
        # If no case is reached then is considered an error
        color = Colour.brand_red()
        title = "Error"
        desc = "ShopKeeper reached with wrong message: Wrong Msg or Not implemented"
        return Embed(color=color, title=title, description=desc)
    
    def commands(self):
        return f"""
    {self.mainKey}-eqmt <equipment> -> returns information of equipment if exist.
    {self.mainKey}-mgeqmt <equipment> -> returns information of magic equipment if exist."""
    
    def getEquipmentInfo(self, cmd: str) -> Embed:
        query = cmd[1][len('mgEqmt '):].strip()
        try:
            api_url = 'https://www.dnd5eapi.co/api/equipment/' + query
            print(f"Query: {api_url}")
            response = requests.get(api_url)
        except:
            color = Colour.brand_red()
            title = "Error"
            desc = "ShopKeeper couldn't reach DnD API"
            return Embed(color=color, title=title, description=desc)

        if response.status_code == 200:
            data = response.json()
            title = data['name']
            desc = f"""
Cost: {data['cost']['quantity']} {data['cost']['unit']}
Damage: {data['damage']['damage_dice']} de tipo \"{data['damage']['damage_type']['name']}\"
Rango normal:{data['range']['normal']}
Rango distancia: {data['range']['long'] if 'long' in data['range'].keys() else 'No aplica'}
Peso: {data['weight']} lb"""
            print("Embeded Content")
            return Embed(title=title, description=desc)
        else:
            color = Colour.brand_red()
            title = "Error"
            desc = "ShopKeeper reached with wrong message: Wrong Msg or Not implemented"
            return Embed(color=color, title=title, description=desc)
        
    def getMagicEquipmentInfo(self, cmd: str) -> Embed:
        item = cmd[2:]
        query = ""
        for elem in item:
            query += f"{elem}-"
        query = query[:-1]
        try:
            api_url = 'https://www.dnd5eapi.co/api/magic-items/' + query
            print(f"Query: {api_url}")
            response = requests.get(api_url)
        except:
            color = Colour.brand_red()
            title = "Error"
            desc = "ShopKeeper couldn't reach DnD API"
            return Embed(color=color, title=title, description=desc)

        if response.status_code == 200:
            data = response.json()
            print(data)
            title = data['name']
            desc = ""
            for i, elem in enumerate(data['desc']):
                #Usar tabulate para ordenar tablas en el mensaje
                desc += f"""
                {elem}"""
            print("Embeded Content")
            return Embed(title=title, description=desc)
        else:
            color = Colour.brand_red()
            title = "Error"
            desc = "ShopKeeper reached with wrong message: Wrong Msg or Not implemented"
            return Embed(color=color, title=title, description=desc)
