# Generated by Django 3.1.7 on 2021-03-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0003_aboutme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='aboutpic')),
            ],
        ),
    ]
