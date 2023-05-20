from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from courses import settings
from curs.views import BaseCategoryListView, BaseCategoryDetail
from curs.views.category import CategoryListView, CategoryDetailView

urlpatterns = [

    path('base/', BaseCategoryListView.as_view(), name='base-list'),
    path('base/<slug:slug>', BaseCategoryDetail.as_view(), name='base-detail'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
