from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .bot_rules.bot_commands import start, help_command, echo
from .bot_rules.run_background import run_continuously
from yoga_payment_bot import settings
from .app_logger import get_logger


logger = get_logger(__name__)


class Command(BaseCommand):
    help = 'Start your bot'

    def handle(self, *args, **options):

        application = (Application.builder()
                       .token(settings.BOT_TOKEN).build())

        # on different commands - answer in Telegram
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('help', help_command))

        # on non command i.e message - echo the message on Telegram
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

        # Scheduler
        run_continuously()

        # Run the bot until the user presses Ctrl-C
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    if __name__ == 'handle':
        handle()
