# Generated by Django 3.0.3 on 2020-02-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promise',
            name='dline',
            field=models.CharField(max_length=20),
        ),
    ]