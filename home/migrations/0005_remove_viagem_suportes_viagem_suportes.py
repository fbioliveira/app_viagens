# Generated by Django 5.0.4 on 2024-05-07 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_viagem_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viagem',
            name='suportes',
        ),
        migrations.AddField(
            model_name='viagem',
            name='suportes',
            field=models.ManyToManyField(blank=True, related_name='viagens', to='home.suporte'),
        ),
    ]
