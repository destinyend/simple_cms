# Generated by Django 4.1 on 2022-08-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_block_object_fit'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='effect',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
    ]