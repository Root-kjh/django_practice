# Generated by Django 4.1.6 on 2023-02-25 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0011_study_original_data_hash'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='study',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='eligibility',
            name='original_eligibility',
        ),
        migrations.RemoveField(
            model_name='intervention',
            name='original_intervention',
        ),
        migrations.AddField(
            model_name='eligibility',
            name='clone_from_eligibility',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cloned_eligibility', to='studies.eligibility', verbose_name='복제 원본 선정조건(eligibility) 고유번호'),
        ),
        migrations.AddField(
            model_name='eligibility',
            name='translate_from_eligibility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translated_eligibilities', to='studies.eligibility', verbose_name='번역 원본 선정조건(eligibility) 고유번호'),
        ),
        migrations.AddField(
            model_name='intervention',
            name='clone_from_intervention',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cloned_intervention', to='studies.intervention', verbose_name='복제 원본 의약품(intervention) 고유번호'),
        ),
        migrations.AddField(
            model_name='intervention',
            name='translate_from_intervention',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translated_interventions', to='studies.intervention', verbose_name='번역 원본 의약품(intervention) 고유번호'),
        ),
        migrations.AddField(
            model_name='study',
            name='clone_from_study',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cloned_study', to='studies.study', verbose_name='복제 원본 임상연구(study) 고유번호'),
        ),
        migrations.AddField(
            model_name='study',
            name='translate_from_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translated_studies', to='studies.study', verbose_name='번역 원본 임상연구(study) 고유번호'),
        ),
        migrations.AlterUniqueTogether(
            name='study',
            unique_together={('translate_from_study', 'locale')},
        ),
        migrations.RemoveField(
            model_name='study',
            name='original_study',
        ),
    ]
