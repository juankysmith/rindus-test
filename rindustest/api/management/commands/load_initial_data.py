from django.db import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from requests import get

from api.models import Comment, Post



class Command(BaseCommand):
    help = "Load Comments and Posts from jsonplaceholder."
    
    def handle(self, *args, **options):
        try:
            posts_dict = self._load_posts()
            self._load_comments(posts_dict)
        except CommandError:
            print("Command load_intial_data failed.")
            raise


    def _load_posts(self) -> dict:
        posts_dict = {}
        response = get(f'https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            fields = [field.name for field in Post._meta.get_fields()]
            try:
                posts = Post.objects.bulk_create(
                    [
                        Post(**{field: element[self._to_camel(field)] 
                            for field in fields if self._to_camel(field) in element}) 
                            for element in response.json()
                    ]
                )
                posts_dict = {post.id : post for post in posts}
            except IntegrityError:
                print(f'Posts already loaded in local database.')

        return posts_dict

    def _to_camel(self, st: str) -> str:
        title_str = ''.join(x for x in st.title() if x.isalnum())
        return title_str[0].lower() + title_str[1:]

    def _load_comments(self, posts_dict: dict = None) -> None:
        response = get(f'https://jsonplaceholder.typicode.com/comments')
        if response.status_code == 200:
            try:
                if not posts_dict:
                    posts_dict = {post.id : post for post in Post.objects.all()}
                Comment.objects.bulk_create(
                    [
                        Comment(
                            name=element['name'], 
                            id=element['id'], 
                            email=element['email'],
                            body=element['body'],
                            post_id=posts_dict[element['postId']]
                        ) for element in response.json()
                    ]
                )
            except IntegrityError:
                print(f'Comments already loaded in local database.')
