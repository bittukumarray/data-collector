from django.urls import path, include
from .views import *


urlpatterns = [
    path('insert', InsertData.as_view()),
    path('query', QueryData.as_view()),
]