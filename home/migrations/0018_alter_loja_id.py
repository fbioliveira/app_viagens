# Generated by Django 5.0.4 on 2024-05-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_suporte_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]