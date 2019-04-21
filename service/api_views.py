from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination

from .models import ServiceInfo
from .serializers import ServiceSerializer


class ServicePagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3


class ServiceListView(ListAPIView):
    queryset = ServiceInfo.objects.all()
    lookup_field = 'virtual_service'
    serializer_class = ServiceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('virtual_service',)
    search_fields = ('virtual_service',)
    pagination_class = ServicePagination


class RetrieveServiceView(RetrieveAPIView):
    queryset = ServiceInfo.objects.all()
    lookup_field = 'virtual_service'
    serializer_class = ServiceSerializer


class AddServiceView(CreateAPIView):
    lookup_field = '__all__'
    serializer_class = ServiceSerializer


class DeleteServiceView(DestroyAPIView):
    queryset = ServiceInfo.objects.all()
    lookup_field = 'virtual_service'


class UpdateServiceView(UpdateAPIView):
    queryset = ServiceInfo.objects.all()
    lookup_field = 'virtual_service'
    serializer_class = ServiceSerializer


class RetrieveUpdateDestroyServiceView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceInfo.objects.all()
    lookup_field = 'virtual_service'
    serializer_class = ServiceSerializer


class RetrieveUpdateServiceView(RetrieveUpdateAPIView):
    queryset = ServiceInfo.objects.all()
    lookup_field = 'virtual_service'
    serializer_class = ServiceSerializer


class RetrieveDestroyServiceView(RetrieveDestroyAPIView):
    queryset = ServiceInfo.objects.all()
    lookup_field = 'virtual_service'
    serializer_class = ServiceSerializer
