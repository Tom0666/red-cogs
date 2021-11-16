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
        role_obj = role
        if not role_obj.mentionable:
            await role_obj.edit(mentionable=True)
            if message:
                await ctx.send(
                    "{}: {}".format(role_obj.mention, message),
                    allowed_mentions=discord.AllowedMentions(
                        everyone=False, users=False, roles=[role_obj]
                    ),
                )
            else:
                await ctx.send(
                    "{}".format(role_obj.mention),
                    allowed_mentions=discord.AllowedMentions(
                        everyone=False, users=False, roles=[role_obj]
                    ),
                )
            await asyncio.sleep(5)
            await role_obj.edit(mentionable=False)
        else:
            if message:
                await ctx.send(
                    "{}: {}".format(role_obj.mention, message),
                    allowed_mentions=discord.AllowedMentions(
                        everyone=False, users=False, roles=[role_obj]
                    ),
                )
            else:
                await ctx.send("{}".formal(role_obj.mention), allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=[role_obj]))
                    
