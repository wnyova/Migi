import requests
import xml.etree.ElementTree as ET
from redbot.core import commands

class GempaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gempa")
    async def get_earthquake_info(self, ctx):
        """Get recent earthquake data in Indonesia."""
        url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the XML response
            root = ET.fromstring(response.content)
            gempa = root.find(".//gempa")

            if gempa is not None:
                magnitude = gempa.find("Magnitude").text
                location = gempa.find("Wilayah").text
                date = gempa.find("Tanggal").text
                time = gempa.find("Jam").text
                depth = gempa.find("Kedalaman").text

                await ctx.send(f"> Gempa Terakhir:\n> \n> **Magnitudo:** {magnitude}\n> **Lokasi:** {location}\n> **Tanggal:** {date}\n> **Waktu:** {time}\n> **Kedalaman:** {depth}")
            else:
                await ctx.send("Tidak ada informasi gempa terbaru.")
        else:
            await ctx.send("Tidak dapat mengambil data gempa. Silakan coba lagi nanti.")

def setup(bot):
    bot.add_cog(GempaCog(bot))
