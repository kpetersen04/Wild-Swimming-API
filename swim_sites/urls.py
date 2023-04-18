from django.urls import path
from .views import SwimSiteListView

urlpatterns = [
    path('', SwimSiteListView.as_view())
]