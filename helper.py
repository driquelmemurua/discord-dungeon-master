from discord import Embed, Colour

class Helper:
    def __init__(self) -> None:
        self.mainKey = '!help'
        
    def on_message(self, message):
        if message.content == self.mainKey:
            title = "Main Commands"
            desc = f"""
            {self.commands()}"""
            return Embed(title=title, description=desc)
        else:
            color = Colour.brand_red()
            title = "Error"
            desc = "Helper reached with wrong message: Wrong Msg or Not implemented"
            return Embed(colour=color, title=title, description=desc)
        
    def commands(self):
        res = """!help -> Returns this message with helpful commands.
        !shop -> Returns list of commands for the shop keeper."""
        return res
    