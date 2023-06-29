# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = os.getenv('GUILD_ID')
bot = commands.Bot(command_prefix='+',intents=discord.Intents.all())

@bot.command(name='spin')
async def spin(ctx):
    guild = bot.get_guild(int(GUILD_ID))
    print(guild)
    vc = ctx.author.voice.channel
    if vc:
        voice_states = vc.voice_states
        if len(voice_states) > 0:
            unlucky = random.choice(list(voice_states))
            victim = guild.get_member(unlucky)
            await victim.move_to(None)
bot.run(TOKEN)
