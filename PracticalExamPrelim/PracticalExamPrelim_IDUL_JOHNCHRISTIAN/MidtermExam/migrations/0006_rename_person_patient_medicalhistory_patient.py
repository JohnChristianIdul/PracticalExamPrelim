# Generated by Django 4.2.4 on 2023-09-18 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermExam', '0005_remove_medicalhistory_person_patient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalhistory',
            old_name='person_patient',
            new_name='patient',
        ),
    ]
