# Generated by Django 3.0.3 on 2020-02-12 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promise', '0002_auto_20200210_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promise',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promise', to=settings.AUTH_USER_MODEL),
        ),
    ]
