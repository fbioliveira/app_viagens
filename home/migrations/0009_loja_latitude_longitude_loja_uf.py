# Generated by Django 5.0.4 on 2024-05-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_viagem_servicos_viagem_servicos'),
    ]

    operations = [
        migrations.AddField(
            model_name='loja',
            name='latitude_longitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='loja',
            name='uf',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
