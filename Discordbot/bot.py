#Discord bot :D

import discord
import requests
import json
import random

greetings = (
"Hi there! My name is HappyBot!\n"
"Thank you for inviting me into your server ଘ(੭*ˊᵕˋ)੭* ੈ♡‧₊˚ \n"
"I have 2 commands that can make you feel better and interact with others! **\"!hug\"** for hugging virtually with others and **\"!wholesome\"** for wholesomememes.\n"
"I also have one more command. **\"!codingmeme\"** for some funny coding memes that you and other can relate and understand!\n"
"Anyways have fun and enjoy  ପ(๑•ᴗ•๑)ଓ ♡"
)




hug_text_art = [
  "( っ˶´ ˘ `)っ*hug*",
  "(づ๑•ᴗ•๑)づ♡*hug*",
  "(つ≧▽≦)つ*hug*",
  "(っᵔ◡ᵔ)っ(˶ᵔ ᵕ ᵔ˶)*hug*",
  "♡⸜(ˆᗜˆ˵ )⸝♡*hug*",
  "(づ｡•ᴗ•｡)づ♡♡♡*hug*",
  "ʕっ• ᴥ • ʔっ*hug*",
  "(づ｡◕‿‿◕｡)づ*hug*",
  " ʕっ•ᴥ•ʔっ*hug*",
  "(⁠つ´▽`)⁠つ *hug*"
]



def subreddit(memes):
  response = requests.get(f'https://meme-api.com/gimme/{memes}')
  json_data = json.loads(response.text)
  return json_data["url"]

class MyClient(discord.Client):
  async def on_ready(self):
    print(f"Logged on as {self.user}")
  
  async def on_guild_join(self, guild):
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        await channel.send(greetings)
        break

  async def on_message(self, message):
    if message.author == self.user:
      return
    
    if message.content.startswith('!wholesome'):
      await message.channel.send(subreddit("wholesomememes"))

    elif message.content.startswith("!hug"):
      hug_text = random.choice(hug_text_art)
      await message.channel.send(hug_text)
    
    elif message.content.startswith("!codingmeme"):
      await message.channel.send(subreddit("codingmemes"))




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("MTI2NTM3NzQ5NDA3MzA4NTk4Mw.GLg8Wq.rl_DGQ4eFAjANeAp__FXaA24_ESydBF10q2WA4")