# Generated by Django 3.2.9 on 2021-11-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('views', models.IntegerField(blank=True, null=True)),
                ('clicks', models.IntegerField(blank=True, null=True)),
                ('cost', models.FloatField()),
            ],
        ),
    ]
