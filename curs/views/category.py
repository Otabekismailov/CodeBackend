from rest_framework import status
from rest_framework.response import Response

from curs.serializers import BaseCategoryserializers, CategorySerializers
from curs.models import BaseCategory, Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    # def get_queryset(self):
    #     queryset = Category.objects.filter(basecategory__slug=self.kwargs[self.lookup_field])
    #     return queryset


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Category
    serializer_class = CategorySerializers
