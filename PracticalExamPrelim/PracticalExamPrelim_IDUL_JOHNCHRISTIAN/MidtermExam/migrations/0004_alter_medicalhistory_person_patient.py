# Generated by Django 4.2.4 on 2023-09-18 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermExam', '0003_alter_medicalhistory_person_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='person_patient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MidtermExam.patient'),
        ),
    ]