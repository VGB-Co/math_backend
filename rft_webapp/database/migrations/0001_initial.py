# Generated by Django 2.1.2 on 2018-12-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=None)),
                ('username', models.TextField()),
                ('type', models.IntegerField(default=None)),
                ('score', models.IntegerField(default=None)),
                ('time', models.FloatField(default=None)),
            ],
        ),
    ]
