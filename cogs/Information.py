import discord, requests, datetime, os
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
        
    #emoji info
    @commands.command(aliases=["emote", "em"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def emoji(self, ctx:Context, emoji:discord.PartialEmoji):
        embed = discord.Embed(
            title = "Emote Info",
            color = ctx.guild.me.color
        )
        embed.add_field(name="Name", value=f"[:{emoji.name}:]({emoji.url})")
        if emoji.animated is True:
            embed.add_field(name="Animated?", value="Yes")
        else:
            embed.add_field(name="Animated??", value="No")
        embed.add_field(name="ID", value=emoji.id)

        embed.add_field(name="Date Added", value=emoji.created_at.strftime("%d-%m-%Y | %H:%M:%S"))
        embed.add_field(name="ID Code", value=f"`{emoji.name}:{emoji.id}`")
        if emoji.is_custom_emoji() is True:
            embed.add_field(name="Custom Emote?", value="Yes")
        else:
            embed.add_field(name="Custom Emote?", value="No")

        embed.set_image(url=emoji.url)

        await ctx.send(embed=embed)
       
    #emoji enlarger
    @commands.command(aliases=["e", "enlarge", "en"])
    async def enlarge(self, ctx, emoji:discord.PartialEmoji=None):
        if not emoji:
            return await ctx.reply("**Invalid Syntax!** Please write what emote you want to enlarge!!\nExample: `c.e :1_CelLovely:`")

        link_emoji = emoji.url

        #donlot emojinya
        donlot = requests.get(link_emoji)
        file = open("resize.png", "wb")
        file.write(donlot.content)
        file.close()

        #kode utk me-resize emoji (untuk png saja)
        def pembesar_gambar(namafile:str):
            gambar = Image.open(namafile)
            atur_ukuran = gambar.resize((1000, 1000))
            atur_ukuran.save("resized.png")

        #resize emoji-nya
        async with ctx.typing():
            if str(link_emoji).endswith(".gif"):
                emubeddo = discord.Embed(
                    title = "Emote Enlarger",
                    description = "Unfotunately, `.gif` emote can't be resized same as `.png` emote",
                    color = ctx.guild.me.color
                )
                emubeddo.set_image(url=link_emoji)
                emubeddo.set_footer(text=f":{emoji.name}:")
                await ctx.send(embed=emubeddo)
            elif str(link_emoji).endswith(".png"):
                pembesar_gambar("resize.png")

                fairu = discord.File("./resized.png", filename="resized.png")
                emubeddo = discord.Embed(
                    title = "Emote Enlarger",
                    color = ctx.guild.me.color
                )
                emubeddo.set_image(url=f"attachment://resized.png")
                emubeddo.set_footer(text=f":{emoji.name}:")
                await ctx.send(file=fairu, embed=emubeddo)
                os.remove("resized.png")
                os.remove("resize.png")

    @enlarge.error
    async def on_enlarge_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.reply("Unfortunately, bot can't enlarge basic emote")
            
    #Spotify
     @commands.command()
    async def spotify(self, ctx, orang:discord.Member=None):
        orang = ctx.author if not orang else orang

        crotify = next((activity for activity in orang.activities if isinstance(activity, discord.Spotify)), None)

        if crotify is None:
            if orang == ctx.author:
                embed = discord.Embed(
                    description = f"You're not listening to Spotify currently.",
                    color = 0xff0000
                )
                return await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(
                    description = f"{orang.mention} not listening to Spotify currently.",
                    color = 0xff0000
                )
                return await ctx.reply(embed=embed)

        embed = discord.Embed(
            title= f"Listened by {orang.name} now",
            color= crotify.color
        )
        embed.set_author(name="Spotify", icon_url="https://user-images.githubusercontent.com/75367930/120773067-293cc680-c54b-11eb-950e-a4518c464124.png")
        embed.add_field(name="Title", value=f"[{crotify.title}](https://open.spotify.com/track/{crotify.track_id})")
        embed.add_field(name="Artist", value=crotify.artist)
        embed.add_field(name="Album", value=crotify.album)

        waktusekarang = datetime.datetime.utcnow() - crotify.start
        durasilagu = crotify.duration

        embed.set_footer(text=f"Seek: {str(waktusekarang)[:-7]} / {str(durasilagu)[:-7]}", icon_url=orang.avatar_url)
        #
        try:
            embed.set_thumbnail(url=crotify.album_cover_url)
        except:
            pass
        #
        await ctx.send(embed=embed)
    
    #KBBI
    @commands.command()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def kbbi(self, ctx, *kata):
        try:
            if not kata:
                await ctx.reply("<:robin_palato:818892964457349220> **Sintaks tidak valid!** Masukkan kata yang ingin kamu lihat di KBBI!\nContoh: `r!kbbi bantal`")
            else:
                async with ctx.typing():
                    khata = "%20".join(kata)
                    api_panas = requests.get(f"https://kbbi-api-zhirrr.vercel.app/api/kbbi?text={khata}").json()
                    katah = api_panas["lema"]
                    arti = api_panas["arti"][0]

                    tabera = discord.Embed(
                        title = katah.upper(),
                        description = arti,
                        color = ctx.guild.get_member(self.client.user.id).color
                    )
                    tabera.set_footer(text='Diberayakan oleh Badan Pengembangan dan Pembinaan Bahasa, Kemendikbud RI', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=tabera)
        except:
            kahta = " ".join(kata)
            embed = discord.Embed(
                title = f"{kahta.upper()}",
                description = "Kata tidak ditemukan...",
                color = 0xff0000
            )
            embed.set_footer(text='Diberayakan oleh Badan Pengembangan dan Pembinaan Bahasa, Kemendikbud RI', icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
            
    #Role Info
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roleinfo(self, ctx:commands.Context, *, role:discord.Role=None):
        if role is None:
            return await ctx.send("<:robin_palato:818892964457349220> **Sintaks tidak valid**! Tuliskan role yang ingin kamu lihat infonya!\nContoh: `r!roleinfo [role]`")

        embed = discord.Embed(
            title = f"Informasi Role",
            color = role.color
        )
        embed.add_field(name="Nama", value=f"{role.mention} (`{role.name}`)")
        embed.add_field(name="ID", value=role.id)
        embed.add_field(name="Warna", value=str(role.color).upper())

        if role.hoist is True:
            embed.add_field(name="Terpisah", value="✅")
        else:
            embed.add_field(name="Terpisah", value="❌")
        #
        if role.mentionable is True:
            embed.add_field(name="Bisa di-Mention", value="✅")
        else:
            embed.add_field(name="Bisa di-Mention", value="❌")
        #
        if role.managed is True:
            embed.add_field(name="Di-Manage", value="✅")
        else:
            embed.add_field(name="Di-Manage", value="❌")

        if role.is_default():
            embed.add_field(name="Role Default", value="✅")
        else:
            embed.add_field(name="Role Default", value="❌")
        #
        if role.is_premium_subscriber():
            embed.add_field(name="Role Booster", value="✅")
        else:
            embed.add_field(name="Role Booster", value="❌")
        #
        if role.is_bot_managed():
            embed.add_field(name="Diatur oleh Bot", value="✅")
        else:
            embed.add_field(name="Diatur oleh Bot", value="❌")

        embed.add_field(name="Posisi", value=role.position)
        embed.add_field(name="Dibuat pada", value=role.created_at.strftime("%d/%m/%Y %H:%M:%S UTC"))
        embed.add_field(name="Jumlah Member", value=len(role.members))

        if sum(len(izin) for izin in [perm[0] for perm in role.permissions if perm[1]]) < 1024:
            embed.add_field(name=f"Izin-Izin ({len([perm[0] for perm in role.permissions if perm[1]])})", value=f'`{", ".join([perm[0] for perm in role.permissions if perm[1]]).replace("_", " ")}`', inline=False)
        else:
            embed.add_field(name=f"Izin-Izin ({len([perm[0] for perm in role.permissions if perm[1]])})", value='Tidak muat', inline=False)

        await ctx.send(embed=embed)    
    
def setup(client):
    client.add_cog(Information(client))
