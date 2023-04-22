# If you drop data you can run this to get the data back
python manage.py loaddata regions/seeds.json;
python manage.py loaddata jwt_auth/seeds.json;
python manage.py loaddata swim_sites/seeds.json;
python manage.py loaddata comments/seeds.json;