from .payment_auth import Authorize
from yoga_payment_bot import settings
from yoomoney import Client


def check_pay_accaunt():
    pay_token = Authorize(
        client_id=settings.BOT_PAY_CLIENT_ID,
        redirect_uri=settings.BOT_REDIRECT_URI,
        scope=["account-info",
               "operation-history",
               "operation-details",
               "incoming-transfers",
               "payment-p2p",
               "payment-shop",]
        ).get_access_token()

    print('Ваш токен: ', str(pay_token), '\n'+
          'Теперь его нужно перезаписать в глобальные переменные')
    client = Client(pay_token)
    user = client.account_info()
    print("Account number:", user.account)
    print("Account balance:", user.balance)
    print("Account currency code in ISO 4217 format:", user.currency)
    print("Account status:", user.account_status)
    print("Account type:", user.account_type)
    print("Extended balance information:")
    for pair in vars(user.balance_details):
        print("\t-->", pair, ":", vars(user.balance_details).get(pair))
    print("Information about linked bank cards:")
    cards = user.cards_linked
    if len(cards) != 0:
        for card in cards:
            print(card.pan_fragment, " - ", card.type)
    else:
        print("No card is linked to the account")
