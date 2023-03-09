# Generated by Django 4.1.2 on 2023-03-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_links', '0003_alter_explorerlinks_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_1',
        ),
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_2',
        ),
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_3',
        ),
        migrations.RemoveField(
            model_name='explorerlinks',
            name='explorer_link_4',
        ),
        migrations.AddField(
            model_name='explorerlinks',
            name='explorer_links',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
