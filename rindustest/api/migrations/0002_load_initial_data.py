from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management import call_command
from django.db import migrations
from api.models import Post


def forward(apps, schema_editor):
    call_command("load_initial_data")
    user = User.objects.create(username="rindus", last_login = timezone.now())
    user.set_password("rindus")
    user.save()


def backward(apps, schema_editor):
    Post.objects.filter(id__lte=100).delete()
    try:
        User.objects.get(username="rindus").delete()
    except User.DoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [("api", "0001_initial")]

    operations = [migrations.RunPython(forward, backward)]
