# Generated by Django 5.0.1 on 2024-01-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0004_alter_options_options_rename_text_options_option_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='option',
            field=models.TextField(max_length=250),
        ),
    ]
