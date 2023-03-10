# Generated by Django 4.1.6 on 2023-02-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0008_condition_locale_condition_original_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='gender',
            field=models.TextField(blank=True, null=True, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='healthy_volunteers',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='intervention_type',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='치료 타입'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
