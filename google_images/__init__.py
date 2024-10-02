from .google_images import GoogleImages

async def setup(bot):
    await bot.add_cog(GoogleImages(bot))
