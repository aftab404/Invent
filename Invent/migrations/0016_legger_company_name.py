# Generated by Django 3.0 on 2019-12-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invent', '0015_auto_20191226_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='legger',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]