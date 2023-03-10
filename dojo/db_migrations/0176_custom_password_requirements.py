# Generated by Django 3.2.16 on 2022-11-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0175_system_settings_enable_notify_sla'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_settings',
            name='lowercase_character_required',
            field=models.BooleanField(default=True, help_text='Requires user passwords to contain at least one lowercase letter (a-z).', verbose_name='Password must contain one lowercase letter'),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='maximum_password_length',
            field=models.IntegerField(default=48, help_text='Requires user to set passwords less than maximum length.', verbose_name='Maximum password length'),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='minimum_password_length',
            field=models.IntegerField(default=9, help_text='Requires user to set passwords greater than minimum length.', verbose_name='Minimum password length'),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='number_character_required',
            field=models.BooleanField(default=True, help_text='Requires user passwords to contain at least one digit (0-9).', verbose_name='Password must contain one digit'),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='special_character_required',
            field=models.BooleanField(default=True, help_text='Requires user passwords to contain at least one special character (()[]{}|\\`~!@#$%^&*_-+=;:\'",<>./?).', verbose_name='Password must contain one special character'),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='uppercase_character_required',
            field=models.BooleanField(default=True, help_text='Requires user passwords to contain at least one uppercase letter (A-Z).', verbose_name='Password must contain one uppercase letter'),
        ),
    ]
