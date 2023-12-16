
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models import Post, Comment
from api.serializers import CommentSerializer, PostSerializer
from api.authentication import BearerAuthentication


class PostViewSet(ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by("id")
    serializer_class = PostSerializer
    authentication_classes=[BearerAuthentication]
    permission_classes = [IsAuthenticated]


class CommentViewSet(ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by("id")
    serializer_class = CommentSerializer
    authentication_classes=[BearerAuthentication]
    permission_classes = [IsAuthenticated]
