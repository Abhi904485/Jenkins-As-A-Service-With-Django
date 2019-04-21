from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import VolumeInfo

from .serializers import VolumeSerializer


class VolumePagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3


class VolumeListView(ListAPIView):
    queryset = VolumeInfo.objects.all()
    lookup_field = 'volume_name'
    serializer_class = VolumeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('volume_name',)
    search_fields = ('volume_name',)
    pagination_class = VolumePagination


class RetrieveVolumeView(RetrieveAPIView):
    queryset = VolumeInfo.objects.all()
    lookup_field = 'volume_name'
    serializer_class = VolumeSerializer


class AddVolumeView(CreateAPIView):
    lookup_field = 'volume_name'
    serializer_class = VolumeSerializer

    # def create(self, request, *args, **kwargs):
    #     try:
    #         volume_name = request.data.get('volume_name')
    #         regex_string = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    #         regex_number = re.compile('[0-9]')
    #         if regex_string.search(volume_name) or regex_number.search(volume_name):
    #             raise ValidationError({'Volume Name': 'Volume name Should not contain digits or special symbols'})
    #     except ValueError:
    #         raise ValidationError({'Volume Name': 'Volume name length should not more than 100 characters'})
    #     return super().create(request, *args, **kwargs)


class DeleteVolumeView(DestroyAPIView):
    queryset = VolumeInfo.objects.all()
    lookup_field = 'volume_name'

    # def delete(self, request, *args, **kwargs):
    #     volume_name = request.data.get('volume_name')
    #     response = super().delete(request, *args, **kwargs)
    #     if response.status_code == 204:
    #         from django.core.cache import cache
    #         cache.delete('team_data_'.format(volume_name))
    #     return response


class UpdateVolumeView(UpdateAPIView):
    queryset = VolumeInfo.objects.all()
    lookup_field = 'volume_name'
    serializer_class = VolumeSerializer


class RetrieveUpdateDestroyVolumeView(RetrieveUpdateDestroyAPIView):
    queryset = VolumeInfo.objects.all()
    lookup_field = 'volume_name'
    serializer_class = VolumeSerializer


class RetrieveUpdateVolumeView(RetrieveUpdateAPIView):
    queryset = VolumeInfo.objects.all()
    lookup_field = 'volume_name'
    serializer_class = VolumeSerializer


class RetrieveDestroyVolumeView(RetrieveDestroyAPIView):
    queryset = VolumeInfo.objects.all()
    lookup_field = 'volume_name'
    serializer_class = VolumeSerializer
