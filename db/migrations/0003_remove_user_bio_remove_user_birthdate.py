# Generated by Django 4.0.2 on 2023-11-08 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_user_order_ticket_alter_movie_actors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
    ]