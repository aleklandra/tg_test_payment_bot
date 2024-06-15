from asgiref.sync import sync_to_async
from telegram import ForceReply, Update
from telegram.ext import ContextTypes
from business_logic.models import Clients


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await Clients.objects.aupdate_or_create(external_id=user.id,
                                            name=(f'{user.first_name}'
                                                  + f'{user.last_name}')
                                            )
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

