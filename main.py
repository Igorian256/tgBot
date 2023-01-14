import telebot

bot = telebot.TeleBot('5889411393:AAFIfd7ZDcqmeHuF_tqYgo9SAjWXrJ88sjw')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, сучка!, Как дела твои? Напиши одним словом', parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == "нормально":
        bot.send_message(message.chat.id, 'А я устал что-то!', parse_mode='html')
    elif message.text == "хорошо":
        bot.send_message(message.chat.id, 'Тебе то хорошо, сам таким состоянием не могу похвастаться', parse_mode='html')
    elif message.text == "пойдёт":
        bot.send_message(message.chat.id, 'В смысле поёдет, давай подробнее!!', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Расслабься! Когда ЧБД? https://www.youtube.com/shorts/iURj2GdSvZA', parse_mode='html')
bot.polling(none_stop=True)

