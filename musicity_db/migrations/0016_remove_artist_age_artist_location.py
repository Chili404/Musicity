# Generated by Django 4.1.2 on 2022-12-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicity_db', '0015_label_remove_artist_location_artist_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='age',
        ),
        migrations.AddField(
            model_name='artist',
            name='location',
            field=models.CharField(default='USA', max_length=100),
            preserve_default=False,
        ),
    ]
