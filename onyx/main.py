from discord.ext import commands
import discord
import yaml
import os

class Bot(commands.Bot):
    async def get_prefix(self, bot, message):
        """Fetches the current prefix in the guild from the database."""
        return commands.when_mentioned_or("onyx ")

    def __init__(self):
        """Initialize the bot and load all extensions."""

        with open("C:/onyx/config.yml", encoding = "UTF-8") as f:
            self.config = yaml.safe_load(f)

        super().__init__(
            command_prefix = self.get_prefix,
            intents = discord.Intents.default()
        )

client = Bot()
client.load_extension("jishaku") # Load the debugging cog.

@client.check
async def check(ctx):
    return True

token = os.getenv("TOKEN")
client.run(token)
