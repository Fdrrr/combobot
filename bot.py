from cmath import inf
import random
import discord
from discord import File
import requests
import os
from download import download
from bs4 import BeautifulSoup
from colorama import Fore
from discord.colour import Colour
from discord.ext import commands , tasks
from discord import user
import aiohttp
token = "TOKEN"

bot = commands.Bot(command_prefix='?',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Ready, To Go.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')


@bot.command()
async def helpp(ctx):
    favColor=discord.colour.Color.from_rgb(36, 36, 36)
    helpEmbed = discord.Embed(title="Help Menu", color=favColor,).set_author(name="AutoCombo")
    helpEmbed.add_field(name="comb",value="Makes 5 or More Combolists For You Then Sends It To Your Dms",inline=False)
    helpEmbed.add_field(name="ping",value="Gives You The Connection Speed In MS",inline=False)
    helpEmbed.set_footer(text=f"Devolopers IQTHEGOAT#0310 - Mohammed Aly#4651")
    await ctx.send(embed=helpEmbed)



@bot.event
async def on_message(ctx):
    print(str(ctx.author)+": "+str(ctx.content))
    await bot.process_commands(ctx)

@bot.command()
async def make(ctx):
    
    ch = ctx.channel
    
    
    print(user)
    print(ch)
    if str(ch) == "combomaker":
        await ctx.send("Making Combo..")
        os.remove("HQCOMBO.txt")
        try:
            os.system("del *.txt")
        except:
                pass
        num = 10
        # making it scrape only the first 10

        # setting up the project making lists so that we can use in BEAUTIFUL SOUP
        pagenum = 1
        outlinkstemp = []
        outlinks = []
        inslinks = []
        n = 1
        newlist = []
        tempins = []
        lastdown = []
        templastdowm = []
        # starting project

        while pagenum < num:  # simple loop to scrape page source
            req = requests.get(
                f"https://sqli.cloud/t/combolists?page={pagenum}")
            src = req.text
            soup = BeautifulSoup(src, "html.parser")
            outs = soup.find_all("a")
            pagenum = pagenum+1

            for link2 in outs:  # simple loop to filter only links from the page source
                if 'href' in link2.attrs:
                    outlinkstemp.append((str(link2.attrs['href'])))

            for item in outlinkstemp:  # loop to filter only combolists
                if "dump" or "combolist" or "email:pass" or "DATABASE" or "mixed" or "combo" or "mixed" or "yahoo" or "gmail" in item:
                    outlinks.append(item)
        lenlinks = len(outlinks)

        # making the user choose how many combolists to download
        li = [10]
        num = random.choice(li)
        list1 = []
        for item in range(num):  # loop to scrape form links and show it to user
            try:
                # choosing random combolist from outlinks
                new = random.choice(outlinks)
                if new in list1:
                    new = random.choice(outlinks)
            except:
                pass
            # try and except to stop dupliactes from happening
            list1.append(new)
            n = n+1
            newlist.append(new)
        n = 1
        # appending combolist to "newlist"
        for i in newlist:  # loop to print to user the 'newlist' and scraping outer uploadee links
            rein = requests.get(i)
            miaw = i[25:len(i)]
            info = (str(n)+": "+miaw)
            await user.send(info)
            n = n+1
            src = rein.text  # taking page source
            soup = BeautifulSoup(src, "html.parser")  # soup
            ins = soup.find_all("a")  # getting all urls in site
            for link in ins:  # loop to filter only links
                if 'href' in link.attrs:
                    tempins.append((str(link.attrs['href'])))
         
        await user.send("ON IT BABY")           
        for item in tempins:
            if 'upload.ee' in item:
                    inslinks.append(item)
                    for line in inslinks:
                        req = requests.get(line)
                        src = req.text
                        soup = BeautifulSoup(src, "html.parser")
                        link = soup.find_all("a")
                    for link3 in link:
                        if 'href' in link3.attrs:
                            templastdowm.append((str(link3.attrs['href'])))
                    for i in templastdowm:  # getting direct download link
                        if "www.upload.ee/download" in i and i  not in lastdown:
                            lastdown.append(i)
                            dirPath = os.getcwd()
                            # printing path
                            # # n = 0  # declaring variable
                            # # await user.send("MAKING COMBOLIST PLEASE WAIT")
        print(lastdown)
        for url in lastdown:
            await user.send(f"DOWNLOADING FILE: {n}")
            path = download(url, f"combo{n}.txt", replace=True)
            n = n+1
        #combining
        os.system("copy /a *.txt HQCOMBO.txt")

        print("uploading")
        await user.send("UPLOADING PLEASE WAIT")
        try:
            files = {"file": open("HQCOMBO.txt", "rb")}
            async with aiohttp.ClientSession() as session:
                async with session.get('https://store1.gofile.io/uploadFile',files=files) as response:
                    print(response.text)

        except:
            print(False)
            print("done")
            await user.send("Have a Good Cracking.")
            await user.send("Check Your DMs")
bot.run(token)