import telebot 
import random
import json
import time


bot = telebot.TeleBot('6435309466:AAGIuwwpNu-Ey5Eh_PcR5xCzyCp4ACPy4v8')

with open('config.json') as v:
    config = json.load(v)
    v.close()


def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['ping'])
def ping(message):
    status = extract_arg(message.text)
    random_seconds = random.uniform(config['min_time_to_send_message'], config['max_time_to_send_message'])
    cheker = 0
    ping_amount = config['ping_amount']
    all_info = message.json
    user_id = all_info['from']['id']
    if user_id in config['admins']:
        while cheker != ping_amount:
            bot.send_message(message.chat.id, status)
            time.sleep(random_seconds)
            cheker += 1
        bot.send_message(message.chat.id, 'готово')
    if user_id not in config['admins']:
        bot.send_message(message.chat.id, 'нема прав на такое злодияние')


bot.polling(none_stop=True)