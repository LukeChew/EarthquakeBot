import discord
from discord.ext import commands
import urllib.request 
import json

client = commands.Bot(command_prefix = 'quake.')

serverlink = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
url = urllib.request.urlopen(serverlink)
data = url.read().decode("utf-8")
quakes = json.loads(data)

async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print ("EarthquakeBot is ready", url.getcode())

@client.command()
async def ping(ctx):
    await ctx.send(client.latency * 1000)

@client.command()
async def places(ctx):
    text="Locations of earthquakes with magnitude 2.5 or greater in the past day:\n"
    for i in quakes["features"]:
        text+=(i["properties"]["place"] + "\n")
    await ctx.send(text)

@client.command()
async def mag(ctx):
    text="Magnitude and locations of earthquakes with magnitude 2.5 or greater in the past day:\n"
    for i in quakes["features"]:
        text+=(str(i["properties"]["mag"])+" magnitude " + i["properties"]["place"] + "\n")
    await ctx.send(text)













