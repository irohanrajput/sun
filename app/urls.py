from django.urls import path
from .views import getSunsetSunrise

urlpatterns = [
    path('', getSunsetSunrise)
]
