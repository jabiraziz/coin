# Generated by Django 4.1.2 on 2023-02-28 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coin_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=120, null=True)),
                ('reddit', models.CharField(max_length=120, null=True)),
                ('source_code', models.CharField(max_length=120, null=True)),
                ('website', models.CharField(max_length=120, null=True)),
                ('youtube_link', models.CharField(max_length=120, null=True)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin_profile.coinprofile')),
            ],
            options={
                'verbose_name_plural': 'Social Links',
            },
        ),
        migrations.CreateModel(
            name='ExplosureLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explorer_link_1', models.CharField(max_length=120, null=True)),
                ('explorer_link_2', models.CharField(max_length=120, null=True)),
                ('explorer_link_3', models.CharField(max_length=120, null=True)),
                ('explorer_link_4', models.CharField(max_length=120, null=True)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin_profile.coinprofile')),
            ],
            options={
                'verbose_name_plural': 'Explosure Links',
            },
        ),
    ]
