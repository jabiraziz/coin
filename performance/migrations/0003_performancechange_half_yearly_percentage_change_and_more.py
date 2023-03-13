# Generated by Django 4.1.2 on 2023-03-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_performancechange_coin_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancechange',
            name='half_yearly_percentage_change',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='performancechange',
            name='monthly_percentage_change',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='performancechange',
            name='quarterly_percentage_change',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='performancechange',
            name='weekly_percentage_change',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='performancechange',
            name='yearly_percentage_change',
            field=models.IntegerField(null=True),
        ),
    ]
