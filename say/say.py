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
    @commands.guild_only()
    async def say(self, ctx: commands.Context, *, message):
        """Make [botname] say something."""
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(message)
        
    @commands.command("loudsay", aliases=["lecho", "lsay", "loudecho", "forcemention"])
    @checks.admin_or_permissions(manage_roles=True)
    async def loudsay(self, ctx, *, message):
        """Same as `[p]say` command but [botname] can mention roles"""
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(message, allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True))
                    
