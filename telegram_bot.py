import requests
import telebot
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from newsapi import NewsApiClient

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_CHATID = os.environ.get('BOT_CHATID')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


    
bot.infinity_polling()