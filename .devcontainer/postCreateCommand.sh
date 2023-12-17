echo "----> Installing Developer Requirements"
pip install -r requirements.txt

cp ./rindustest/.pg_service.conf $HOME
echo "----> Moved Postgres conf file to user home folder"


# docker exec -it rindus-test_devcontainer_db_1 bash
# psql -h localhost -U postgres
# create database rindusdb;
# \l