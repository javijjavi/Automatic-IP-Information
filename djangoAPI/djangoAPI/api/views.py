from django.contrib.auth.models import User, User
from rest_framework import viewsets
#from djangoAPI.djangoAPI.api.serializers import IPSSerializer, IPSerializer
@api_view(['GET','POST'])
class IPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = IPSerializer


class IPSViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = IPSSerializer