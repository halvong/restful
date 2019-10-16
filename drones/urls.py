from drones import views
from django.urls import path, re_path

urlpatterns = [
    path('drone-categories/', views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
    re_path(r'^drone-categories/(?P<pk>[0-9]+)$', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
    path('drones/', views.DroneList.as_view(), name=views.DroneList.name),
    re_path(r'^drones/(?P<pk>[0-9]+)$', views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path('pilots/', views.PilotList.as_view(), name=views.PilotList.name),
    re_path(r'^pilots/(?P<pk>[0-9]+)$', views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path('competitions/', views.CompetitionList.as_view(), name=views.CompetitionList.name),
    re_path(r'^competitions/(?P<pk>[0-9]+)$', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
