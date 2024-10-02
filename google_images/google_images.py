import discord
from redbot.core import commands
import aiohttp
import os
from dotenv import load_dotenv

class GoogleImages(commands.Cog):
    """Google Image Search Cog"""

    def __init__(self, bot):
        self.bot = bot
        load_dotenv()  # Load environment variables from .env file
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.cx = os.getenv('GOOGLE_SEARCH_ENGINE_ID')

    @commands.command()
    async def googleimg(self, ctx, *, query: str):
        """Search Google Images"""
        if not self.api_key or not self.cx:
            await ctx.send("API key or Search Engine ID is not set.")
            return

        search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={self.cx}&key={self.api_key}&searchType=image"

        async with aiohttp.ClientSession() as session:
            async with session.get(search_url) as response:
                data = await response.json()

                if "items" not in data:
                    await ctx.send("No images found.")
                    return

                image_url = data["items"][0]["link"]
                await ctx.send(image_url)
