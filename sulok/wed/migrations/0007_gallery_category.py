# Generated by Django 3.1.7 on 2021-03-17 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wed.category'),
        ),
    ]
