# Generated by Django 2.2.7 on 2019-12-27 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_animal_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='created_date',
            new_name='created',
        ),
    ]