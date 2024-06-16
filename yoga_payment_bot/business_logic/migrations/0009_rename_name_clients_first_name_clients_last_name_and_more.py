# Generated by Django 4.2 on 2024-06-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_logic', '0008_auto_20240615_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='clients',
            name='last_name',
            field=models.TextField(null=True, verbose_name='Фамилия клиента'),
        ),
        migrations.AddField(
            model_name='clients',
            name='username',
            field=models.TextField(null=True, verbose_name='ТГ ник клиента'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='external_id',
            field=models.PositiveIntegerField(db_index=True, unique=True, verbose_name='Внешний ID клиента'),
        ),
    ]
