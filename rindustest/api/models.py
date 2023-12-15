from django.db import models

class Post(models.Model):
    """Post data example from API 
        {
            'userId': 1, 
            'id': 1, 
            'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 
            'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit'
        }
    """
    user_id = models.IntegerField()
    title = models.CharField(max_length=300)
    body = models.TextField()

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
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    body = models.TextField()