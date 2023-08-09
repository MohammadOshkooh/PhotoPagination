from django.urls import path
from .views import ImageListView

urlpatterns = [
    path('photo/', ImageListView.as_view(), name='photo-list')
]