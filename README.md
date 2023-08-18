Bookworm
==
Digital library educational project using REST API and MySQL
--
## Stack
- Python 3.10
- MySQL 8.0.33
- Flask
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
Use ready-made scripts to create a databases
```bash
source yourabolutpathtoproject\resources\create_db.sql
```
Run server:
```
python -m flask --app bookworm/app run
```
if you need to set up debug mode, run:
```
python -m flask --app bookworm/app run --debug
```
## Additionally
In the utils folder, the [fake_data_generator.py](utils/fake_data_generator.py) script can **RECREATE** a database with fake data.
You can choose any value in the range.

The project have a tests of API endpoints.
For tests, create a test database:
```bash
source yourabolutpathtoproject\resources\create_test_db.sql
```
Run tests:
```bash
pytest -svv
```
