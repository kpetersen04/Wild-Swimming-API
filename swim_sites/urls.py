from django.urls import path
from .views import SwimSiteListView, SwimSiteDetailView

urlpatterns = [
    path('', SwimSiteListView.as_view()),
    path('<int:pk>/', SwimSiteDetailView.as_view())
]