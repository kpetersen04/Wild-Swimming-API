# run this in the terminal to create seed files for our data
python manage.py dumpdata regions --output regions/seeds.json --indent=2;
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;
python manage.py dumpdata swim_sites --output swim_sites/seeds.json --indent=2;
python manage.py dumpdata comments --output comments/seeds.json --indent=2;