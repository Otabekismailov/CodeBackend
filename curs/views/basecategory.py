from curs.serializers import BaseCategoryserializers
from curs.models import BaseCategory
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class BaseCategoryListView(ListCreateAPIView):
    queryset = BaseCategory.objects.all()
    serializer_class = BaseCategoryserializers


class BaseCategoryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
    queryset = BaseCategory.objects.all()
    serializer_class = BaseCategoryserializers
