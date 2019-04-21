from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination

from .models import TeamInfo
from .serializers import TeamSerializer


class TeamPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3


class TeamListView(ListAPIView):
    queryset = TeamInfo.objects.all()
    lookup_field = 'team_name'
    serializer_class = TeamSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('team_name',)
    search_fields = ('team_name',)
    pagination_class = TeamPagination


class RetrieveTeamView(RetrieveAPIView):
    queryset = TeamInfo.objects.all()
    lookup_field = 'team_name'
    serializer_class = TeamSerializer


class AddTeamView(CreateAPIView):
    lookup_field = 'team_name'
    serializer_class = TeamSerializer


class DeleteTeamView(DestroyAPIView):
    queryset = TeamInfo.objects.all()
    lookup_field = 'team_name'


class UpdateTeamView(UpdateAPIView):
    queryset = TeamInfo.objects.all()
    lookup_field = 'team_name'
    serializer_class = TeamSerializer


class RetrieveUpdateDestroyTeamView(RetrieveUpdateDestroyAPIView):
    queryset = TeamInfo.objects.all()
    lookup_field = 'team_name'
    serializer_class = TeamSerializer


class RetrieveUpdateTeamView(RetrieveUpdateAPIView):
    queryset = TeamInfo.objects.all()
    lookup_field = 'team_name'
    serializer_class = TeamSerializer


class RetrieveDestroyTeamView(RetrieveDestroyAPIView):
    queryset = TeamInfo.objects.all()
    lookup_field = 'team_name'
    serializer_class = TeamSerializer
