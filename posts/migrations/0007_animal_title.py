# Generated by Django 2.2.7 on 2019-11-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_animal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]