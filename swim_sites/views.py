from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Swim_site
from .serializers.common import Swim_siteSerializer

class SwimSiteListView(APIView):
    def get(self, _request):
        swim_sites = Swim_site.objects.all()
        serialized_sites = Swim_siteSerializer(swim_sites, many=True)
        return Response(serialized_sites.data, status=status.HTTP_200_OK)

