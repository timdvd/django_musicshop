# Generated by Django 3.0.2 on 2020-08-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]