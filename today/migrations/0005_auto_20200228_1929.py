# Generated by Django 3.0.2 on 2020-02-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0004_mytest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytest',
            name='repo',
            field=models.ManyToManyField(to='today.Article'),
        ),
    ]