from django.urls import path
from cars.views import *


urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarlistView.as_view()),
    path('car/detail/<int:pk>', CarDeleteView.as_view())
]