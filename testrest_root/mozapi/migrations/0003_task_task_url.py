# Generated by Django 3.2.8 on 2021-10-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozapi', '0002_delete_fake'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
