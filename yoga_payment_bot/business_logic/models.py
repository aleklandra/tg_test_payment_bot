from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime


class Clients(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Внешний ID клиента',
        unique=True,
        db_index=True)
    first_name = models.TextField(
        verbose_name='Имя клиента')
    last_name = models.TextField(
        verbose_name='Фамилия клиента')
    date_added = models.DateTimeField(verbose_name='Дата первого подключения',
                                      auto_now_add=True,
                                      db_index=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('-date_added', )
    

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    start_date = models.DateField(verbose_name='Дата первого подключения',
                                  default=timezone.now,
                                  db_index=True)
    amount_of_days = models.SmallIntegerField(verbose_name=(
        'Количество дней в подписке'),)
    product = models.CharField(verbose_name='Продукт в подписке',
                               max_length=256)
    current_status = models.CharField(verbose_name='Активность подписки',
                                      max_length=256)
    client = models.ForeignKey(Clients, related_name='client',
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='Клиент')
    expire_date = models.DateField(verbose_name='Дата окончания подписки',
                                   default=timezone.now,
                                   db_index=True)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-start_date', )

    def save(self, *args, **kwargs):
        self.expire_date = (self.start_date
                            + timedelta(days=self.amount_of_days))
        super(Subscriptions, self).save(*args, **kwargs)

    def __str__(self):
        return (f'{self.start_date}: продолжительность '
                f'{self.amount_of_days} дней')
