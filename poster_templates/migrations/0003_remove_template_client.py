# Generated by Django 3.2 on 2024-10-24 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poster_templates', '0002_auto_20241021_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='client',
        ),
    ]
