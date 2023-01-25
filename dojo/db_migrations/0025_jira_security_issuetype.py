# Generated by Django 2.2.4 on 2019-12-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0024_cve_fix_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jira_conf',
            name='default_issue_type',
            field=models.CharField(choices=[('Task', 'Task'), ('Story', 'Story'), ('Epic', 'Epic'), ('Spike', 'Spike'), ('Bug', 'Bug'), ('Security', 'Security')], default='Bug', max_length=9),
        ),
    ]
