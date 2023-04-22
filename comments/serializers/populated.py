from jwt_auth.serializers.common import UserSerializer
from .common import CommentSerializer

class PopulatedCommentsSerializer(CommentSerializer):
    created_by = UserSerializer()