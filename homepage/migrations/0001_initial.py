# Generated by Django 4.1 on 2022-08-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=100, verbose_name='English')),
                ('uzbek', models.CharField(max_length=100, verbose_name='Uzbek')),
            ],
        ),
    ]
