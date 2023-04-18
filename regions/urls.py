from django.urls import path
from .views import RegionListVIew, RegionDetailView

urlpatterns = [
    path('', RegionListVIew.as_view()), 
    path('<int:pk>/', RegionDetailView.as_view())
]