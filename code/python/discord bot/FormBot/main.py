import disnake
from disnake import Webhook
import aiohttp
import os
import datetime
import json
from disnake.ext import commands
import mysql.connector  
from datetime import timedelta
import re
import pytz








loading_dict = {}


try:
  with open('token.json') as v:
    token = json.load(v)
    v.close()

except Exception as e:
  print('Невозможно открыть токен, ошибка: ' + e)
  with open('token.json', 'w+') as v:
      v.write('{}')
      v.close()
  with open('token.json') as v:
    token = json.load(v)
    v.close()

try:

  with open('archive.json') as v:
    archive = json.load(v)
    v.close()
except Exception as e:
  print(f'Error in archive open: {e}')
  with open('archive.json', 'w+') as v:
      v.write('{}')
      v.close()
  with open('archive.json') as v:
    archive = json.load(v)
    v.close()

try:  
  with open('config.json', encoding="utf-8") as f:
      
      config = json.load(f)
      premissions_list = list(config['premissions'].values())
      f.close()

except Exception as e:
   print(f'Error in config: {e}')
   
      

   
aclient = commands.Bot(command_prefix=commands.when_mentioned_or('.'), intents=disnake.Intents().all())



@aclient.event
async def on_ready():
      info_embed = disnake.Embed(
        colour=disnake.Colour.gold(),
        title=f'"Подача заявок в персонал или на доверенного игрока"',
        description=config['embed_select_menu']
      )


      channel = aclient.get_channel(config['form_channel']['form_channel'])
      msg_id = config['select_id']
      msg = await channel.fetch_message(msg_id)
      await msg.edit(content="", embed=info_embed, view=DepartamentView())
      aclient.add_view(ButtonView())
      for i in archive:
          if archive[i]['accepted'] == False:
            aclient.add_view(ButtonView(), message_id=archive[i]['embed_message_id'])
      print('Good')



class DiscordModal(disnake.ui.Modal):
    def __init__(self):
        super().__init__(
            title=f'Анкета на дискорд сотрудника', 
            components=[
              disnake.ui.TextInput(
                custom_id='gmail',
                style=disnake.TextInputStyle.short,
                label='Почта гугл',
                required=True,
                placeholder='Потребуется для выдачи доступов к закрытым документам.'
              ), 
              
              disnake.ui.TextInput(
                custom_id='date_time',
                style=disnake.TextInputStyle.short,
                label='Дата и время вам удобно пройти собеседование',
                required=True,
              ), 

              disnake.ui.TextInput(
                custom_id='age',
                style=disnake.TextInputStyle.short,
                label='Ваш возраст',
                required=True,
              ),

              disnake.ui.TextInput(
                custom_id='expirince',
                style=disnake.TextInputStyle.paragraph,
                label='Есть ли у вас опыт в данном направлении??',
                required=True,
                placeholder='Обязательно укажите подробности'
              ),

              disnake.ui.TextInput(
                custom_id='comments',
                style=disnake.TextInputStyle.paragraph,
                label='Ваши комментарии, пожелания,дополнения',
                required=False
              )
            ]
          )

    async def callback(self, interaction: disnake.Interaction):
      
      time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
      time_now = time.strftime('%d/%m/%Y %H:%M:%S')



      disnake_departament = config['abbreviation'][loading_dict[str(interaction.user.id) + '_discord']]
      selected_server = loading_dict[str(interaction.user.id) + '_discord']
      embed = disnake.Embed(
        colour=disnake.Colour.dark_blue(),
        title=f'Пришла новая заявка на {disnake_departament}',
        description=f'#ds_{selected_server}'
      )
      embed.set_author(name=f'{interaction.user.display_name} | {interaction.user}', icon_url=interaction.user.avatar)
      embed.set_thumbnail(url=interaction.user.avatar)
      embed.add_field(name='DiscordID:', value=interaction.user.id, inline = True) 
      embed.add_field(name='Кандидат:', value=interaction.user.mention, ) 
      
      embed.add_field(name='Почта:', value=interaction.text_values['gmail'], )
      embed.add_field(name='Опыт:', value=interaction.text_values['expirince'] )
      embed.add_field(name='Возраст:', value=interaction.text_values['age'] )
      embed.add_field(name='Время когда удобно пройти собеседование:', value=interaction.text_values['date_time'], inline = False )
      embed.add_field(name='Комментарии:', value=interaction.text_values['comments'] )
      embed.color = 0xFFFF00


      try:
        
        user = await aclient.fetch_user(interaction.user.id)
          
        await user.send('Ответы приняты на ' +  str(config['abbreviation'][loading_dict[str(interaction.user.id) + '_discord']] + '\n*Срок рассмотрения - до 7 дней*'))
        await interaction.response.send_message('Проверьте личные сообщения', ephemeral=True)
        
      except Exception as e:
        await interaction.response.send_message('**Для подачи заявки откройте личные сообщения от бота!**\nДля этого:\n- Нажмите правой кнопкой мыши по серверу\n- Настройки конфиденциальности\n- Личные сообщения\nПосле попробуйте ещё раз.', ephemeral=True)
        print(f'Discord modal error: {e}')
        async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'Discord modal error: {e}', username='Logs') 
        return

      
      channel = aclient.get_channel(config['form_channel'][selected_server])
      
      
      vice_king = config['roles_id']['discord'][selected_server]['vice_king']
      embed_message = await channel.send(f'{vice_king}',embed=embed, view=ButtonView())

      date_until = datetime.datetime.now(pytz.timezone('Europe/Moscow')) + datetime.timedelta(days = config['cooldown_form'])
      with open('archive.json', 'w') as v:
          archive.update({f'{str(interaction.user.id)}_{selected_server}_discord' : {'server': selected_server, 'departament': 'discord', 'date_until': str(date_until.strftime('%d/%m/%y %H:%M:%S')), 'accepted': False, 'embed_message_id': embed_message.id}})
          json.dump(archive, v, indent=4 )
        
      
      
      
      try:
        del loading_dict[str(interaction.user.id) + '_discord']
        del loading_dict[str(interaction.user.id) + '_main']
        del loading_dict[str(interaction.user.id) + '_server']
            
           
      except Exception as e:
        print(e)
        async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'{e}', username='Logs') 

      print(f'{interaction.user} : + {interaction.user.id} отправил заявку в дискорд отдел на {selected_server} в {time_now}')
      
      


class SkutumModal(disnake.ui.Modal):
    
    def __init__(self):
        super().__init__(
            title='Анкета на доверенного игрока', 
            components=[
              disnake.ui.TextInput(
                custom_id='steamid',
                style=disnake.TextInputStyle.short,
                label='Ваш SteamID64 ',
                required=True,               
                placeholder='76561198259182867 (это пример)' 
              ), 
              
              disnake.ui.TextInput(
                custom_id='warns_question',
                style=disnake.TextInputStyle.short,
                label='Были ли у вас нарушения на сервере? Какие?',
                required=True,
              ), 

              disnake.ui.TextInput(
                custom_id='age',
                style=disnake.TextInputStyle.short,
                label='Ваш возраст',
                required=True,
              ), 

              disnake.ui.TextInput(
                custom_id='about_job',
                style=disnake.TextInputStyle.paragraph,
                label='Что должен делать доверенный игрок?',
                required=True,
                placeholder='Расскажите своё мнение, основываясь на игровом опыте.'
              ), 

              disnake.ui.TextInput(
                custom_id='comments',
                style=disnake.TextInputStyle.paragraph,
                label='Дополнительная информация, пожелания',
                required=False
              )
            ]
        )

    async def callback(self, interaction: disnake.Interaction):
      
      time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
      time_now = time.strftime('%d/%m/%Y %H:%M:%S')
          
      self.steamid = str(interaction.text_values['steamid'])
      self.steamid = self.steamid.strip(' ')  
      if re.search('^7656119([0-9]{10})$' , self.steamid): 
        

        db_connection = mysql.connector.connect(
          host=config['db_data']['host'],
          user=config['db_data']['user'],
          password=config['db_data']['password'],
          database=f"scpsl{config['ports'][loading_dict[str(interaction.user.id) + '_server']]}"
        )

        mycursor = db_connection.cursor()

        """Варны"""
        mycursor.execute(f"SELECT reason FROM Warns WHERE TargetID = {self.steamid}") 
        warn_lists = []
        for i in mycursor:
          
          warn_lists.append('▶ '+ i[0])
        len_warns = len(warn_lists)
        warns = (' \n '.join(warn_lists))
        
        """Баны"""
        mycursor.execute(f"SELECT reason FROM Bans WHERE TargetID = {self.steamid}") 
        ban_lists = []
        for i in mycursor:
          
          ban_lists.append('▶ '+ i[0])
        
        len_bans = len(ban_lists)
        bans = (' \n '.join(ban_lists))

        """Муты"""
        mycursor.execute(f"SELECT reason FROM Mutes WHERE TargetID = {self.steamid}") 
        mute_lists = []
        for i in mycursor:
          
          mute_lists.append('▶ '+ i[0])
        len_mutes = len(mute_lists)
        mutes = (' \n '.join(mute_lists))

        """Время"""
        mycursor.execute(f"SELECT PlayTime FROM Stats WHERE PlayerID = {self.steamid}") 

        time_list = []
        for i in mycursor:
          for x in i:
            stats_dict = json.loads(x)
      


        """Ник игрокa"""
        
        mycursor.execute(f"SELECT Nickname FROM Players WHERE ID = {self.steamid}") 

        for i in mycursor:
           nickname = i
        
        full_time = 0
        for i in stats_dict:
          
          index = i.index('T')
          data = i[:index]
          full_time += stats_dict[i]
          td = timedelta(seconds=stats_dict[i])
          play_day = f'{data} наиграно: {td}'
          time_list.append(play_day)
          
        full_time = timedelta(seconds=full_time)


        days_full_time = 0
        stats_last_days = []
        days = 0
        while days != 14:
          stats_about_day = (datetime.datetime.today() - datetime.timedelta(days=days)).strftime('%Y-%m-%d')
    


    
          for i in time_list:
            
            if stats_about_day in i:
              seconds_from_dict = stats_about_day + 'T00:00:00+03:00'
              days_full_time += stats_dict[seconds_from_dict]
              
              stats_last_days.append(i)
              break

          
        
          days += 1
        days_full_time = timedelta(seconds=days_full_time)
        stats_last_days.insert(0, f'Общий за последние 14 дней: {days_full_time}')
        stats = (' \n '.join(stats_last_days))
        

        
        selected_server = loading_dict[str(interaction.user.id) + '_server']
        embed = disnake.Embed(
          colour=disnake.Colour.dark_blue(),
          title='Пришла новая заявка на доверенного игрока!',
          description=f'#sk_{selected_server}'
        )
        embed.set_author(name=f'{interaction.user.display_name} | {interaction.user}', icon_url=interaction.user.avatar)
        embed.set_thumbnail(url=interaction.user.avatar)
        embed.add_field(name='DiscordID:', value=interaction.user.id, inline = False) 
        embed.add_field(name='Кандидат:', value=interaction.user.mention, inline = False) 
        embed.add_field(name='Ник на сервере:', value=nickname[0], inline = False)
        embed.add_field(name='SteamID 64:', value=f'{self.steamid}', inline = False)
        embed.add_field(name='Нарушения на сервере:', value=interaction.text_values['warns_question'], inline = False )
        embed.add_field(name='Возраст:', value=interaction.text_values['age'], inline = False )
        embed.add_field(name='Представление о доверенных игроках:', value=interaction.text_values['about_job'], inline = False )
        embed.add_field(name='Дополнительная информация, пожелания', value=interaction.text_values['comments'], inline = False )
        embed.add_field(name=f'Варнов: {len_warns}', value=warns, inline=False )
        embed.add_field(name=f'Банов: {len_bans}', value=bans, inline=False )
        embed.add_field(name=f'Мутов: {len_mutes}', value=mutes, inline=False )
        embed.add_field(name='Общий онлайн:', value=full_time, inline=False )
        embed.add_field(name=f'Последние 14 дней:', value=stats, inline=False )
        embed.color = 0xFFFF00
        
        
        try:
        
          user = await aclient.fetch_user(interaction.user.id)
          
          await user.send('Ответы приняты на ' +  str(config['abbreviation'][loading_dict[str(interaction.user.id) + '_server']] + '\n*Срок рассмотрения - до 7 дней*'))
          await interaction.response.send_message('Проверьте личные сообщения', ephemeral=True)
        
        except Exception as e:
          await interaction.response.send_message('**Для подачи заявки откройте личные сообщения от бота!**\nДля этого:\n- Нажмите правой кнопкой мыши по серверу\n- Настройки конфиденциальности\n- Личные сообщения\nПосле попробуйте ещё раз.', ephemeral=True)
          async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config['logs_chat'], session=session)
         
            await webhook.send(f'{e}', username='Logs')  
          return

        selected_server = loading_dict[str(interaction.user.id) + '_server']
        channel = aclient.get_channel(config['form_channel'][f'scutum_{selected_server}'])
        
        
        vice_king = config['roles_id'][selected_server]['vice_king']
        embed_message = await channel.send(content='',embed=embed, view=ButtonView())
        date_until = datetime.datetime.now(pytz.timezone('Europe/Moscow')) + datetime.timedelta(days = config['cooldown_form'])
        with open('archive.json', 'w') as v:
          print(f'{archive} в {time_now}')
          archive.update({f'{str(interaction.user.id)}_{selected_server}_skutum' : {'server': selected_server, 'departament': 'skutum', 'date_until': str(date_until.strftime('%d/%m/%y %H:%M:%S')), 'accepted': False, 'embed_message_id': embed_message.id}})
          json.dump(archive, v, indent=4 )

        channel = aclient.get_channel(config['form_channel'][loading_dict[str(interaction.user.id) + '_server']])
        

        print(f'{interaction.user} : + {interaction.user.id} отправил заявку на доверенных игроков {selected_server} в {time_now}')
        try:
           del loading_dict[str(interaction.user.id) + '_discord']
           del loading_dict[str(interaction.user.id) + '_main']
           del loading_dict[str(interaction.user.id) + '_server']
            
           
        except Exception as e:
          print(e)
          async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config['logs_chat'], session=session)
            
            await webhook.send(f'{e}', username='Logs') 
            await webhook.send(f'{archive}', username='Logs') 
        

      else: 
         await interaction.response.send_message('Неправильный SteamID', ephemeral=True)

class GameModal(disnake.ui.Modal):
    def __init__(self):
        super().__init__(
            title='Анкета на Мл. Модератора', 
            components=[
              disnake.ui.TextInput(
                custom_id='steamid',
                style=disnake.TextInputStyle.short,
                label='Ваш SteamID64 ',
                required=True,               
                placeholder='76561198259182867 (это пример)' 
              ), 
              
              disnake.ui.TextInput(
                custom_id='date_time',
                style=disnake.TextInputStyle.short,
                label='Когда вам угодно пройти собеседование?',
                required=True,
              ), 

              disnake.ui.TextInput(
                custom_id='age',
                style=disnake.TextInputStyle.short,
                label='Ваш возраст',
                required=True,
              ), 

              disnake.ui.TextInput(
                custom_id='expirince',
                style=disnake.TextInputStyle.paragraph,
                label='Интервью, часть 1',
                required=True,
                placeholder='Как давно вы играете на наших серверах, какие плюсы и какие проблемы могли бы выделить?.'
              ), 

              disnake.ui.TextInput(
                custom_id='comments',
                style=disnake.TextInputStyle.paragraph,
                label='Интервью, часть 2',
                required=False,
                placeholder='Чем занимается админ FLX и как долго вы собираетесь им быть?'
              )
            ]
        )

    
    async def callback(self, interaction: disnake.Interaction):
      self.steamid = str(interaction.text_values['steamid'])
      self.steamid = self.steamid.strip(' ')
      time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
      time_now = time.strftime('%d/%m/%Y %H:%M:%S')
      if re.search('^7656119([0-9]{10})$' , self.steamid): 
        

        db_connection = mysql.connector.connect(
          host=config['db_data']['host'],
          user=config['db_data']['user'],
          password=config['db_data']['password'],
          database=f"scpsl{config['ports'][loading_dict[str(interaction.user.id) + '_server']]}"
        )

        mycursor = db_connection.cursor()

        """Варны"""
        mycursor.execute(f"SELECT reason FROM Warns WHERE TargetID = {self.steamid}") 
        warn_lists = []
        for i in mycursor:
          
          warn_lists.append('▶ ' + i[0])
        len_warns = len(warn_lists)
        warns = (' \n'.join(warn_lists))
        
        """Баны"""
        mycursor.execute(f"SELECT reason FROM Bans WHERE TargetID = {self.steamid}") 
        ban_lists = []
        for i in mycursor:
          
          ban_lists.append('▶ ' + i[0])
        
        len_bans = len(ban_lists)
        bans = (' \n'.join(ban_lists))

        """Муты"""
        mycursor.execute(f"SELECT reason FROM Mutes WHERE TargetID = {self.steamid}") 
        mute_lists = []
        for i in mycursor:
          
          mute_lists.append('▶ ' + i[0])
        len_mutes = len(mute_lists)
        mutes = (' \n'.join(mute_lists))

        """Время"""
        mycursor.execute(f"SELECT PlayTime FROM Stats WHERE PlayerID = {self.steamid}") 

        time_list = []
        
        for i in mycursor:
          for x in i:
            stats_dict = json.loads(x)

        """Ник игрокa"""
        
        mycursor.execute(f"SELECT Nickname FROM Players WHERE ID = {self.steamid}") 

        for i in mycursor:
           nickname = i

        try:
          full_time = 0
          for i in stats_dict:
          
            index = i.index('T')
            data = i[:index]
            full_time += stats_dict[i]
            td = timedelta(seconds=stats_dict[i])
            play_day = f'{data} наиграно: {td}'
            time_list.append(play_day)
        except:
          await interaction.response.send_message('Ошибка, данного игрока нет в базе данных', ephemeral=True)    
        full_time = timedelta(seconds=full_time)


        days_full_time = 0
        stats_last_days = []
        days = 0
        while days != 14:
          stats_about_day = (datetime.datetime.today() - datetime.timedelta(days=days)).strftime('%Y-%m-%d')
    


    
          for i in time_list:
            
            if stats_about_day in i:
              seconds_from_dict = stats_about_day + 'T00:00:00+03:00'
              days_full_time += stats_dict[seconds_from_dict]
              
              stats_last_days.append(i)
              break

          
        
          days += 1
        days_full_time = timedelta(seconds=days_full_time)
        stats_last_days.insert(0, f'Общий за последние 14 дней: {days_full_time}')
        stats = (' \n '.join(stats_last_days))
    
        


        selected_server = loading_dict[str(interaction.user.id) + '_server']
        embed_game = disnake.Embed(
          colour=disnake.Colour.dark_blue(),
          title='Пришла новая заявка на Мл. Модератор',
          description=f'#gm_{selected_server}'
        )
        embed_game.set_author(name=f'{interaction.user.display_name} | {interaction.user}', icon_url=interaction.user.avatar)
        embed_game.set_thumbnail(url=interaction.user.avatar)
        embed_game.add_field(name='DiscordID:', value=interaction.user.id, inline = False) 
        embed_game.add_field(name='Кандидат:', value=interaction.user.mention, inline = False) 
        embed_game.add_field(name='Ник на сервере:', value=nickname[0])
        embed_game.add_field(name='SteamID 64:', value=interaction.text_values['steamid'], inline = False)
        embed_game.add_field(name='Как давно играет, плюсы и минусы:', value=interaction.text_values['expirince'], inline = False )
        embed_game.add_field(name='Возраст:', value=interaction.text_values['age'], inline = False )
        embed_game.add_field(name='Время когда удобно пройти собеседование:', value=interaction.text_values['date_time'], inline = False )
        embed_game.add_field(name='Чем заниматься админ и как долго собирается быть:', value=interaction.text_values['comments'] )
        embed_game.add_field(name=f'Варнов: {len_warns}', value=warns, inline = False )
        embed_game.add_field(name=f'Банов: {len_bans}', value=bans, inline = False )
        embed_game.add_field(name=f'Мутов: {len_mutes}', value=mutes, inline = False )
        embed_game.add_field(name='Общий онлайн:', value=full_time, inline = False )
        embed_game.add_field(name=f'Последние 14 дней:', value=stats, inline = False )
        embed_game.color = 0xFFFF00
        

        
        channel = aclient.get_channel(config['form_channel'][loading_dict[str(interaction.user.id) + '_server']])
        try:
        
          user = await aclient.fetch_user(interaction.user.id)
          
          await user.send('Ответы приняты на ' +  str(config['abbreviation'][loading_dict[str(interaction.user.id) + '_server']] + '\n*Срок рассмотрения - до 7 дней*'))
          await interaction.response.send_message('Проверьте личные сообщения', ephemeral=True)
        
        except Exception as e:
          await interaction.response.send_message('**Для подачи заявки откройте личные сообщения от бота!**\nДля этого:\n- Нажмите правой кнопкой мыши по серверу\n- Настройки конфиденциальности\n- Личные сообщения\nПосле попробуйте ещё раз.', ephemeral=True)
          print(e)
          async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config['logs_chat'], session=session)
         
            await webhook.send(f'{e}', username='Logs')  
          return
        
        
        vice_king = config['roles_id'][selected_server]['vice_king']
        
        embed_message = await channel.send(f'{vice_king}' ,embed=embed_game, view=ButtonView())
        
        

        print(f'{interaction.user} : + {interaction.user.id} отправил заявку на {selected_server} в {time_now}')

        date_until = datetime.datetime.now(pytz.timezone('Europe/Moscow')) + datetime.timedelta(days = config['cooldown_form'])
        with open('archive.json', 'w') as v:
          archive.update({f'{str(interaction.user.id)}_{selected_server}_game' : {'server': selected_server, 'departament': 'game', 'date_until': str(date_until.strftime('%d/%m/%y %H:%M:%S')), 'accepted': False, 'embed_message_id': embed_message.id}})
          json.dump(archive, v, indent=4 )
        try:
           del loading_dict[str(interaction.user.id) + '_discord']
           del loading_dict[str(interaction.user.id) + '_main']
           del loading_dict[str(interaction.user.id) + '_server']
            
           
        except Exception as e:
          print(e)
          async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config['logs_chat'], session=session)
         
            await webhook.send(f'{e}', username='Logs') 
      else:
         await interaction.response.send_message('Неправильный SteamID', ephemeral=True)
      


class GameSelect(disnake.ui.Select):

  
  
    def __init__(self):
      
      
      options = [
        disnake.SelectOption(label='Chaotic⚧️', value='ch'),
        disnake.SelectOption(label='Minigames🎮', value='mg'),
        disnake.SelectOption(label='FunRP🎴', value='fnrp'),
        disnake.SelectOption(label='LightRP💡', value='lrp'),
        disnake.SelectOption(label='MediumRP🔞', value='mrp'),
        disnake.SelectOption(label='HardRP🌑', value='hrp')
      ]
      super().__init__(
          options=options,
          placeholder='Выберите сервер', min_values=1, max_values=1
      )
    

  
    
    async def callback(self, interaction: disnake.Interaction):
        
        selected_server = self.values[0]
        selected_main = loading_dict[str(interaction.user.id) + '_main']
        loading_dict[str(interaction.user.id) + '_server'] = selected_server
        with open('config.json', encoding="utf-8") as f:
          config = json.load(f)

        with open('archive.json', encoding="utf-8") as v:
          archive = json.load(v)

        try:
          if archive[f'{str(interaction.user.id)}_{selected_server}_{selected_main}']['server'] == loading_dict[str(interaction.user.id) + '_server']:
            if archive[f'{str(interaction.user.id)}_{selected_server}_{selected_main}']['departament'] == loading_dict[str(interaction.user.id) + '_main']:
                str_datetime = archive[f'{str(interaction.user.id)}_{selected_server}_{selected_main}']['date_until']
                time_from_end = datetime.datetime.strptime(str_datetime, '%d/%m/%y %H:%M:%S').date()
                time_form_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).date()
                if archive[f'{str(interaction.user.id)}_{selected_server}_{selected_main}']['accepted'] == False:
                  await interaction.response.send_message('Ваша заявка еще не была рассмотрена, попробуйте позже', ephemeral=True)
                  return


                if time_from_end < time_form_now:
                  
                  with open('archive.json', 'w') as f:
                    del archive[f'{str(interaction.user.id)}_{selected_server}_{selected_main}']
                    json.dump(archive, f, indent=4)
                if time_from_end > time_form_now:  
                    await interaction.response.send_message(f'Вы __НЕ__ можете подать заявку до: {time_from_end}, попробуйте позже', ephemeral=True)
                    return
                    
        except Exception as e:
          print(e)
          async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(config['logs_chat'], session=session)
         
            await webhook.send(f'{e}', username='Logs')  
        time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        time_now = time.strftime('%d/%m/%Y %H:%M:%S')
        
        blacklist_detector = False
        blacklist_skutum_detector = False
        blacklist = config['blacklist']
        blacklist_skutum = config['blacklist_skutum']
        for i in blacklist:
           if interaction.user.get_role(i) != None:
              blacklist_detector = True

        for i in blacklist_skutum:
           if interaction.user.get_role(i) != None:
              blacklist_skutum_detector = True

        if blacklist_detector == True and loading_dict[str(interaction.user.id) + '_main'] != 'skutum':
            await interaction.response.send_message('Вы не прошли верификацию дискорда или имеете роли, запрещающие попадание в состав проекта', ephemeral=True )
            return

        if blacklist_skutum_detector == True and loading_dict[str(interaction.user.id) + '_main'] == 'skutum':
           await interaction.response.send_message('Вы не прошли верификацию дискорда или имеете роли, запрещающие попадание в состав проекта', ephemeral=True )
           return
        
        if loading_dict[str(interaction.user.id) + '_main'] == 'skutum':
            loading_dict[str(interaction.user.id) + '_server'] = selected_server
            servak_sk = loading_dict[str(interaction.user.id) + '_server']
            
            if config['servers'][f's{servak_sk}'] == True:
                await interaction.response.send_modal(SkutumModal())
                print(f'{interaction.user} : + {interaction.user.id} выбрал открытый доверенный игрок отдел {selected_server} в {time_now}')
            if config['servers'][f's{servak_sk}'] == False:
                await interaction.response.send_message('В данный момент заявки на доверенных игроков данного сервера закрыты, ожидайте новостей', ephemeral=True )
                print(f'{interaction.user} : + {interaction.user.id} выбрал закрытый скуутум отдел {selected_server} в {time_now}')

        else:
          loading_dict[str(interaction.user.id)+ '_server'] = selected_server
          servak_gm = loading_dict[str(interaction.user.id) + '_server']
          
          try:
            if config['servers'][servak_gm] == False:
                await interaction.response.send_message('В данный момент заявки в модерацию данного сервера закрыты, ожидайте следющего набора', ephemeral=True )
                print(f'{interaction.user} : + {interaction.user.id} выбрал закрытый модераторский отдел {selected_server} в {time_now}')
            elif config['servers'][servak_gm] == True:
                await interaction.response.send_modal(GameModal())
                print(f'{interaction.user} : + {interaction.user.id} выбрал открытый модераторский отдел {selected_server} в {time_now}')
          except Exception as e:   
            print(e)
            async with aiohttp.ClientSession() as session:
              webhook = Webhook.from_url(config['logs_chat'], session=session)
         
              await webhook.send(f'{e}', username='Logs')  
            await interaction.response.send_message('Произошла ошибка, обратитесь в поддержку дискорд отдела', ephemeral=True )
        


class DiscordSelect(disnake.ui.Select):

  
  
    def __init__(self):
      options = [
        disnake.SelectOption(label='Анкета на кодера', value='cdr'),
        disnake.SelectOption(label='Анкета на ивентмастера', value='ivms'),
        disnake.SelectOption(label='Анкета на декоратора', value='dkr')
      ]
      
      super().__init__(
          options=options,
          placeholder='Выберите направление', min_values=1, max_values=1
      )
    

   
    async def callback(self, interaction: disnake.Interaction):
        
          with open('archive.json', encoding="utf-8") as v:
            archive = json.load(v)

          selected_disnake = self.values[0]
          loading_dict[str(interaction.user.id) + '_discord'] = selected_disnake
          selected_dis_job = loading_dict[str(interaction.user.id) + '_discord']
          selected_main = loading_dict[str(interaction.user.id) + '_main']
          try:
            if archive[f'{str(interaction.user.id)}_{selected_dis_job}_discord']['server'] == loading_dict[str(interaction.user.id) + '_discord']:
              
              if archive[f'{str(interaction.user.id)}_{selected_dis_job}_discord']['departament'] == loading_dict[str(interaction.user.id) + '_main']:
                  
                  str_datetime = archive[f'{str(interaction.user.id)}_{selected_dis_job}_discord']['date_until']
                  time_from_end = datetime.datetime.strptime(str_datetime, '%d/%m/%y %H:%M:%S').date()
                  time_form_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).date()
                  if archive[f'{str(interaction.user.id)}_{selected_dis_job}_{selected_main}']['accepted'] == False:
                    await interaction.response.send_message('Ваша заявка еще не была рассмотрена, попробуйте позже', ephemeral=True)
                    return
            
                  if time_from_end < time_form_now:
                    
                    with open('archive.json', 'w') as f:
                      del archive[f'{str(interaction.user.id)}_{selected_dis_job}_discord']
                      json.dump(archive, f, indent=4)
                  if time_from_end > time_form_now:  
                      await interaction.response.send_message(f'Вы __НЕ__ можете подать заявку до: {time_from_end}, попробуйте позже', ephemeral=True)
                      return
                    
          except Exception as e:
            print(e)      
            async with aiohttp.ClientSession() as session:
              webhook = Webhook.from_url(config['logs_chat'], session=session)
         
              await webhook.send(f'{e}', username='Logs') 

          time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
          time_now = time.strftime('%d/%m/%Y %H:%M:%S')
          selected_disnake = self.values[0]
          loading_dict[str(interaction.user.id) + '_discord'] = selected_disnake
          
          blacklist_detector = False
          blacklist = config['blacklist']
          for i in blacklist:
            if interaction.user.get_role(i) != None:
                blacklist_detector = True


          if blacklist_detector == True:
            await interaction.response.send_message('Вы не прошли верификацию дискорда или имеете роли, запрещающие попадание в состав проекта', ephemeral=True )
            return

          if config['servers'][loading_dict[str(interaction.user.id) + '_discord']] == False:
            await interaction.response.send_message('В данный момент заявки на набор на данную вакансию закрыты, ожидайте следющего набора', ephemeral=True )
            print(f'{interaction.user} : + {interaction.user.id} попытался отправить заявку в закрытй дискорд отдел {selected_disnake} в {time_now}')
          if config['servers'][loading_dict[str(interaction.user.id) + '_discord']] == True:
            await interaction.response.send_modal(DiscordModal())
            print(f'{interaction.user} : + {interaction.user.id} выбрал открытый дискорд отдел {selected_disnake} в {time_now}')
          else:
            await interaction.response.send_message('Произошла ошибка, обратитесь в поддержку дискорд отдела', ephemeral=True )
    
       

class MainSelect(disnake.ui.Select):

    def __init__(self):
      options=[
      disnake.SelectOption(label='Дискорд отдел 🔧', value='discord'),
      disnake.SelectOption(label='Модераторский отдел 🎮', value='game'),
      disnake.SelectOption(label='Доверенный игрок 🧠', value='skutum')
      ]
      super().__init__(placeholder='Выберите отдел',min_values=1, max_values=1, options=options)

    
   
    async def callback(self, interaction: disnake.Interaction):
        

        time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        time_now = time.strftime('%d/%m/%Y %H:%M:%S')

        selected_main = self.values[0]
        loading_dict[str(interaction.user.id) + '_main'] = selected_main
        blacklist_detector = False
        blacklist_skutum_detector = False
        blacklist = config['blacklist']
        blacklist_skutum = config['blacklist_skutum']
        for i in blacklist:
           if interaction.user.get_role(i) != None:
              blacklist_detector = True


        for i in blacklist_skutum:
           if interaction.user.get_role(i) != None:
              blacklist_skutum_detector = True
              

        if blacklist_detector == True and loading_dict[str(interaction.user.id) + '_main'] != 'skutum':
            
            await interaction.response.send_message('Вы не прошли верификацию дискорда или имеете роли, запрещающие попадание в состав проекта.', ephemeral=True )
            return

        if blacklist_skutum_detector == True and loading_dict[str(interaction.user.id) + '_main'] == 'skutum':
           await interaction.response.send_message('Вы не прошли верификацию дискорда или имеете роли, запрещающие попадание в состав проекта.', ephemeral=True )
        
        
        
        if loading_dict[str(interaction.user.id) + '_main'] == 'discord':
          await interaction.response.send_message(view=DiscordView(), ephemeral=True)
          print(f'{interaction.user} : + {interaction.user.id} нажал в главном меню дискорд отдел в {time_now}')
        if loading_dict[str(interaction.user.id) + '_main'] == 'game':
          await interaction.response.send_message(view=GameView(), ephemeral=True)
          print(f'{interaction.user} : + {interaction.user.id} нажал в главном меню модераторский отдел в {time_now}')
            
            
        if loading_dict[str(interaction.user.id) + '_main'] == 'skutum':
          await interaction.response.send_message(view=GameView(), ephemeral=True)
          print(f'{interaction.user} : + {interaction.user.id} нажал в главном меню доверенный игрок отдел в {time_now}')
        
        
class AcceptButton(disnake.ui.Button):


  def __init__(self):
     super().__init__(label='✅Принять✅', style=disnake.ButtonStyle.green, custom_id='AcceptButton')

  async def callback(self, interaction: disnake.Interaction):
    

    time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    time_now = time.strftime('%d/%m/%Y %H:%M:%S')
    detector = 0
    print(f'{interaction.user} нажал на кнопку принятия в {time_now}')
    for i in premissions_list:
      if interaction.user.get_role(i) != None:
        detector += 1
    
    if detector == 0:
       await interaction.response.send_message('Нет доступа', ephemeral=True )
       return
    
    
    abriviation = {
       'sk': 'skutum',
       'gm': 'game',
       'ds': 'discord'
    }

    emb: disnake.Embed = interaction.message.embeds[0]
    emb.color = 0x27FF00
    emb.add_field(name='Принял:', value=interaction.user, inline = False) 
    embed_description = emb.description[1:]
    words = embed_description.split('_')
    departament = words[0]
    server = words[1]
    member_id = next((field.value for field in emb.fields if field.name == 'DiscordID:'), None)
    
    
    
    try: 
      member = await interaction.guild.fetch_member(member_id)
      if departament == 'sk':
        roles = member.guild.get_role(config['roles_id'][server]['skutum'])
        await member.add_roles(roles)
        with open('archive.json', 'w') as v:
          del archive[f'{member_id}_{server}_{abriviation[departament]}']
          
          json.dump(archive, v, indent=4 )

          await interaction.message.edit(embed=emb, view=None)
      
    except Exception as e:
      print(f'Ошибка! не принята анкета на доверенный игрока: {e} в {time_now}') 
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(config['logs_chat'], session=session)
         
        await webhook.send(f'Ошибка! не принята анкета на доверенный игрока: {e}', username='Logs')
        await webhook.send(f'{archive}', username='Logs')  
      

      
    try:
      member = await interaction.guild.fetch_member(member_id)
      if departament == 'gm':
        roles = member.guild.get_role(config['roles_id'][server]['y_moderator'])
        await member.add_roles(roles)
        roles = member.guild.get_role(config['roles_id'][server]['server'])
        await member.add_roles(roles)
        roles = member.guild.get_role(config['roles_id']['c_class'])
        await member.add_roles(roles)
        with open('archive.json', 'w') as v:
          del archive[f'{member_id}_{server}_{abriviation[departament]}']
          
          json.dump(archive, v, indent=4 )

          await interaction.message.edit(embed=emb, view=None)
      
        
    except Exception as e:
      print(f'Ошибка! не принята анкета на модератора: {e} в {time_now}')    
      async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'Ошибка! не принята анкета на модератора: {e}', username='Logs') 
          await webhook.send(f'{archive}', username='Logs')   

    try:
      member = await interaction.guild.fetch_member(member_id)
      if departament == 'ds':
        roles = member.guild.get_role(config['roles_id']['discord'][server]['role'])
        await member.add_roles(roles)
        roles = member.guild.get_role(config['roles_id']['c_class'])
        await member.add_roles(roles)
        with open('archive.json', 'w') as v:
          del archive[f'{member_id}_{server}_{abriviation[departament]}']
          
          json.dump(archive, v, indent=4 )

          await interaction.message.edit(embed=emb, view=None)
      
    except Exception as e:
      print(f'Ошибка! не принята анкета на дискорд работника: {e} в {time_now}')   
      async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'Ошибка! не принята анкета на дискорд работника: {e}', username='Logs') 
          await webhook.send(f'{archive}', username='Logs')  


    
    
    
class DeniedButton(disnake.ui.Button):
  
  def __init__(self):
     super().__init__(label='❌Отказать❌', style=disnake.ButtonStyle.red, custom_id='DeniedButton')

  async def callback(self, interaction: disnake.Interaction):

    time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    time_now = time.strftime('%d/%m/%Y %H:%M:%S')
    detector = 0
    print(f'{interaction.user} нажал на кнопку отказа в {time_now}')
    for i in premissions_list:
      if interaction.user.get_role(i) != None:
        detector += 1


    if detector == 0:
       await interaction.response.send_message('Нет доступа', ephemeral=True )
       return
    
    
    emb: disnake.Embed = interaction.message.embeds[0]
    emb.color = 0xFF0000
    emb.add_field(name='Отказал:', value=interaction.user, inline = False)
    discript = emb.description[1:]
    departament, server = discript.split('_')
    
    member_id = next((field.value for field in emb.fields if field.name == 'DiscordID:'), None)
    
    await interaction.response.send_modal(DeniedModal(message_id=interaction.message.id, member_discord_id=member_id, departament=departament,  server=server, emded_denied=emb)) 
    
       



class DeniedModal(disnake.ui.Modal):
  def __init__(self, message_id, member_discord_id, departament, server, emded_denied):
        self.message_id = message_id
        self.member_discord_id = member_discord_id
        self.departament = departament
        self.server = server
        self.emded_denied = emded_denied
        super().__init__(
            title=f'Отказ', 
            components=[
              disnake.ui.TextInput(
                custom_id='reason',
                style=disnake.TextInputStyle.short,
                label='Причина отказа',
                required=False,
                placeholder='Введите причину отказа'
              ), 
              
              disnake.ui.TextInput(
                custom_id='comment',
                style=disnake.TextInputStyle.short,
                label='Коментарии',
                required=False,
              )
            ]
          ) 
  async def callback(self, interaction: disnake.Interaction):
      abriviation = {
       'sk': 'доверенного игрока',
       'gm': 'модератора',
       'ds': 'дискорд сотрудника'
      }
      abriviation_acrhive = {
       'sk': 'skutum',
       'gm': 'game',
       'ds': 'discord'
    }
      server = config['abbreviation'][self.server]
      departament = abriviation[self.departament]
      message = f'Ваша заявка на __{departament}__ на сервере/должность __{server}__ была отклонена'
      

      denied_modal_embed = disnake.Embed(
        colour=disnake.Colour.red(),
        title=f'Отказ! {message}',
      )
      
      
      denied_modal_embed.add_field(name='Причина:', value=interaction.text_values['reason']) 
      denied_modal_embed.add_field(name='Комментарии:', value=interaction.text_values['comment']) 
      
      if self.departament == 'sk':
         from_server = f'scutum_{self.server}'
      if self.departament == 'gm':
         from_server = self.server
      if self.departament == 'ds':
         from_server = self.server


      self.emded_denied.add_field(name='Причина:', value=interaction.text_values['reason'], inline = False)
      channel = aclient.get_channel(config['form_channel'][from_server])
      msg_id = self.message_id
      msg = await channel.fetch_message(msg_id)
      await msg.edit(content="", embed=self.emded_denied, view=None)
     
      
      date_until = datetime.datetime.now(pytz.timezone('Europe/Moscow')) + datetime.timedelta(days = config['cooldown_form'])
      with open('archive.json', 'w+') as v:
        archive[f'{self.member_discord_id}_{self.server}_{abriviation_acrhive[self.departament]}']['accepted'] = True
        archive[f'{self.member_discord_id}_{self.server}_{abriviation_acrhive[self.departament]}']['date_until'] = str(date_until.strftime('%d/%m/%y %H:%M:%S'))
        json.dump(archive, v, indent=4 )
      try:
        
        user = await aclient.fetch_user(self.member_discord_id)
         
        await user.send(embed=denied_modal_embed)
        await interaction.response.send_message('Отказано успешно!', ephemeral=True)
        
      except Exception as e:
        print(e)
        async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'{e}', username='Logs') 
        await interaction.response.send_message(f'Ошибка отправки сообщения: {e}', ephemeral=True)
      time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
      time_now = time.strftime('%d/%m/%Y %H:%M:%S')
      print(f'{interaction.user.id} отказал заявку {self.member_discord_id} на {departament} в {time_now}')
      

      

class DepartamentView(disnake.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
      self.add_item(MainSelect())

class DiscordView(disnake.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
      self.add_item(DiscordSelect())


class GameView(disnake.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
      self.add_item(GameSelect())

class ButtonView(disnake.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
      self.add_item(AcceptButton())
      self.add_item(DeniedButton())









@aclient.slash_command(description="Создает новое меню для подачи заявок.")
async def form_create(ctx):
  info_embed = disnake.Embed(
        colour=disnake.Colour.gold(),
        title=f'"Подача заявок в персонал или доверенных игроков"',
        description=config['embed_select_menu']
      )
  await ctx.send(embed=info_embed,view=DepartamentView())






@form_create.error
async def form_create_error(ctx, error ):
    if isinstance(error, commands.MissingAnyRole):
       await ctx.send('Нет доступа')
    else:
       print(error)
       async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'{e}', username='Logs') 
       

Servers = {
  "Chaotic" : 'ch',
  "MiniGames" :'mg',
  "FunRP" : 'fnrp',
  "LightRP" : 'lrp',
  "MediumRP" : 'mrp',
  "HardRP" : 'hrp',      
  "Кодер" : 'cdr',      
  "Ивент_Мастер": 'ivms',     
  "Декоратор" : 'dkr',
}
Open_Close = {
   "Открыть": "True",
   "Закрыть" : "False"
}
Skutum_test = {
   "доверенные игроки" : 's',
   "Модератор" : 'md',
   "Оба" : 'both'
}
@aclient.slash_command(description='Открыть/Закрыть заявки.')
async def formtoggle(ctx, server:str=commands.Param(choices=Servers, description='выберите сервер/должность.'), 
                     open_close: str=commands.Param(choices=Open_Close, description='Переключатель откытие или закрытие заявок'), 
                     type: str=commands.Param(default=None, choices=Skutum_test, description='Какой отдел закрыть/открыть.')):
  servers_config = config['abbreviation'][server]
 
  open_close = eval(open_close)
 
  if open_close == True:
    server_status = 'открыты'
    
  if open_close == False:
    server_status = 'закрыты'
  
 
  if server in ['cdr', 'ivms', 'dkr']:
    with open('config.json', 'w') as f:
          config['servers'].update({f'{server}' : open_close})
          json.dump(config, f, indent=4 )
    await ctx.send(f'Заявки в дискорд отдел на должность {servers_config} {server_status}')
    return

  if type == None:
     await ctx.send('Ошибка! Не был выбран отдел.')
     return

  if type == 's':

    with open('config.json', 'w') as f:
          config['servers'].update({f's{server}' : open_close})
          json.dump(config, f, indent=4 )
    await ctx.send(f'Заявки на доверенных игроков и на должность {servers_config} {server_status}')
  

  if type == 'md':
    with open('config.json', 'w') as f:
          config['servers'].update({f'{server}' : open_close})
          json.dump(config, f, indent=4 )
    await ctx.send(f'Заявки в модератор отдел на должность {servers_config} {server_status}')

  if type == 'both':
    with open('config.json', 'w') as f:
          config['servers'].update({f's{server}' : open_close})
          json.dump(config, f, indent=4 )
    await ctx.send(f'Заявки на доверенных игроков и модератор-отдел на должность {servers_config} {server_status}')  
 

  

@formtoggle.error
async def form_open_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
       await ctx.send('Нет доступа')
    else:
       print(error)
       async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'{e}', username='Logs') 
       



@aclient.slash_command(description='Перезапуск бота.')
async def restart_form(ctx):
    await ctx.send("Перезагрузка...")
    print(f'{ctx.author.id} попытался перезагрузить бота')
    try:
      os.system("python main.py")
      
    except Exception as e:
      await ctx.send("Перезагрузка сломалась :(") 
      print(e)
      async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'Ошибка! не принята анкета на дискорд работника: {e}', username='Logs')  
    
    
@restart_form.error
async def restart_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
       await ctx.send('Нет доступа')
    else:
       print(error)
       async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(config['logs_chat'], session=session)
         
          await webhook.send(f'Ошибка! не принята анкета на дискорд работника: {e}', username='Logs') 
       

aclient.run(
  token['token'])
