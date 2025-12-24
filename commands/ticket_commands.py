from discord.ext import commands
from database.tickets import get_ticket, close_ticket, find_owner
from utils.logger import log_close
import discord

def setup(bot):

    @bot.command()
    async def close(ctx):
        if not isinstance(ctx.channel, discord.Thread):
            return

        owner = find_owner(ctx.channel.id)
        ticket = get_ticket(owner)

        if ticket["claimed"] and ticket["claimed"] != ctx.author.id:
            return await ctx.reply("Only the claimer can close this ticket.")

        close_ticket(owner)
        await log_close(bot, owner, ctx.author)
        await ctx.channel.edit(locked=True, archived=True)
        await ctx.reply("Ticket closed.")