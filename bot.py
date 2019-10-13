#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(bot, context):
    """Send a message when the command /start is issued."""
    chat_id = bot.message.chat_id
    bot.message.reply_text("ChatBot Clinica 10Ten"
                           "\nDesde este chat usted puede realizar consultas, cancelar y reservar citas medicas")
    bot.message.reply_text("/acceder (username)\nIndique su usuario")
    bot.message.reply_text("/consultar (Lunes 15:30 Odontologia)\nIndique el dia, la hora y la especialidad")
    bot.message.reply_text("/reservar (Lunes 15:30 Odontologia)\nReserve una cita medica")
    bot.message.reply_text("/cancelar (Lunes 15:30 Odontologia)\nCancelar una cita medica")
    bot.message.reply_text("/diccionario (paracetamol)\nRevisar medicamentos o alghnos terminos de medicina")


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('En que le podemos ayudar!!!')


def echo(update, context):
    """Echo the user message."""
    if update.message.text.upper() == 'HOLA' or update.message.text.upper() == 'BUEN DIA' or update.message.text.upper() == 'BUENOS DIAS':
        update.message.reply_text('Hola buen dia!!!')
    else:
        update.message.reply_text('No reconozco la instruccion, aun estoy aprendiendo!!!')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def acceder(bot, context):
    try:
        bot.message.reply_text('Bienvenido ' + context.args[0])
    except(TypeError, NameError, ValueError):
        bot.message.reply_text('ERROR!!!')


def consultar(bot, context):
    try:
        bot.message.reply_text('Horario no disponible.')
    except(TypeError, NameError, ValueError):
        bot.message.reply_text('ERROR!!!')


def reservar(bot, context):
    try:
        bot.message.reply_text('Reservacion exitosa.')
    except(TypeError, NameError, ValueError):
        bot.message.reply_text('ERROR!!!')


def cancelar(bot, context):
    try:
        bot.message.reply_text('Cancelacion exitosa.')
    except(TypeError, NameError, ValueError):
        bot.message.reply_text('ERROR!!!')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("889768953:AAGQDjtMRcwOovNtkC9qorapTT49K3cnm54", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("acceder", acceder))
    dp.add_handler(CommandHandler("consultar", consultar))
    dp.add_handler(CommandHandler("reservar", reservar))
    dp.add_handler(CommandHandler("cancelar", cancelar))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
