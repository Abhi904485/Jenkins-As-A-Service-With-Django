# from django_filters import FilterSet
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import action
# from rest_framework.response import Response
#
# from .models import TeamInfo
# from rest_framework import viewsets, status
#
#
# class TeamFilterSet(FilterSet):
#     class Meta:
#         model = TeamInfo
#         fields = ['team_name', ]
#
#
# class TeamViewSet(viewsets.ViewSet):
#     filter_backends = (DjangoFilterBackend,)
#     filter_class = TeamFilterSet
#
#     @action(detail=True, methods=['post'])
#     def add_team(self, request):
#         team_name = request.post.get('team_name')
#         try:
#             TeamInfo.objects.create(team_name=team_name)
#             return Response("Team Created!", status=status.HTTP_201_CREATED)
#
#         except Exception as ex:
#             return Response(ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     @action(detail=True, methods=['get'])
#     def get_team(self, request):
#         return Response(TeamInfo.objects.all().values(), status=status.HTTP_200_OK)
