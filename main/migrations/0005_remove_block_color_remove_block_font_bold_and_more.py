# Generated by Django 4.1 on 2022-08-29 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_text_block_html'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='color',
        ),
        migrations.RemoveField(
            model_name='block',
            name='font_bold',
        ),
        migrations.RemoveField(
            model_name='block',
            name='font_italic',
        ),
        migrations.RemoveField(
            model_name='block',
            name='font_size',
        ),
        migrations.RemoveField(
            model_name='block',
            name='font_underline',
        ),
        migrations.RemoveField(
            model_name='block',
            name='height',
        ),
        migrations.RemoveField(
            model_name='block',
            name='horizontal_align',
        ),
        migrations.RemoveField(
            model_name='block',
            name='object_fit',
        ),
        migrations.RemoveField(
            model_name='block',
            name='vertical_align',
        ),
        migrations.RemoveField(
            model_name='block',
            name='width',
        ),
    ]