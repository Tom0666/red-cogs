from redbot.core.bot import Red
from .purge import Purge


async def setup(bot: Red):
    cog = Purge(bot)
    bot.add_cog(cog)
    await cog.initialize()
