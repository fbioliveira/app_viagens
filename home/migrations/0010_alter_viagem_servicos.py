# Generated by Django 5.0.4 on 2024-05-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_loja_latitude_longitude_loja_uf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='servicos',
            field=models.ManyToManyField(blank=True, related_name='servicos', to='home.servico'),
        ),
    ]