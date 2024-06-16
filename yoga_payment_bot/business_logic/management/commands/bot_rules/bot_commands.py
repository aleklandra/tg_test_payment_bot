from asgiref.sync import sync_to_async
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from business_logic.models import Clients

PAY_30_YOGA_BUTTON = KeyboardButton('Оплатить подписку на 30 дней')
PAY_180_YOGA_BUTTON = KeyboardButton('Оплатить подписку на 180 дней')
PAY_365_YOGA_BUTTON = KeyboardButton('Оплатить подписку на 365 дней')
HELP_BUTTON = KeyboardButton('Помощь')
INFO_BUTTON = KeyboardButton('Информация')
KEYBOARD = ReplyKeyboardMarkup([[PAY_30_YOGA_BUTTON],
                                [PAY_180_YOGA_BUTTON],
                                [PAY_365_YOGA_BUTTON],
                                [INFO_BUTTON, HELP_BUTTON],])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await Clients.objects.aupdate_or_create(external_id=user.id,
                                            first_name=user.first_name,
                                            last_name=user.last_name,
                                            username=user.username
                                            )
    await update.message.reply_html(
        rf'Hi {user.mention_html()}! Чтобы оплатить подписку, нажмите "Оплатить"',
        reply_markup=KEYBOARD,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

