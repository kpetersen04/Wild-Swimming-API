from jwt_auth.serializers.common import UserSerializer
from .common import FavoriteSerializer
from swim_sites.serializers.common import Swim_siteSerializer

class PopulatedFavoriteSerializer(FavoriteSerializer):
    created_by = UserSerializer()
    site = Swim_siteSerializer()