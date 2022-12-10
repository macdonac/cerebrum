# bot.py
import os
import random
import discord
import openai
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')
openai.api_key = os.getenv('OPENAI_API_KEY')
#client = discord.Client(intents=discord.Intents.default())

# @client.event
# async def on_ready():
#     print(f'{client.user}\'s wrinkled brain has arrived!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Howdy {member.name}, I hope you cleaned your toes!'
#     )

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     bitch_quotes_to_respond_with = [
#         'Stop it',
#         'Sexy',
#         'Penis'

#     ]

#     if message.content == '99!':
#         response = random.choice(bitch_quotes_to_respond_with)
#         await message.channel.send(response)
    # elif '' in message.content:
    #     response = "Don't talk to me i'll murder you"
    #     await message.channel.send(response)
    # elif message.content == 'raise-exception':
    #     raise discord.DiscordException


@bot.command(name='bitch')
async def bitch(ctx):
    await ctx.send('I will eat your first-born')


@bot.command(name='?')
async def ask_chatGPT(ctx):
    #openai.Model.list()
    prompt = ctx.message.content
    prompt = prompt.replace('!?', '')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
)

    await ctx.send(response.choices[0]['text'] or "You done fucked me up boi, ask another question.")
#client.run(TOKEN)
bot.run(TOKEN)
