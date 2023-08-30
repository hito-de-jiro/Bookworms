Bookworm
==
Digital library pet project using REST API and MySQL
--
## Stack
- Python 3.10
- MySQL
- Flask
- Docker
## Copy project
```
git clone https://github.com/hito-de-jiro/bookworms.git
```
## Preparation

Use the package manager [pip](https://pip.pypa.io/en/stable/).
Install virtual environment. You can use virtualenv.
```bash
pip install virualenv
virtualenv venv
```
Activate venv (windows):
```
venv\Scripts\activate.bat
```
## Build
Install dependencies of project

```bash
pip install -r requirements.txt
```
## Connect the database
The project uses a docker container with a MySQL server.
Instructions for installing the container [here](https://www.appsdeveloperblog.com/how-to-start-mysql-in-docker-container/).

A command that will create a mysql server with a database:
```bash
docker run -d -p 3306:3306 --name mysql-docker-container -e MYSQL_ROOT_PASSWORD=passw -e MYSQL_DATABASE=library -e MYSQL_USER=root -e MYSQL_PASSWORD=passw mysql/mysql-server:latest
```
Checking running containers:
```bash
docker container ls
```
If you need to stop the container:
```bash
docker stop <container_id>
```
The command to start the bush inside the container:
```bash
docker exec -it mysql-docker-container bash 
```
Check the database and create a database for tests:
```bash
mysql -uroot -ppassw
```
```mysql
SHOW DATABASES;
```
```mysql
CREATE DATABASE test_library;
```
Or use ready-made scripts to create databases:
```bash
source yourabolutpathtoproject\resources\create_db.sql
```
Run server:
```
python -m flask --app bookworm/app run
```
If you need to set up debug mode, run:
```
python -m flask --app bookworm/app run --debug
```
## Additionally
In the utils folder, the [fake_data_generator.py](utils/fake_data_generator.py) script can **RECREATE** a database with fake data.
You can choose any value in the range.

The project have a tests of API endpoints.
For tests, use the database created in docker, or create a test database using a ready-made script:
```bash
source yourabolutpathtoproject\resources\create_test_db.sql
```
Run tests:
```bash
pytest -svv
```
