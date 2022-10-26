from django.urls import path
from .views import CryoCartList, CryoCartListDetail
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [

    path("allCryoAsset/", CryoCartList.as_view(), name="cryoCart"),
    path('allCryoAsset/<int:pk>/', CryoCartListDetail.as_view(), name='cryo-update'),
]
    