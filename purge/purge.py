import discord
from redbot.core import checks, commands
from redbot.core.i18n import cog_i18n, Translator

_ = T_ = Translator("Purge", __file__)

@cog_i18n(_)
class Purge(commands.Cog):
    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot

    @commands.command("purge", aliases=["delete", "prune"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    @checks.mod_or_permissions(manage_messages=True)
    async def purge(self, ctx: commands.Context, amount: int):
        """
        Delete multiple messages at once!

        **Arguments**:
        > <amount> = the amount of messages to delete.
        """
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
