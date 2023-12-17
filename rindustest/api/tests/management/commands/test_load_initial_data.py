from io import StringIO
from django.core.management import call_command
from django.db import IntegrityError
from django.test import TransactionTestCase


class CommandLoadInitialDataTest(TransactionTestCase):

    reset_sequences = True

    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "load_initial_data",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()
    
    def test_command_empty_database(self):
        from api.models import Post, Comment
        self.call_command()
        self.assertEqual(Post.objects.all().count(), 100)
        self.assertEqual(Comment.objects.all().count(), 500)

        with self.assertRaises(IntegrityError, msg='Posts already loaded in local database.'):
            self.call_command()
        self.assertEqual(Post.objects.all().count(), 100)
        self.assertEqual(Comment.objects.all().count(), 500)

        
