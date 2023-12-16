echo "----> Installing Developer Requirements"
pip install -r requirements.txt

echo "----> Move Postgres conf file to user home folder"
cp ./rindustest/.pg_service.conf $HOME

export DJANGO_SETTINGS_MODULE=rindustest.settings
django-admin runserver

# docker exec -it rindus-test_devcontainer_db_1 bash
# psql -h localhost -U postgres
# create database rindusdb;
# \l