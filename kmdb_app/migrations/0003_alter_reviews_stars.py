# Generated by Django 3.2.6 on 2021-08-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmdb_app', '0002_alter_reviews_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='stars',
            field=models.IntegerField(),
        ),
    ]
