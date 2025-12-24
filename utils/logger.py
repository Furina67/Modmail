import datetime
import discord
from config.settings import SERVER_ID, LOG_CHANNEL_ID

async def log_close(bot, uid, staff):
    ch = bot.get_guild(SERVER_ID).get_channel(LOG_CHANNEL_ID)
    if not ch:
        return

    embed = discord.Embed(
        title="Ticket Closed",
        color=discord.Color.red(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="User ID", value=str(uid), inline=False)
    embed.add_field(name="Closed By", value=f"{staff} ({staff.id})", inline=False)
    await ch.send(embed=embed)