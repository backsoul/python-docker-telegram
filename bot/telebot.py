# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler)
from telegram import Update
import emoji
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()  # take environment variables from .env.
def start(update, context):
    print("Iniciaron el bot!!")
    update.message.reply_text(f'Hello {update.effective_user.first_name} :pulgar_hacia_arriba:')
    update.message.reply_text(os.environ["DB_HOST"])
    update.message.reply_text(os.environ["DB_USER"])
    update.message.reply_text(os.environ["DB_PASSWORD"])
 

def main():
    TOKEN=os.environ["TOKEN"]
    updater=Updater(TOKEN, use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',	start))
    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    # mydb = mysql.connector.connect(
    # host=os.environ["DB_HOST"],
    # user=os.environ["DB_USER"],
    # password=os.environ["DB_PASSWORD"]
    # )
    # print(mydb)
    main()