# Generated by Django 5.0.4 on 2024-06-11 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_role_user_alter_role_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='suporte',
            name='desativado',
            field=models.BooleanField(default=False),
        ),
    ]