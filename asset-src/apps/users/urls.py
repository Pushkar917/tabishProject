from django.urls import path
from .views import UserAPIView


urlpatterns = [

    path("all/", UserAPIView.as_view(), name="userapiview"),
   
]