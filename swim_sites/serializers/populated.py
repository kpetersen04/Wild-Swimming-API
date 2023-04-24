from regions.serializers.common import RegionSerializer
from swim_sites.serializers.common import Swim_siteSerializer
from comments.serializers.populated import PopulatedCommentsSerializer

class PopulatedSwim_siteSerializer(Swim_siteSerializer):
    region = RegionSerializer()
    comments = PopulatedCommentsSerializer(many=True)