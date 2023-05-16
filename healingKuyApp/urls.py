from django.urls import path,re_path

from . import views

urlpatterns = [
    # user
    path('', views.index, name='index'),
    path('find_trip/', views.findTrip, name='find_trip'),
    path('scheduled_trip/', views.scheduledTrip, name='scheduled_trip'),
    path('login/', views.login, name='login'),

    # admin
     # admin url
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/trip_location/', views.tripLocation, name='trip_location'),
    path('dashboard/buses/', views.buses, name='buses'),
    path('dashboard/buses/add/', views.addBus, name='add_bus'),
    path('dashboard/trip_schedules/', views.tripSchedules, name='trip_schedules'),
    path('dashboard/booking/', views.booking, name='booking'),




    # api
    path('api/bus/', views.busApi, name='bus_api'),
    path('api/bus/delete/<int:id>', views.busApiDelete, name='bus_api_delete'),
    path('api/bus/update/<int:id>', views.busApiUpdate, name='bus_api_update'),
    path('api/location/', views.locationApi, name='location_api'),
    path('api/location/update/<int:id>', views.locationApiUpdate, name='location_api_update'),
    path('api/location/delete/<int:id>', views.locationApiDelete, name='location_api_delete'),
    re_path(r'^api/schedule/$', views.scheduleApi, name='schedule_api'),
    path('api/schedule/update/<int:id>', views.scheduleApiUpdate, name='schedule_api_update'),
    path('api/schedule/delete/<int:id>', views.scheduleApiDelete, name='schedule_api_delete'),
]