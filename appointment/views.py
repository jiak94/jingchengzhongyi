from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Appointment, TimeSlot
import datetime

# Create your views here.
def index(request):
    return render(request, 'appointment/welcome.html')


def doctors(request):
    doctors = Doctor.objects.all()
    context = {
        "doctors": doctors
    }
    return render(request, 'appointment/doctors.html', context)


def timeslot(request, doctor_id):
    time_slot = TimeSlot.objects.all().filter(
        doctor= doctor_id,
        date__gte=datetime.date.today(),
        remaining__gt=0
    )
    doctor = Doctor.objects.get(id=doctor_id)

    context = {
        'slots': time_slot,
        'doctor': doctor
    }
    # response = "You are looking at the time slot of doctor %s"
    # return HttpResponse(response % doctor_id)
    return render(request, 'appointment/book.html', context)


def reserve(request):
    if request.method == 'POST':
        request_obj = request.POST
        #create appointment per request
        slot_id = request_obj['slot_id']
        # patient_firstname = request_obj['patient_firstname']
        # patient_lastname = request_obj['patient_lastname']
        patient_name = request_obj['patient_name']
        gender = request_obj['gender']
        contact_number = request_obj['contact_number']

        time_slot_instance = TimeSlot.objects.get(id=slot_id)

        remaining = time_slot_instance.remaining

        if remaining <= 0:
            return render(request, 'appointment/fail.html')
        else:
            time_slot_instance.remaining -= 1
            time_slot_instance.save()

        appointment = Appointment(timeslot=time_slot_instance,
                                                patient_name=patient_name,
                                                gender=gender,
                                                contact_number=contact_number)
        appointment.save()
        print(appointment)
        return render(request, 'appointment/success.html')
    else:
        return doctors(request)
