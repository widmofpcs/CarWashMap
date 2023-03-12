from django.http import Http404
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from washes.models import CarWash
from washes.serializers import WashesSerializer


class WashList(APIView):
    def get(self, request, format=None):
        washes = CarWash.objects.all()
        serializer = WashesSerializer(washes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WashesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WashDetail(APIView):
    def get_object(self, pk):
        try:
            return CarWash.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        wash = self.get_object(pk)
        serializer = WashesSerializer(wash, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        wash = self.get_object(pk)
        serializer = WashesSerializer(wash, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        wash = self.get_object(pk)
        wash.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)