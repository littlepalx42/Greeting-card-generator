# Generated by Django 3.2 on 2024-10-21 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poster_templates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='image_template',
        ),
        migrations.AddField(
            model_name='template',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='poster_templates.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='greeting_cards',
            field=models.ImageField(default='abc', upload_to='greeting_cards/'),
            preserve_default=False,
        ),
    ]