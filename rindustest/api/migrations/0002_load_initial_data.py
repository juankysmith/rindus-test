from django.core.management import call_command
from django.db import migrations
from api.models import Post


def forward(apps, schema_editor):
    call_command('load_initial_data')


def backward(apps, schema_editor):
    Post.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [('api', '0001_initial')]

    operations = [migrations.RunPython(forward, backward)]
