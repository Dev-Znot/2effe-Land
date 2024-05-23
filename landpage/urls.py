from django.urls import path
from .views import landpage

app_name = "land"

urlpatterns = [
    path("", landpage, name="landpage"),
]
