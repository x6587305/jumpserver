# Generated by Django 2.2.13 on 2020-10-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0059_auto_20201027_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='ip',
            field=models.CharField(db_index=True, max_length=128, verbose_name='IP'),
        ),
    ]
