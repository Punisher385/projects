import telebot

token='7905158284:AAGmQ_sBOzPUvxDQQEwCJFPrRp-0iDHiQqU'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if name == 'main':
     bot.infinity_polling()