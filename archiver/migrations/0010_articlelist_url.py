# Generated by Django 3.0.1 on 2020-02-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiver', '0009_auto_20200202_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlelist',
            name='url',
            field=models.CharField(default='', max_length=2086),
            preserve_default=False,
        ),
    ]
