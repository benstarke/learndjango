# Generated by Django 3.0.2 on 2020-03-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0008_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='problem_pics')),
                ('solution', models.TextField()),
                ('solve', models.TextField()),
            ],
        ),
    ]