from django.urls import path
from . import views
urlpatterns = [
    path('',views.time_changes,name="time_changes")
]
