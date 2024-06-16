from yoomoney import Quickpay
from yoga_payment_bot import settings


def quickpay():
    quickpay = Quickpay(
                receiver=settings.BOT_PAY_RECIEVER,
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=2,
                )
    print(quickpay.base_url)
    print(quickpay.redirected_url)