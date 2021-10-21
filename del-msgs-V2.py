import discord
import asyncio
import shutil
import datetime
from discord.ext import commands
from colorama import init, Fore
import os
import sys

client = discord.Client()
token = input(f"{Fore.LIGHTRED_EX}[{Fore.RESET}{Fore.LIGHTGREEN_EX}${Fore.RESET}{Fore.LIGHTRED_EX}]{Fore.RESET}{Fore.LIGHTGREEN_EX}Token: ")


os.system('clear')
print("\n")



def logo():
    try:
        msg = f"""
.d8888. d88888b  .o88b.  .d88b.  d8b   db d8888b. 
88'  YP 88'     d8P  Y8 .8P  Y8. 888o  88 88  `8D 
`8bo.   88ooooo 8P      88    88 88V8o 88 88   88 
  `Y8b. 88~~~~~ 8b      88    88 88 V8o88 88   88 
db   8D 88.     Y8b  d8 `8b  d8' 88  V888 88  .8D 
`8888Y' Y88888P  `Y88P'  `Y88P'  VP   V8P Y8888D
"""
        for l in msg:
            print(l, end="")
    except KeyboardInterrupt:

        sys.exit()
logo()




print(Fore.RED + '\n\n[-] ---------------------------------------- [-] Second Software Enginer [-] ---------------------------------------- [-]'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(''.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(Fore.GREEN + '                             [1] .c : (Digite ".c" para Deletar mensagens dos servidores e da sua dm com uma pessoa)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(Fore.GREEN + '                             [2] .dm : (Digite ".dm" para Deletar todas mensagens de todas as suas conversas da sua dm)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(''.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)) 
print(Fore.RED + '[-] ---------------------------------------- [-] Second Software Enginer [-] ---------------------------------------- [-]'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('  ')




@client.event
async def on_ready():
    width = shutil.get_terminal_size().columns
    def ui():
        print()
        print(Fore.WHITE + "Developer/Second'44 爱#0044".center(width))
        print()
        print(Fore.YELLOW +  "[-] PERFIL LOGADO - [-] SISTEMA DELETTE MESSAGES [-] : {0} [-]".format(client.user).center(width))
        print()
        print(Fore.WHITE +  "[-] Powered By Second 44 [-]\n".center(width))
        print(f"{Fore.LIGHTGREEN_EX}[{Fore.RESET}{Fore.LIGHTRED_EX}-{Fore.RESET}{Fore.LIGHTGREEN_EX}]{Fore.RESET}{Fore.LIGHTCYAN_EX} Acc Logada: {Fore.RESET}{Fore.MAGENTA}{client.user}{Fore.RESET}")
        print(f"{Fore.LIGHTGREEN_EX}[{Fore.RESET}{Fore.LIGHTRED_EX}-{Fore.RESET}{Fore.LIGHTGREEN_EX}]{Fore.RESET}{Fore.LIGHTCYAN_EX} UID: {Fore.RESET}{Fore.MAGENTA}{client.user.id}{Fore.RESET}\n")
    ui()
    
    
    

@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel
        if commands[0] == '.c':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                    await asyncio.sleep(1)
                                    print(f"{Fore.CYAN}{msg}\n")
                                except Exception as x:
                                    pass
                                    
                                    if commands[0] == '.dm':
                                    	for channel in client.private_channels:
                                    		if isinstance(channel, discord.DMChannel):
                                    			async for msg in channel.history(limit=9999):
                                    				try:
                                    					
                                    					if msg.author == client.user:
                                    						await msg.delete()
                                    						asyncio.sleep(1)
                                    						print(msg)
                                    				except:
                                    							pass
                                    							
client.run(token, bot=False)