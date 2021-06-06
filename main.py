import discord
from discord.utils import find
import os
from keep_alive import keep_alive
from replit import db

token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

def updateReq(reqMsg):
  if "requirement" in db.keys():
    requirement = db["requirement"]
    requirement=(reqMsg)
    db["requirement"] = requirement
  else:
    db["requirement"] = [reqMsg]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

 
@client.event
async def on_member_join(member):
    membersID=850424690206834688
    counterChannel=client.get_channel(membersID)

    chanID=510436310088155156

    memberCounter = len([m for m in member.guild.members if not m.bot])

    await counterChannel.edit(name = 'ᴍembers: {}'.format(memberCounter))
    print('Members counted')
    
    general = client.get_channel(chanID)
    if general and general.permissions_for(member.guild.me).send_messages:
      ('Permission accepted')
      await general.send(f"Hey {member.mention}, welcome to Blessing ™ (Arcane Legends) :tada::hugging: ! Stay blessed!!\nPlease type **!b help** to see my features.")
    print('Someone joined')
        
@client.event
async def on_member_remove(member):
    membersID=850424690206834688
    counterChannel=client.get_channel(membersID)
    memberCounter = len([m for m in member.guild.members if not m.bot])
    await counterChannel.edit(name = 'ᴍembers: {}'.format(memberCounter))
    print('Someone left')

@client.event
async def embed(ctx):
    print("Embed runned")
    embed=discord.Embed(title="About Bot", 

    description="This is official Arcane Legends Blessing Guild Bot")
    embed.set_author(name="Arcane Legends Officers")

    embed.add_field(name="Members Counter", 
    value="Counts every member   when someone joins ", inline=True)

    embed.set_footer(text="version 1.0")
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!b hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!b help'):
        print("Embed runned")
        embed=discord.Embed(title="How to use Blessing bot",
        color=discord.Color.greyple())

        embed.add_field(name="To se Guild requirements\n",value="Type **!b reqinfo**", inline=False)

        embed.add_field(name="To add new Guild requirements\n", value="Type **!b req** <*requirement message*> \n Permission for this command: Masters/Developers/Officers ", inline=False)

        await message.channel.send(embed=embed)
        
    if message.content.startswith('!b botinfo'):
        print("Embed runned")
        embed=discord.Embed(title="About Bot", 

        description="This is official Arcane Legends Blessing Guild Bot", color=discord.Color.greyple())
        embed.set_author(name="Arcane Legends Officers")

        embed.add_field(name="Features (*more coming soon*)", 
        value="1. Counts every member when someone joins\n 2. Board that shows when Masters/Developers/Officers edit guild requirements ", inline=True)

        embed.set_footer(text="version 1.01")
        await message.channel.send(embed=embed)

    if message.content.startswith('!b req'):
        if message.content.startswith('!b reqinfo'):
          print("Embed runned")
          req=db["requirement"]
          embed=discord.Embed(title="About Requirements",          
          description=req, color=discord.Color.greyple())

          await message.channel.send(embed=embed)

        elif discord.utils.get(message.author.roles, name="Master") or discord.utils.get(message.author.roles, name="Officer") or discord.utils.get(message.author.roles, name="Developer"):
          print("Request change started")
          req=message.content.split("!b req ", 1)[1]
          updateReq(req)
          print("Embed runned")

          embed=discord.Embed(title="About Requirements", 
          description=req, color=discord.Color.greyple())

          await message.channel.send(embed=embed)
          await message.channel.send("@everyone New requirements just came!")

        else:
            await message.channel.send(message.author.mention +"\nI'm sorry but you dont have a permission to do this!")
     
keep_alive()
client.run(token)
