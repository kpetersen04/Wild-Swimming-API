from regions.serializers.common import RegionSerializer
from swim_sites.serializers.common import Swim_siteSerializer

class PopulatedRegionSerializer(RegionSerializer):
    swim_sites = Swim_siteSerializer(many=True)
