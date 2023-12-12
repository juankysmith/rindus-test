echo "----> Installing Developer Requirements"
pip install -r requirements.txt

echo "----> Move Postgres conf file to /home/vscode/"
cp ./rindustest/.pg_service.conf /home/vscode/.

# docker exec -it rindus-test_devcontainer_db_1 bash
# psql -h localhost -U postgres
# create database rindusdb;
# \l