# Generated by Django 2.2.7 on 2021-02-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210228_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='song',
            field=models.FileField(max_length=500, upload_to='song/'),
        ),
    ]
