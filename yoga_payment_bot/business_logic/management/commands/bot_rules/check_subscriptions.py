from datetime import datetime, timedelta
from business_logic.models import Subscriptions


def check_subscriptions():
    tomorrow = datetime.today() + timedelta(days=1)
    tomorrow_expire_subs = (Subscriptions
                              .objects
                              .select_related('client')
                              .filter(expire_date=tomorrow)
                              .values_list('client__external_id',
                                           'client__first_name',
                                           'start_date',
                                           'amount_of_days'))
    if tomorrow_expire_subs.count() == 0:
        return None
    else:
        clients_dict = []
        for client in tomorrow_expire_subs:
            clients_dict.append(
                {
                    'external_id': client[0],
                    'name': client[1],
                    'start_date': client[2],
                    'amount_of_days': client[3]
                }
            )
        return clients_dict


def notification_about_subscription():
    clients_list = check_subscriptions()

    if clients_list is None:
        return None
    else:
        notifications = []
        for client in clients_list:
            name = client['name']
            start_date = client['start_date']
            chat_id = client['external_id']
            notifications.append(
                {'message': (f'Добрый день, {name}!\n'
                             + 'Подписка на канал @letters_to_my_friends '
                             + f'от {start_date} истекает уже завтра.\n'
                             + 'Если хотите продлить подпику '
                             + 'нажмите на кнопку "оплатить подпику".'),
                 'chat_id': chat_id})
        return notifications
