# Generated by Django 5.0.4 on 2024-05-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_viagem_lojas_viagem_lojas'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
