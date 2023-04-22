from jwt_auth.serializers.common import UserSerializer
from comments.serializers.common import CommentSerializer

class PopulatedUserSerializer(UserSerializer):
    comments = CommentSerializer(many=True)