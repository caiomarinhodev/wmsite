# Generated by Django 3.1.7 on 2021-12-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211202_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nome_empresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]