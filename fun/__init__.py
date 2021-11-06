from redbot.core.bot import Red
from .fun import Fun


async def setup(bot: Red):
    cog = Fun(bot)
    bot.add_cog(cog)
    await cog.initialize()
