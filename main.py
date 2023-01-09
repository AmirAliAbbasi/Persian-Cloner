from os import system
mytitle = "IRx Cloner | Coded By Pa9da ᶦᶜᵉ#0001"
system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
import random
import string
import os.path
import time
from colorama import *
from pystyle import *
os.system('cls & title ICE SPOOFER - Support : https://discord.gg/GVtVwWVEKH')
ice = """


                ██╗██████╗░██╗░░██╗  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                ██║██╔══██╗╚██╗██╔╝  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                ██║██████╔╝░╚███╔╝░  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
                ██║██╔══██╗░██╔██╗░  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
                ██║██║░░██║██╔╝╚██╗  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
                ╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝              
                
                            ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
                            ┇      [Discord] https://discord.gg/kos              ┇
                            ┇      [Github]  https://github.com/pa9da            ┇
                            ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
                                            › Press Enter...
    """
icespoofer = """

    ██╗██████╗░██╗░░██╗  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
    ██║██╔══██╗╚██╗██╔╝  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
    ██║██████╔╝░╚███╔╝░  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
    ██║██╔══██╗░██╔██╗░  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
    ██║██║░░██║██╔╝╚██╗  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
    ╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
    """

System.Size(200,40)
Anime.Fade(Center.Center(ice), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)
System.Size(100,40)
print(Fore.RED + icespoofer)
token = input(Fore.BLUE + f'Token Acc Khod Ra Vared Konid:\n >') # <-- your Account token
guild_s = input('Lotfan Id Channeli Ke Mikhayd Copy Konid Ra Vared Konid:\n >') # <-- input guild id
guild = input('Lotfan Id Channeli ke Mikhayd Clone Besharo Vared Konid:\n >') # <-- output guild id
input_guild_id = guild_s  
output_guild_id = guild  
token = token  


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


client.run(token, bot=False)
