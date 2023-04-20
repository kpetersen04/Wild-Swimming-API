from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Region
from .serializers.common import RegionSerializer

class RegionListVIew(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get(self, _request):
        regions = Region.objects.all()
        print(regions)
        serialized_regions = RegionSerializer(regions, many=True)
        print(serialized_regions.data)
        return Response(serialized_regions.data, status=status.HTTP_200_OK)
    
class RegionDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # function used to get the region with the matched primary key 
    def get_region(self, pk):
        try: 
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise NotFound(detail="No region with that name can be found.")

    def get(self, _request, pk):
        region = self.get_region(pk=pk)
        serialized_region = RegionSerializer(region)
        return Response(serialized_region.data, status=status.HTTP_200_OK)
    
