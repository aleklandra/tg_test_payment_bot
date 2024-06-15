import pytz
import time
import telebot
import schedule
from yoga_payment_bot import settings
from .check_subscriptions import notification_about_subscription


def bot_send_notification_message():
    notifications = notification_about_subscription()
    if notifications is None:
        return None
    else:
        bot = telebot.TeleBot(settings.BOT_TOKEN)
        count = 0
        for message in notifications:
            bot.send_message(message['chat_id'], message['message'])
            count += 1
            if count == 10:
                time.sleep(10)


schedule.every().days.at('16:57', pytz.timezone('Europe/Moscow')).do(bot_send_notification_message)