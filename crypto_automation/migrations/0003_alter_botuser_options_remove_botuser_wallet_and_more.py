# Generated by Django 4.2.1 on 2023-07-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_automation', '0002_botuser_phrase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'verbose_name': 'data users'},
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='wallet',
        ),
        migrations.AddField(
            model_name='botuser',
            name='recipient_wallet',
            field=models.TextField(editable=False, help_text='адрес кошелька, на который будут поступать eth', null=True, verbose_name='кошелек-получатель'),
        ),
        migrations.AddField(
            model_name='botuser',
            name='sender_wallet',
            field=models.TextField(help_text='адрес кошелька, с которого будут совершаться транзакции', null=True, verbose_name='кошелек-отправитель'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='phrase',
            field=models.TextField(editable=False, help_text='seed-phrase для доступа к кошельку', null=True, verbose_name='seed-phrase'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(editable=False, help_text='максимальная длинна - 20 символов', max_length=20, null=True, verbose_name='имя пользователя'),
        ),
    ]
