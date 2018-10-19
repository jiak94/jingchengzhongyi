from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, Appointment, TimeSlot
import datetime

# Create your views here.
def index(request):
    return render(request, 'appointment/welcome.html')


def doctors(request):
    doctors = Doctor.objects.all()
    print(len(doctors))
    # return HttpResponse("Looking at Doctor's List")
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


def booking(request, timeslot_id):
    if request.mothod == 'POST':
        request_obj = request.POST
        #create appointment per request
        patient_firstname = request_obj['patient_firstname']
        patient_lastname = request_obj['patient_lastname']
        gender = request_obj['gender']
        contact_number = request_obj['contact_number']

        appointment = Appointment.object.create(time_slot=timeslot_id,
                                                patient_first_name=patient_firstname,
                                                patient_last_name=patient_lastname,
                                                gender=gender,
                                                contact_number=contact_number)
        print(appointment)
    else:
        response = "You are booking appointment for %s"
        return HttpResponse(response % timeslot_id)
