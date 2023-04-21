from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Swim_site
from .serializers.common import Swim_siteSerializer

class SwimSiteListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get(self, _request):
        swim_sites = Swim_site.objects.all()
        serialized_sites = Swim_siteSerializer(swim_sites, many=True)
        return Response(serialized_sites.data, status=status.HTTP_200_OK)
    
class SwimSiteDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_swim_site(self, pk):
        try: 
            return Swim_site.objects.get(pk=pk)
        except Swim_site.DoesNotExist:
            raise NotFound(detail="no swim site with that code can be found")

    def get(self, _request, pk):
        swim_site = self.get_swim_site(pk=pk)
        serialized_swim_site = Swim_siteSerializer(swim_site)
        return Response(serialized_swim_site.data, status=status.HTTP_200_OK)
