# Generated by Django 4.1.2 on 2022-12-05 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicity_db', '0016_remove_artist_age_artist_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='label_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicity_db.label'),
            preserve_default=False,
        ),
    ]
