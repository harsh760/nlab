# Generated by Django 3.2 on 2021-05-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210502_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
