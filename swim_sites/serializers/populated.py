from regions.serializers.common import RegionSerializer
from swim_sites.serializers.common import Swim_siteSerializer
from comments.serializers.common import CommentSerializer

class PopulatedSwim_siteSerializer(Swim_siteSerializer):
    region = RegionSerializer()
    comments = CommentSerializer(many=True)