from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    """Post data example from API
    {
        'userId': 1,
        'id': 1,
        'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit'
    }
    """

    user_id = models.BigIntegerField(default=99999942)
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return f"[{self.pk}] {self.title}"


class Comment(models.Model):
    """Comment data example from API
    {
        'postId': 1,
        'id': 1,
        'name': 'id labore ex et quam laborum',
        'email': 'Eliseo@gardner.biz',
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit'
    }
    """

    post_id = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"Comment {self.pk}: {self.name}"


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    from rest_framework.authtoken.models import Token

    if created:
        Token.objects.create(user=instance)
