# Generated by Django 3.0.9 on 2020-10-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0009_auto_20200821_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='canonical_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
