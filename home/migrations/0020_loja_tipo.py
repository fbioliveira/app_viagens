# Generated by Django 5.0.4 on 2024-06-01 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_loja_loja_mae_alter_suporte_imagem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loja',
            name='tipo',
            field=models.CharField(choices=[('filial', 'Filial'), ('posto', 'Posto'), ('rep', 'Representante')], default='N/A', max_length=10),
        ),
    ]
