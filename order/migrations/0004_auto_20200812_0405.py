# Generated by Django 3.0.8 on 2020-08-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200810_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='selected_theme',
        ),
        migrations.AddField(
            model_name='order',
            name='metadata',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
