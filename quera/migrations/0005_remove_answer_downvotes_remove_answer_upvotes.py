# Generated by Django 4.2.6 on 2023-11-26 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quera', '0004_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='upvotes',
        ),
    ]
