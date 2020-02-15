# Codics

This is my homework I created a store site.
I used Django as a web server and MySQL database.

## Installation


```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt-get install python3-dev
sudo apt-get install python3-dev libmysqlclient-dev
sudo apt-get install mysql-server
```

## Virtual env

```bash
pipi3 install virtualenv
mkdir python-virtual-environments && cd python-virtual-environments
python3 -m venv env
source env/bin/activate
```

## Installation python packages

```bash
pip install -r requerements.txt
```

##  Create the Database

```bash
mysql -u root -p
CREATE USER user;
CREATE DATABASE codics;
GRANT ALL PRIVILEGES ON codics.* TO 'user'@'%' WITH GRANT OPTION;
```

##  Run server

```bash
python manage.py migrate
python manage.py runserver (by default run localhost:8000)
```
