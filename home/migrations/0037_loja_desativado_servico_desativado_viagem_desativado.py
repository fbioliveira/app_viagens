# Generated by Django 5.0.4 on 2024-06-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_loja_postos_alter_loja_republica'),
    ]

    operations = [
        migrations.AddField(
            model_name='loja',
            name='desativado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servico',
            name='desativado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='viagem',
            name='desativado',
            field=models.BooleanField(default=False),
        ),
    ]