import nextcord
from nextcord.ext import commands, tasks
from datetime import datetime, timedelta

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    update_channel.start()

    await update_channel()

@tasks.loop(hours=24)
async def update_channel():
    guild_id = 1122248853140291644 
    channel_id = 1174986288965890079 

    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)

    if channel and isinstance(channel, nextcord.VoiceChannel):
        current_date = datetime.utcnow().strftime('%A | %m-%d')
        
        # Update the voice channel name
        await channel.edit(name=f"Date: {current_date}")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"An error occurred in event {event}.")

# Replace 'YOUR_TOKEN' with your actual bot token
bot.run('YOUR_TOKEN')
