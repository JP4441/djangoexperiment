# Generated by Django 4.0.3 on 2022-03-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]