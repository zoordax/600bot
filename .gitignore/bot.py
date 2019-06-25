import discord
from discord.ext import commands
import time
import asyncio
import datetime as DT
import os




heros = ("600bot/.gitignore/heros")


client = discord.Client()

access_token = os.environ["TOKEN"]







@client.event
async def on_message(message):
    id = client.get_guild( 586332766568710155 )
    v_u = ["zoordax#7914"]
    channels = ["🐲chasse-aux-monstres", "🚧tests-bots🚧", "🧰administrateurs"]
     
   

    if str (message.channel) in channels and str(message.author) in v_u:
        if message.content.find ("$hello") != -1:
            await message.channel.send ("hi")
        elif message.content == "$users":
            await message.channel.send (f"""# of Members: {id.member_count}, at {DT.datetime.now()}""")

    if str( message.channel ) in channels and message.author.guild_permissions.administrator:
        if message.content == "!monstres":
            embed = discord.Embed( title="**Monstre**" , description="Pour utiliser le bot taper : \n **!le_monstre**", color = 0xff1c21 )
            embed.add_field( name="***>>>***Tous les monstres***<<<***" , value="\n ailedegivre \nailenoire\nbetedesneiges\nchaman\ndrider\nepinator\ngargantua\ngolem\ngriffon\nfaucheuse\nmorphalange\ntroyen\nlarve\nnoceros\nreineabeille\nsabrecroc\ntitan\nwyrm" )
            await message.channel.send( content=None , embed=embed )


    if str( message.channel ) in channels and str(message.author) in v_u:
        if message.content.find ("$loutre") != -1:
            await message.channel.send("<@415175231565463552> koya est out !!!", delete_after=15)
            await asyncio.sleep(15)
            await message.delete()
            
    if str( message.channel ) in channels and str(message.author) in v_u:
        if message.content.find ("!zoord") != -1:
            await message.channel.send("<zoor le meillor  !!!")
            await asyncio.sleep(3600)
            await message.delete()
        
        
    if str( message.channel ) in channels and str(message.author) in v_u :
       if message.content.find ("!belette") != -1:
           await message.channel.send("<@415175231565463552> !!!!! ca va ?", delete_after = 3600)
           await asyncio.sleep(3600)
           await message.delete()
          
        
    if str( message.channel ) in channels and str(message.author) in v_u :
       if message.content.find ("!depression") != -1:
           await message.channel.send("<@415175231565463552> ecoute ne fais pas de betise tu peux me parler , dis moi ce qui ne vas pas :-)", delete_after = 3600)
           await asyncio.sleep(3600)
           await message.delete()   

    if str( message.channel ) in channels :
        if message.content.find ("!golem") != -1:
            await message.channel.send(file=discord.File('heros/golem.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!wyrm") != -1:
            await message.channel.send(file=discord.File('heros/wyrm.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels:
        if message.content.find( "!titan" ) != -1:
            await message.channel.send( file=discord.File( 'heros/titan.jpg' ), delete_after = 3600) 
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!sabrecroc") != -1:
            await message.channel.send(file=discord.File('heros/sabrecroc.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!reineabeille") != -1:
            await message.channel.send(file=discord.File('heros/abeille.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!noceros") != -1:
            await message.channel.send(file=discord.File('heros/noceros.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!larve") != -1:
            await message.channel.send(file=discord.File('heros/larve.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!troyen") != -1:
            await message.channel.send(file=discord.File('heros/troyen.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()



    if str( message.channel ) in channels :
        if message.content.find ("!morphalange") != -1:
            await message.channel.send(file=discord.File('heros/morphalange.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()




    if str( message.channel ) in channels :
        if message.content.find ("!betedesneiges") != -1:
            await message.channel.send(file=discord.File('heros/Bneige.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!faucheuse") != -1:
            await message.channel.send(file=discord.File('heros/faucheuse.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!griffon") != -1:
            await message.channel.send(file=discord.File('heros/griffon.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!gargantua") != -1:
            await message.channel.send(file=discord.File('heros/gargantua.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!epinator") != -1:
            await message.channel.send(file=discord.File('heros/epinator.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!drider") != -1:
            await message.channel.send(file=discord.File('heros/drider.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!ailedegivre") != -1:
            await message.channel.send(file=discord.File('heros/givre.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!ailenoire") != -1:
            await message.channel.send(file=discord.File('heros/Anoir.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!chaman") != -1:
            await message.channel.send(file=discord.File('heros/chaman.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()
            
            

client.run(access_token)






