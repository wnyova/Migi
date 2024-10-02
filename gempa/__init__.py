from .gempa import GempaCog

async def setup(bot):
    await bot.add_cog(GempaCog(bot))
