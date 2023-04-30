from jwt_auth.serializers.common import UserSerializer
from comments.serializers.common import CommentSerializer
from favorites.serializers.populated import PopulatedFavoriteSerializer

class PopulatedUserSerializer(UserSerializer):
    comments = CommentSerializer(many=True)
    favorites = PopulatedFavoriteSerializer(many=True)