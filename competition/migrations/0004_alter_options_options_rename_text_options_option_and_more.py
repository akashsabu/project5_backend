# Generated by Django 5.0.1 on 2024-01-24 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='options',
            options={'verbose_name_plural': 'Options'},
        ),
        migrations.RenameField(
            model_name='options',
            old_name='text',
            new_name='option',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_choice',
        ),
        migrations.AlterModelTable(
            name='options',
            table='Competition_options',
        ),
    ]
