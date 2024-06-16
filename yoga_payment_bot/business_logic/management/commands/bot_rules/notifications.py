import pytz
import time
import telebot
import schedule
from yoga_payment_bot import settings
from .check_subscriptions import notification_about_subscription

PAY_30_YOGA_BUTTON = telebot.types.KeyboardButton('Оплатить подписку на 30 дней')
PAY_180_YOGA_BUTTON = telebot.types.KeyboardButton('Оплатить подписку на 180 дней')
PAY_365_YOGA_BUTTON = telebot.types.KeyboardButton('Оплатить подписку на 365 дней')
HELP_BUTTON = telebot.types.KeyboardButton('Помощь')
INFO_BUTTON = telebot.types.KeyboardButton('Информация')

KEYBOARD = telebot.types.InlineKeyboardMarkup([[PAY_30_YOGA_BUTTON],
                                              [PAY_180_YOGA_BUTTON],
                                              [PAY_365_YOGA_BUTTON]],
                                              row_width=1)


def bot_send_notification_message():
    notifications = notification_about_subscription()
    if notifications is None:
        return None
    else:
        bot = telebot.TeleBot(settings.BOT_TOKEN)
        count = 0
        for message in notifications:
            bot.send_message(message['chat_id'], message['message'],
                             reply_markup=KEYBOARD)
            count += 1
            if count == 10:
                time.sleep(10)


schedule.every().days.at('16:57', pytz.timezone('Europe/Moscow')).do(bot_send_notification_message)