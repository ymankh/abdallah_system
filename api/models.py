from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Session(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    payment_status = models.CharField(max_length=50)
    session_given = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.child.name} with {self.doctor.name} on {self.date} at {self.time}"
