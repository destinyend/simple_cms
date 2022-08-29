# Generated by Django 4.1 on 2022-08-29 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=128)),
                ('time', models.FloatField()),
            ],
            options={
                'db_table': 'api_stat',
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.SmallIntegerField(default=999)),
                ('text', models.TextField(blank=True, default='')),
                ('font_size', models.PositiveSmallIntegerField(default=14)),
                ('font_italic', models.BooleanField(default=False)),
                ('font_bold', models.BooleanField(default=False)),
                ('font_underline', models.BooleanField(default=False)),
                ('color', models.CharField(default='black', max_length=16)),
                ('background', models.CharField(blank=True, default='', max_length=6)),
                ('bg_image', models.FileField(blank=True, upload_to='images')),
                ('width', models.PositiveSmallIntegerField(default=100)),
                ('height', models.PositiveSmallIntegerField(default=40)),
                ('horizontal_align', models.CharField(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')], default='left', max_length=6)),
                ('vertical_align', models.CharField(choices=[('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom')], default='top', max_length=6)),
            ],
            options={
                'db_table': 'blocks',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(db_index=True, max_length=64, unique=True)),
                ('status', models.CharField(choices=[('a', 'Active'), ('b', 'Banned')], default='a', max_length=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
