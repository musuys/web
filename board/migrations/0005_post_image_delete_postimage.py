# Generated by Django 4.0.5 on 2022-06-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]