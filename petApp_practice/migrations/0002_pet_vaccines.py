# Generated by Django 4.1.5 on 2023-01-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petApp_practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='vaccines',
            field=models.ManyToManyField(to='petApp_practice.vaccines'),
        ),
    ]