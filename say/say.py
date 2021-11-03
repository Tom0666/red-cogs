import discord, asyncio
from redbot.core import checks, commands
from redbot.core.bot import Red
from redbot.core.i18n import cog_i18n, Translator

_ = T_ = Translator("Say", __file__)

@cog_i18n(_)
class Say(commands.Cog):
    """Make the bot say something."""
    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot
        self._ready = asyncio.Event()

    async def initialize(self):
        self._ready.set()

    @commands.command("say", aliases=["echo"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def say(self, ctx: commands.Context, message):
        """Make the [botname] say something."""
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(message)