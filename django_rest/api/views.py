from rest_framework import viewsets
from django.contrib.auth.models import User,Group
from api.serializers import UserSerializer,GroupSerializer
from api.models import Event,Guest
from api.serializers import EventSerializer,GuestSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ API端口允许User查看或编辑 """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """API端口允许Groups查看或编辑"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
    ''' API端口允许Event查看或编辑'''
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GuestViewSet(viewsets.ModelViewSet):
    ''' API端口允许Guest查看或编辑'''
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
