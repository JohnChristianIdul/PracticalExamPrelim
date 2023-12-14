from django.db import models


# Create your models here.
class Person(models.Model):
    PID = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=50, null=False)
    Lname = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.Fname

class Doctor(Person):
    Specialty = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.Fname

class Patient(Person):
    attending_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.Fname

class Procedure(models.Model):
    Procedure_Core = models.IntegerField(primary_key=True)
    Procedure_Name = models.CharField(max_length=50, null=False)
    Cost = models.IntegerField()

    def __str__(self):
        return str(self.Procedure_Name)

class MedicalHistory(models.Model):
    proceed = models.ManyToManyField(Procedure, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class DocToProcedure(models.Model):
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, related_name="procedure_done", on_delete=models.CASCADE)
    TimeOfProcedure = models.TimeField()
    DateOfProcedure = models.DateField()

    def __str__(self):
        return str(self.DateOfProcedure) + " " + str(self.TimeOfProcedure)

