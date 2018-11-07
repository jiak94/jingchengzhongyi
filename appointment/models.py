from django.db import models

class Doctor(models.Model):
    image = models.FileField(upload_to='upload/')
    description = models.TextField()
    advantages = models.TextField()
    occupation = models.CharField(blank=False, max_length=50)
    firstname = models.CharField(blank=False, max_length=5)
    lastname = models.CharField(blank=False, max_length=5)

    def __str__(self):
        return ('%s %s' % (self.lastname, self.firstname))



class Fee(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=20, decimal_places=2,
                              blank=False, unique=True,
                              default=0)

    def __str__(self):
        return (str(self.fee))

class TimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    remaining = models.IntegerField(blank=False)

    def __str__(self):
        name = self.doctor.lastname + self.doctor.firstname
        return ('%s From %s to %s' % (name, self.start_time, self.end_time))

class Appointment(models.Model):
    #patient_first_name = models.CharField(blank=False, max_length=5)
    #patient_last_name = models.CharField(blank=False, max_length=5)
    patient_name = models.CharField(blank=False, max_length=5)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    GENDER_CHOICE = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE,
                              default='M', blank=False)

    contact_number = models.CharField(max_length=11, blank=False)

    def __str__(self):
        return ('%s %s' % (self.patient_name % self.contact_number))
