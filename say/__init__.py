from redbot.core.bot import Red
from .say import Say

async def setup(bot: Red):
    cog = Say(bot)
    bot.add_cog(cog)
    await cog.initialize()