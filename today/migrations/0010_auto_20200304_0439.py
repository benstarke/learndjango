# Generated by Django 3.0.2 on 2020-03-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0009_postproblem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproblem',
            name='image',
            field=models.ImageField(null=True, upload_to='problem_pics'),
        ),
    ]