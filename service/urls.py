from django.urls import path

from .api_views import ServiceListView, RetrieveServiceView, AddServiceView, DeleteServiceView, \
    UpdateServiceView, RetrieveUpdateDestroyServiceView, RetrieveDestroyServiceView

urlpatterns = [
    path('services/', ServiceListView.as_view()),
    path('add_service/', AddServiceView.as_view()),
    path('<str:virtual_service>/delete_service/', DeleteServiceView.as_view()),
    path('<str:virtual_service>/update_service/', UpdateServiceView.as_view()),
    path('<str:virtual_service>/', RetrieveUpdateDestroyServiceView.as_view()),
    path('<str:virtual_service>/rd', RetrieveDestroyServiceView.as_view()),
    path('<str:virtual_service>/ru', RetrieveUpdateDestroyServiceView.as_view()),
    path('<str:virtual_service>/rt', RetrieveServiceView.as_view()),

]
