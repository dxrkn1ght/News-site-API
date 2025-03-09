from rest_framework import viewsets, response
from .models import New
from .serializers import NewSerializer


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
