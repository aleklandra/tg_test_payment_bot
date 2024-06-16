import logging
from django.core.management.base import BaseCommand
from .payments.payment_link import quickpay
from .app_logger import get_logger


logger = get_logger(__name__)


class Command(BaseCommand):
    help = 'Start check your payment accaunt'

    def handle(self, *args, **options):
        try:
            quickpay()
        except Exception as error:
            logger.error(f'Проблема с авторизацией платежей {error}')
