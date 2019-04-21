from django.urls import path

from .api_views import TeamListView, AddTeamView, DeleteTeamView, UpdateTeamView, RetrieveUpdateDestroyTeamView, \
    RetrieveDestroyTeamView, RetrieveUpdateTeamView, RetrieveTeamView

urlpatterns = [

    path('teams/', TeamListView.as_view()),
    path('add_team/', AddTeamView.as_view()),
    path('<str:team_name>/delete_team/', DeleteTeamView.as_view()),
    path('<str:team_name>/update_team/', UpdateTeamView.as_view()),
    path('<str:team_name>/', RetrieveUpdateDestroyTeamView.as_view()),
    path('<str:team_name>/rd', RetrieveDestroyTeamView.as_view()),
    path('<str:team_name>/ru', RetrieveUpdateTeamView.as_view()),
    path('<str:team_name>/rt', RetrieveTeamView.as_view()),
]
