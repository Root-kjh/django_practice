# Generated by Django 4.1.6 on 2023-02-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0010_study_control_status_type_study_original_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='original_data_hash',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='original_data sha256 hash'),
        ),
    ]
