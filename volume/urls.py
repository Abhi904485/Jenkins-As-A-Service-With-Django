from django.urls import path

from .api_views import VolumeListView, RetrieveVolumeView, AddVolumeView, DeleteVolumeView, \
    UpdateVolumeView, RetrieveUpdateDestroyVolumeView, RetrieveDestroyVolumeView

urlpatterns = [
    path('volumes/', VolumeListView.as_view()),
    path('add_volume/', AddVolumeView.as_view()),
    path('<str:volume_name>/delete_volume/', DeleteVolumeView.as_view()),
    path('<str:volume_name>/update_volume/', UpdateVolumeView.as_view()),
    path('<str:volume_name>/', RetrieveUpdateDestroyVolumeView.as_view()),
    path('<str:volume_name>/rd', RetrieveDestroyVolumeView.as_view()),
    path('<str:volume_name>/ru', RetrieveUpdateDestroyVolumeView.as_view()),
    path('<str:volume_name>/rt', RetrieveVolumeView.as_view()),

]
