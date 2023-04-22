from discord import Embed, Colour
import requests

class ShopKeeper:
    def __init__(self) -> None:
           self.mainKey = '!shop'
           
    def on_message(self, message):
        ## Base Command
        if message.content == self.mainKey:
            title = "Shop Keeper Main Commands"
            desc = f"""
            {self.commands()}"""
            return Embed(title=title, description=desc)
        
        ## Equipment Information
        if 'eqmt' in message.content:
            cmd = message.content.split("-")
            print(cmd)
            query = cmd[1][len('eqmt '):].strip()
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
        else:
            color = Colour.brand_red()
            title = "Error"
            desc = "ShopKeeper reached with wrong message: Wrong Msg or Not implemented"
            return Embed(color=color, title=title, description=desc)
    
    def commands(self):
        return f"""
    {self.mainKey} <equipment> -> returns information of equipment if exist."""
