import discord
from discord.ext import commands
from config.settings import BOT_TOKEN, PREFIX
from events import message_events
from commands import ticket_commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.dm_messages = True
intents.guilds = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

message_events.setup(bot)
ticket_commands.setup(bot)

bot.run(BOT_TOKEN)