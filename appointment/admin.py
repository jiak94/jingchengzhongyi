from django.contrib import admin
from .models import Doctor, Fee, Appointment, TimeSlot
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Fee)
admin.site.register(Appointment)
admin.site.register(TimeSlot)
