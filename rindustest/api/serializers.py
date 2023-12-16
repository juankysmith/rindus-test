from rest_framework import serializers

from api.models import Post, Comment



class CommentsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return f"Comment {value.pk}: {value.name}"
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentsListingField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'comments']
            

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post_id', 'name', 'email', 'body']
        
