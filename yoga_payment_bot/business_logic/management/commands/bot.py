import logging
import asyncio
from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .bot_rules.bot_commands import start, help_command, echo
from .bot_rules.run_background import run_continuously

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Start your bot'

    def handle(self, *args, **options):

        application = (Application.builder()
                       .token("6870926047:AAF0iwDlLXYwn0lSjTe8mllusx_3VN6qz4Q").build())

        # on different commands - answer in Telegram
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))

        # on non command i.e message - echo the message on Telegram
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

        # Run the bot until the user presses Ctrl-C

        run_continuously()

        application.run_polling(allowed_updates=Update.ALL_TYPES)

    if __name__ == 'handle':
        handle()
