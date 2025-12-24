import discord
from config.settings import STAFF_ROLE_ID
from database.tickets import get_ticket, set_claim, close_ticket, find_owner
from utils.logger import log_close

class TicketView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="Claim", style=discord.ButtonStyle.primary)
    async def claim(self, interaction, button):
        if STAFF_ROLE_ID not in [r.id for r in interaction.user.roles]:
            return await interaction.response.send_message("Not staff.", ephemeral=True)

        owner = find_owner(interaction.channel.id)
        ticket = get_ticket(owner)

        if ticket["claimed"]:
            return await interaction.response.send_message(
                f"Already claimed by <@{ticket['claimed']}>", ephemeral=True
            )

        set_claim(owner, interaction.user.id)
        button.disabled = True
        button.label = f"Claimed by {interaction.user.display_name}"

        await interaction.response.edit_message(view=self)
        await interaction.channel.send(f"Ticket claimed by {interaction.user.mention}")

    @discord.ui.button(label="Close", style=discord.ButtonStyle.danger)
    async def close(self, interaction, _):
        if STAFF_ROLE_ID not in [r.id for r in interaction.user.roles]:
            return await interaction.response.send_message("Not staff.", ephemeral=True)

        owner = find_owner(interaction.channel.id)
        ticket = get_ticket(owner)

        if ticket["claimed"] and ticket["claimed"] != interaction.user.id:
            return await interaction.response.send_message(
                "Only the claimer can close this ticket.", ephemeral=True
            )

        try:
            user = await self.bot.fetch_user(owner)
            await user.send("Your ticket has been closed by staff.")
        except:
            pass

        close_ticket(owner)
        await log_close(self.bot, owner, interaction.user)
        await interaction.channel.edit(locked=True, archived=True)
        await interaction.response.send_message("Ticket closed.", ephemeral=True)