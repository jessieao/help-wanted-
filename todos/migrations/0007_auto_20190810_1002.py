# Generated by Django 2.1 on 2019-08-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_todo_sent_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='sent_reminder',
            field=models.BooleanField(null=True, verbose_name=bool),
        ),
    ]
