import discord, asyncio
from redbot.core import checks, commands
from redbot.core.bot import Red
from redbot.core.i18n import cog_i18n, Translator
from .converters import FuzzyRole

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
    async def loudsay(self, ctx, role: FuzzyRole, *, message=None):
        """Same as `[p]say` command but [botname] can mention roles"""
        message = f"{role.mention}: {message}" if message else role.mention
        try:
            await ctx.message.delete()
        except:
            pass
        mentionPerms = discord.AllowedMentions(everyone=True, roles=True, users=True)
        me = ctx.channel.guild.me
        if (
            not role.mentionable
            and not ctx.channel.permissions_for(me).mention_everyone
            and ctx.channel.permissions_for(me).manage_roles
            and me.top_role > role
        ):
            await role.edit(mentionable=True)
            await ctx.send(message, allowed_mentions=mentionPerms)
            await asyncio.sleep(1.5)
            await role.edit(mentionable=False)
        else:
            await ctx.send(message, allowed_mentions=mentionPerms)
                    
