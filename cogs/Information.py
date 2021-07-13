import discord, requests
from discord.ext import commands
from discord.ext.commands.context import Context

class Information(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    #Corona Info Indonesia
    @commands.command(aliases=["covid-19", "covid19", "coronavirus", "korona", "corona"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def covid(self, ctx, *countryName):
        try:
            if not countryName:
                api = requests.get(f"https://coronavirus-19-api.herokuapp.com/countries/indonesia").json()
                positif = api["cases"]
                sembuh = api["recovered"]
                meninggoy = api["deaths"]
                dirawat = api["active"]

                embed = discord.Embed(
                    color = discord.Colour.red()
                )
                embed.set_author(name="Status COVID-19 di Indonesia", icon_url="https://www.suse.com/c/wp-content/uploads/2020/03/corona.gif")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/817023521946599475/220px-SARS-CoV-2_without_background.png")
                embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                embed.add_field(name="Kasus Positif", value=positif, inline=False)
                embed.add_field(name="Kasus Sembuh", value=sembuh, inline=False)
                embed.add_field(name="Kasus Meninggal", value=f"{meninggoy}\n", inline=False)
                embed.add_field(name="Masih Dirawat", value=f"{dirawat}\n\nTetap patuhi protokol kesehatan. Gunakan masker ketika berada di luar rumah, jaga jarak untuk meminimalisir kemungkinan tertular, selalu cuci tangan pakai sabun, dan jangan sampai tertular.", inline=False)
                await ctx.send(embed=embed)
            else:
                negara = "%20".join(countryName)
                api = requests.get(f"https://coronavirus-19-api.herokuapp.com/countries/{negara}").json()
                neggara = api["country"]
                confirmed = api["cases"]
                recovered = api["recovered"]
                deaths = api["deaths"]
                active = api["active"]

                embed = discord.Embed(
                    color = discord.Colour.red()
                )
                embed.set_author(name=f"Status COVID-19 di {neggara}", icon_url="https://www.suse.com/c/wp-content/uploads/2020/03/corona.gif")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805880890194264137/817023521946599475/220px-SARS-CoV-2_without_background.png")
                embed.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                embed.add_field(name="Kasus Positif", value=confirmed, inline=False)
                embed.add_field(name="Kasus Sembuh", value=recovered, inline=False)
                embed.add_field(name="Kasus Meninggal", value=f"{deaths}\n", inline=False)
                embed.add_field(name="Masih Dirawat", value=f"{active}\n\nTetap patuhi protokol kesehatan. Gunakan masker ketika berada di luar rumah, jaga jarak untuk meminimalisir kemungkinan tertular, selalu cuci tangan pakai sabun, dan jangan sampai tertular.", inline=False)
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "Nama negara tidak valid!",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)
            
            
    #color
    @commands.command(aliases=["hex", "colour", "warna"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def color(self, ctx, color=None):
        try:
            if not color:
                await ctx.reply("**Invalid Syntax!** Please write HEX color that you want to know the detail **without `#`**.\nExample: `c.color ffff00`")
            else:
                hasil = requests.get(f"https://www.thecolorapi.com/id?hex={color}").json()
                nama_warna = hasil["name"]["value"]
                kode_hex = hasil["hex"]["value"]
                rgb_R = hasil["rgb"]["r"]
                rgb_G = hasil["rgb"]["g"]
                rgb_B = hasil["rgb"]["b"]
                hsl_H = hasil["hsl"]["h"]
                hsl_S = hasil["hsl"]["s"]
                hsl_L = hasil["hsl"]["l"]
                hsv_H = hasil["hsv"]["h"]
                hsv_S = hasil["hsv"]["s"]
                hsv_V = hasil["hsv"]["v"]
                cmyk_C = hasil["cmyk"]["c"]
                cmyk_M = hasil["cmyk"]["m"]
                cmyk_Y = hasil["cmyk"]["y"]
                cmyk_K = hasil["cmyk"]["k"]
                xyz_X = hasil["XYZ"]["X"]
                xyz_Y = hasil["XYZ"]["Y"]
                xyz_Z = hasil["XYZ"]["Z"]

                warnaEmbed = int(f"{color}", 16)
                embed = discord.Embed(
                    title = f"Warna: {nama_warna}",
                    color = warnaEmbed
                )
                embed.set_thumbnail(url=f'https://some-random-api.ml/canvas/colorviewer?hex={color}')
                embed.set_footer(text=f'Di-Request oleh {ctx.author}', icon_url=ctx.author.avatar_url)
                embed.add_field(name="HEX", value=f"`{kode_hex}`")
                embed.add_field(name="RGB", value=f"`{rgb_R}, {rgb_G}, {rgb_B}`")
                embed.add_field(name="HSL", value=f"`{hsl_H}, {hsl_S}, {hsl_L}`")
                embed.add_field(name="HSV", value=f"`{hsv_H}, {hsv_S}, {hsv_V}`")
                embed.add_field(name="CMYK", value=f"`{cmyk_C}, {cmyk_M}, {cmyk_Y}, {cmyk_K}`")
                embed.add_field(name="XYZ", value=f"`{xyz_X}, {xyz_Y}, {xyz_Z}`")
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                title = ":x: Invalid Color!",
                color = 0xff0000
            )
            await ctx.reply(embed=embed)
            
    #gempa
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gempa(self, ctx):
        api = requests.get("https://gempa-api-zhirrr.vercel.app/api/gempa").json()
        waktu = api["Waktu"]
        lintang = api["Lintang"]
        bujur = api["Bujur"]
        magnitudo = api["Magnitudo"]
        kedalaman = api["Kedalaman"]
        wilayah = api["Wilayah"]
        map = api["Map"]

        tanagoyang = discord.Embed(
            title = "Gempa Bumi Terkini di Indonesia",
            color = 0xff0000
        )
        tanagoyang.set_thumbnail(url="http://iconsetc.com/icons-watermarks/simple-red/ocha/ocha_disaster-earthquake/ocha_disaster-earthquake_simple-red_512x512.png")
        tanagoyang.set_footer(text=f"Di-Request oleh {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        tanagoyang.add_field(name="Wilayah", value=wilayah, inline=False)
        tanagoyang.add_field(name="Waktu", value=waktu, inline=False)
        tanagoyang.add_field(name="Kedalaman", value=kedalaman, inline=False)
        tanagoyang.add_field(name="Lintang", value=lintang, inline=False)
        tanagoyang.add_field(name="Bujur", value=bujur, inline=False)
        tanagoyang.add_field(name="Magnitudo", value=f"{magnitudo}\n\nJangan panik, tetap pantau keadaan terkini, dan waspada terhadap gempa susulan yang mungkin bisa saja terjadi.", inline=False)
        await ctx.send(embed=tanagoyang)
        
     
       
def setup(client):
    client.add_cog(Information(client))
