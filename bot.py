import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# Retrieves the .env values for the bot's token, server, and server ID 
# respectively
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = os.getenv('GUILD_ID')
TEXT_CHANNEL_ID = os.getenv('CHANNEL_ID')
# Denotes the prefix to use the bot in a text channel, in this case '+'
bot = commands.Bot(command_prefix='+',intents=discord.Intents.all())

# Bot command that randomly selects a user in the voice channel of 
# whoever initiated the command, and disconnects them
@bot.command(name='spin')
async def spin(ctx):
    guild = bot.get_guild(int(GUILD_ID))
    channel = bot.get_channel(int(TEXT_CHANNEL_ID))
    vc = ctx.author.voice.channel
    # Checks that the text author is in a valid VC
    if vc:
        # Gets list of voice states in selected voice channel. Voice 
        # states represent the active connection of a user to the
        # voice channel
        voice_states = vc.voice_states
        if len(voice_states) > 0:
            unlucky = random.choice(list(voice_states))
            # gets voice_client of selected user by id (unlucky)
            victim = guild.get_member(unlucky)
            # Disconnects user
            await victim.move_to(None)
            # Special message if the person execuitng the message is 
            # the victim
            if(ctx.author.id == unlucky):
                await channel.send(f'<@{unlucky}> was super unlucky!')
            else: 
                await channel.send(f'<@{unlucky}> was shot!')

bot.run(TOKEN)
