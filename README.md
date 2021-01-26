# notice-connect
Django tech assessment for Notice Connect

To get started:

rm -rf env

python -m venv env

source env/bin/activate

pip install -r requirements.txt



python match/manage.py makemigrations match

python match/manage.py migrate

python match/manage.py loaddata match/match/fixtures/notices.json


python match/manage.py runserver
