from discord.ext import commands
from .database import CustomGuild

class CustomContext(commands.Context):
    """Use a subclassed context for more functionality."""
    
    @property
    async def guild(self):
        return CustomGuild(super().guild)
