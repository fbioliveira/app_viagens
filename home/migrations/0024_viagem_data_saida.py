# Generated by Django 5.0.4 on 2024-06-09 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_suporte_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='data_saida',
            field=models.DateField(blank=True, default=datetime.date(2024, 6, 9), null=True),
        ),
    ]