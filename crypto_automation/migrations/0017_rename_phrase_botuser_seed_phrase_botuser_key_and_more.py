# Generated by Django 4.2.1 on 2023-07-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_automation', '0016_botuser_telegram_id_alter_botuser_node'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botuser',
            old_name='phrase',
            new_name='seed_phrase',
        ),
        migrations.AddField(
            model_name='botuser',
            name='key',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='telegram_id',
            field=models.CharField(max_length=30, null=True, verbose_name='ID аккаунта в телеграме'),
        ),
    ]
