# Generated by Django 5.0.4 on 2024-06-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_loja_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='tipo',
            field=models.CharField(choices=[('Filial', 'Filial'), ('Posto', 'Posto'), ('Representante', 'Representante'), ('Deposito', 'Deposito')], default='N/A', max_length=20),
        ),
    ]
