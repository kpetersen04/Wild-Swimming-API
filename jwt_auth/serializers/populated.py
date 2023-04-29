from jwt_auth.serializers.common import UserSerializer
from comments.serializers.common import CommentSerializer
from favorites.serializers.common import FavoriteSerializer

class PopulatedUserSerializer(UserSerializer):
    comments = CommentSerializer(many=True)
    favorites = FavoriteSerializer(many=True)