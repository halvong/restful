from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
from drones.serializers import DroneCategorySerializer
from drones.serializers import DroneSerializer
from drones.serializers import PilotSerializer
from drones.serializers import PilotCompetitionSerializer
from rest_framework import permissions
from drones import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, rest_framework as filters

class DroneCategoryList(generics.ListCreateAPIView):
    name = 'dronecategory-list'
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer

    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'dronecategory-detail'
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer

class DroneList(generics.ListCreateAPIView):
    name = 'drone-list'
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    filter_fields = ('name', 'drone_category', 'manufacturing_date', 'has_it_competed', )
    search_fields = ('^name',)
    ordering_fields = ('name', 'manufacturing_date',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custompermission.IsCurrentUserOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'drone-detail'
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )


class PilotList(generics.ListCreateAPIView):
    name = 'pilot-list'
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

    filter_fields = ('name', 'gender', 'races_count',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'races_count')

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'pilot-detail'
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CompetitionFilter(filters.FilterSet):
    from_achievement_date = DateTimeFilter(field_name='distance_achievement_date', lookup_expr='gte')
    to_achievement_date = DateTimeFilter(field_name='distance_achievement_date', lookup_expr='lte')
    min_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='gte')
    max_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='lte')
    drone_name = AllValuesFilter(field_name='drone__name')
    pilot_name = AllValuesFilter(field_name='pilot__name')

    class Meta:
        model = Competition
        fields = ('distance_in_feet', 'from_achievement_date', 'to_achievement_date', 'min_distance_in_feet', 'max_distance_in_feet',
                # drone__name will be accessed as drone_name
                'drone_name',
                # pilot__name will be accessed as pilot_name
                'pilot_name',
                )

class CompetitionList(generics.ListCreateAPIView):
    name = 'competition-list'
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    filter_class = CompetitionFilter
    ordering_fields = ('distance_in_feet', 'distance_achievement_date', )

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'competition-detail'
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer

#---
class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get(self, request, *args, **kwargs):

        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
        })
