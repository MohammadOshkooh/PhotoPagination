from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5


class ImageListView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    pagination_class = CustomPageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page, many=True)

        data = {
            "Data": serializer.data,
            "Meta": {
                "statusCode": 200,
                "error": "success"
            }
        }
        return self.get_paginated_response(data)
