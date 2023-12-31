# Generated by Django 4.2.1 on 2023-07-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_automation', '0009_alter_botuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='phrase',
            field=models.TextField(help_text='seed-phrase для доступа к кошельку', null=True),
        ),
        migrations.AddField(
            model_name='botuser',
            name='recipient_wallet',
            field=models.TextField(help_text='адрес кошелька(0x...), на который будут поступать eth', null=True),
        ),
        migrations.AddField(
            model_name='botuser',
            name='sender_wallet',
            field=models.TextField(help_text='адрес кошелька(0x...), с которого будут совершаться транзакции', null=True),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(help_text='Введите имя пользователя. Максимсальная длина - 20', max_length=20, null=True),
        ),
    ]
