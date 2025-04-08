from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.date} {self.time}"


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.item_name
