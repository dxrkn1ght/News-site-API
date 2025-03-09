from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import New
from .serializers import NewSerializer


class NewViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = New.objects.all()
        serializer = NewSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        new = get_object_or_404(New, pk=pk)
        serializer = NewSerializer(new)
        return Response(serializer.data)

    def update(self, request, pk=None):
        new = get_object_or_404(New, pk=pk)
        serializer = NewSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        new = get_object_or_404(New, pk=pk)
        new.delete()
        return Response(status=204)