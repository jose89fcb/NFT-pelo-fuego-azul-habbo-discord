import discord
import os
import datetime
from discord.ext import commands
import random
from urllib import parse, request


client = commands.Bot(command_prefix= '!')


@client.command()
@commands.has_permissions(manage_messages=True)
async def Limpiar(ctx, limit: int):
    await ctx.message.delete()

    
    await ctx.channel.purge(limit=limit)
    embed = discord.Embed(title=':thumbsup: Borrado correctamente :partying_face: ', description=f'Se han borrado {limit} Mensajes. con exito! \n Comando ejecutado Por {ctx.author}.',timestamp=datetime.datetime.utcnow(), color=discord.Colour.random())
    embed.set_footer(text="Creado Por Jose89fcb")
    await ctx.channel.send(embed=embed, delete_after=5877895)


    
@client.event
async def on_ready():
    print("BOT listo!")

    

client.run('ODk2NzU2ODk0NTQxMTcyNzg2.YWLv8A.FOstGshSzyemi568PkPemfad8Fc')