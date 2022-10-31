from django.urls import path
from .views import CryoCartList, CryoCartListDetail, CryoCartUpdate, ImplemetationCryoCartUpdateWithAssetID, ImplementationCryoListCreateAPIView, ImplementationCryoRetrieveUpdateAPIView

urlpatterns = [

    #cryorelated information
    path(r"allCryoAsset/", CryoCartList.as_view(), name="cryoCart"),
    path(r'allCryoAsset/<int:pk>/', CryoCartListDetail.as_view(), name='cryo-update'),
    path(r'allCryoAssetUpdate/<slug:assetID>/', CryoCartUpdate, name='cryo-update-new'),

    #all the cryo's implementation related information 

    path(r"allNewCryoAssetImplemetation/<str:assetID>", ImplemetationCryoCartUpdateWithAssetID.as_view(), name="newimplementationCryoCart"),
    path(r"allCryoAssetImplemetation/", ImplementationCryoListCreateAPIView.as_view(), name="implementationCryoCart"),
    path(r'allImplementationCryoCart/<int:pk>/', ImplementationCryoRetrieveUpdateAPIView.as_view(), name="allimplementationCryoCartUpdate"),
]
    