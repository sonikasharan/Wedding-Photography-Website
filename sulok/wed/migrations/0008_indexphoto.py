# Generated by Django 3.1.7 on 2021-03-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0007_gallery_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='indexpics')),
            ],
        ),
    ]
