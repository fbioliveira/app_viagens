# Generated by Django 5.0.4 on 2024-05-17 16:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_customuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SenhaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='senha_raw', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
