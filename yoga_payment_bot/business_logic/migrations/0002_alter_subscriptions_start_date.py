# Generated by Django 3.2.16 on 2024-06-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_logic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptions',
            name='start_date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата первого подключения'),
        ),
    ]
