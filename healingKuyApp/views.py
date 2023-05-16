from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from .models import Schedule, Bus, Location, Booking
from .serializers import ScheduleSerializer, BusSerializer, LocationSerializer, BookingSerializer
from .form import BusForm
from .urls import path

# Create your views here.
# user
def index(request):
    return render(request, 'healingKuyApp/index.html')

def findTrip(request):
    context = {
        'title' : 'find_trip',
        'locations': Location.objects.all()
    }
    return render(request, 'healingKuyApp/find_trip.html', context)    

def scheduledTrip(request):

    context = {
        'title' : 'scheduled_trip',
        'schedules' : requests.get('http://127.0.0.1:2000/api/schedule', verify=False).json,
    }
    return render(request, 'healingKuyApp/scheduled_trip.html', context)

def login(request):
    context = {
        'title' : 'login'
    }
    return render(request, 'healingKuyApp/login.html', context) 


# admin
def dashboard(request):
    context = {
        'title' : 'dashboard'
    }
    return render(request, 'healingKuyApp/admin/index.html', context)

def tripLocation(request):
    if request.method == 'POST':
        # data = {"location": "medan", "status": "1"}
        r = requests.post('http://127.0.0.1:2000/api/location/', json=request.POST)

    context = {
        'title' : 'trip_location',
        'locations' :  requests.get('http://127.0.0.1:2000/api/location', verify=False).json(),
    }
    return render(request, 'healingKuyApp/admin/trip_location.html', context)

def buses(request):
    if request.method == 'POST':
        r = requests.post('http://127.0.0.1:2000/api/bus/', json=request.POST)

    context = {
        'title' : 'buses',
        'buses' : requests.get('http://127.0.0.1:2000/api/bus', verify=False).json
    }
    return render(request, 'healingKuyApp/admin/buses.html', context)

def addBus(request):
    form = BusForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
   

def tripSchedules(request):
    if request.method == 'POST':
        r = requests.post('http://127.0.0.1:2000/api/schedule/', json=request.POST)
        

    context = { 
        'title' : 'trip_schedules',
        'tripSchedules': requests.get('http://127.0.0.1:2000/api/schedule', verify=False).json,
        'buses': requests.get('http://127.0.0.1:2000/api/bus', verify=False).json,
        'locations': requests.get('http://127.0.0.1:2000/api/location', verify=False).json(),
       
    }
    return render(request, 'healingKuyApp/admin/trip_schedules.html', context)

def booking(request):
    context = {
        'title' : 'booking'
    }
    return render(request, 'healingKuyApp/admin/booking.html', context)




# api request
@csrf_exempt
def busApi(request):
    if request.method == 'GET':
        bus = Bus.objects.all()
        bus_serializer = BusSerializer(bus,many=True)
        return JsonResponse(bus_serializer.data, safe=False)
    elif request.method == 'POST':
        bus_data = JSONParser().parse(request)
        bus_serializer = BusSerializer(data=bus_data)
        if bus_serializer.is_valid():
            bus_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

@csrf_exempt
def busApiUpdate(request, id=0):
    bus_data =JSONParser().parse(request)
    bus = Bus.objects.get(bus_id=id)
    bus_serializer = BusSerializer(bus,data=bus_data)
    if bus_serializer.is_valid():
        bus_serializer.save()
        return JsonResponse("Update Successfully", safe=False)
    return JsonResponse("Failed to update", safe=False)

@csrf_exempt
def busApiDelete(request, id=0): 
    bus= Bus.objects.get(bus_id=id)
    bus.delete()
    return redirect(buses)

@csrf_exempt
def locationApi(request):
    if request.method == 'GET':
        location = Location.objects.all()
        location_serializer = LocationSerializer(location,many=True)
        return JsonResponse(location_serializer.data, safe=False)
    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        location_serializer = LocationSerializer(data=location_data)
        if location_serializer.is_valid():
            location_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to add", safe=False)        

@csrf_exempt
def locationApiUpdate(request, id=0):
    location_data = JSONParser().parse(request)
    location = Location.objects.get(location_id=id)
    location_serializer = LocationSerializer(location,data=location_data)
    if location_serializer.is_valid():
        location_serializer.save()
        return JsonResponse("Update Successfully",safe=False)
    return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def locationApiDelete(request,id=0):
    location = Location.objects.get(location_id=id)
    location.delete()
    return redirect(tripLocation)

@csrf_exempt
def scheduleApi(request):
    if request.method == 'GET':
        schedule = Schedule.objects.all()
        schedule_serializer = ScheduleSerializer(schedule,many=True)
        return JsonResponse(schedule_serializer.data, safe=False)
    elif request.method == 'POST':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = ScheduleSerializer(data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
@csrf_exempt
def scheduleApiUpdate(request, id=0):
    schedule_data = JSONParser().parse(request)
    schedule = Schedule.objects.get(schedule_id=id)
    schedule_serializer = ScheduleSerializer(schedule,data=schedule_data)
    if schedule_serializer.is_valid():
        schedule_serializer.save()
        return JsonResponse("Update Successfully", safe=False)
    return JsonResponse("Failde to update", safe=False)

@csrf_exempt
def scheduleApiDelete(request, id=0):
    schedule = Schedule.objects.get(schedule_id=id)
    schedule.delete()
    return redirect(tripSchedules)