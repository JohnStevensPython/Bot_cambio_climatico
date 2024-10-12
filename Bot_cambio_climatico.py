import discord
from discord.ext import commands
from model import get_class
import requests
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'hola, soy {bot.user}, diseñado parta darte informacion sobre el problema del cambio climatico y soluciones para este!, ingresa la palabra funciones para ver otros comandos!(recuerda introducir el signo dolar antes de los comandos)')

@bot.command()
async def funciones(ctx):
    functions = ["cambio_climatico: Te informara sobre que es el cambio climatico en si","causas: Te informara acerca de las causas humanas que hayan aumentado esto ","causas_imagenes: Te mostrara imagenes de las principales causas humanas del cambio climatico","consecuencias: Hara una lista de las consecuencias de este problema","Tips: te muestra consejos que puedes implementar para evitar la contaminacion","check: comprueba si el tipo de energia presente es contaminante o no contaminante, para que funcione, debes subir la imagen del tipo de energia con la palabra check."]
    # causaAleatoria = random.choice(causas)
    await ctx.send("Codigos:")
    for function in functions:
        await ctx.send(function)

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def cambio_climatico(ctx):
    await ctx.send("El cambio climatico es una variación que se está registrando en el clima del planeta, y que altera la composición de la atmósfera. Se manifiesta en un aumento de las temperaturas medias y una alteración del clima a escala mundial, haciendo más común eventos climáticos extremos")


@bot.command()
async def causas(ctx):
    causas = ["La deforestacion","la contaminacion","la produccion de gases de efecto invernadero","La generacion de energia","La agricultura","El transporte","Las industrias"]
    # causaAleatoria = random.choice(causas)
    await ctx.send("las principales causas humanas del cambio climatico desde el siglo XIX son:")
    for causa in causas:
        await ctx.send(causa)

imagenes = os.listdir("imagenes_cambio_climatico")

@bot.command()
async def causas_imagenes(ctx):
    for imagen in imagenes:
        with open(f'imagenes_cambio_climatico/{imagen}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)


@bot.command()
async def tips(ctx):
    consecuencias = ["Ahorra energia en tu casa, esto lo puedes hacer reduciendo el uso de la luz y de aparatos con enchufe","Trata de comer mas frutas y verduras","Haz el metodo de las tres R, reduce, reutiliza y recicla","Usa tipos de transporte no contaminantes como la bicicleta, sobre todo para distancias cortas","Trata de cambiar el tipo de energia quen usas en tu hogar a una mas renovable","si piesas adquirir un auto, trata de ver la posibilidad de adquirir uno electrico"]
    # causaAleatoria = random.choice(causas)
    await ctx.send("Aqui hay algunos consejos utiles para ti para combatir el cambio climatico:")
    for consecuencia in consecuencias:
        await ctx.send(consecuencia)


@bot.command()
async def consecuencias(ctx):
    consecuencias = ["Aumento de las temperaturas medias","Derretimiento de los glaciares","Aumento de inundaciones","Aumento de sequías extremas","Aumento de eventos de precipitaciones extremas","Aumento de los incendios forestales"]
    # causaAleatoria = random.choice(causas)
    await ctx.send("las principales consecuencias del cambio climnatico son:")
    for consecuencia in consecuencias:
        await ctx.send(consecuencia)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Olvidaste subir la imagen!")

        
bot.run('token')