Django Restful Web Services, Packtpub
10/17, Thurs

chp9
PG271, Versioning

#create user
tom:tom
b3664d4c107f627dfad4568a62271c206037869d

hal:hal
03a6e11bcb09426abbeb02a3458a37e4fa1e674d

#postgresql
docker-compose exec database psql --username=tom --dbname=drones --command="SELECT id FROM auth_user WHERE username = 'djangosuper';"

#
curl -iX GET http://localhost:8000/pilots/ -H "Authorization: Token 03a6e11bcb09426abbeb02a3458a37e4fa1e674d"


#
curl -X GET localhost:8000/toys/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Quadcopter"}' localhost:8000/drone-categories/

http POST :8000/drones/ name="WonderDrone" drone_category="Quadcopter" manufacturing_date="2017-07-20T02:02:00.716312Z" has_it_competed=false
http POST :8000/drones/ name="Atom" drone_category="Quadcopter" manufacturing_date="2017-08-18T02:02:00.716312Z" has_it_competed=false
curl -iX POST -H "Content-Type: application/json" -d '{"name":"WonderDrone", "drone_category":"Quadcopter", "manufacturing_date": "2017-07-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Atom", "drone_category":"Quadcopter", "manufacturing_date": "2017-08-18T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/

#drones
http POST :8000/drones/ name="Noisy Drone" drone_category="Octocopter" manufacturing_date="2017-10-23T02:03:00.716312Z" has_it_competed=false
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Noisy Drone", "drone_category":"Octocopter", "manufacturing_date": "2017-10-23T02:03:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/

#pilots
http POST :8000/pilots/ name="Penelope Pitstop" gender="F" races_count=0
http POST :8000/pilots/ name="Peter Perfect" gender="M" races_count=0
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Penelope Pitstop", "gender":"F", "races_count": 0}' localhost:8000/pilots/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Peter Perfect", "gender":"M", "races_count": 0}' localhost:8000/pilots/

#competitions
http POST :8000/competitions/ distance_in_feet=800 distance_achievement_date="2017-10-20T05:03:20.776594Z" pilot="Penelope Pitstop" drone="Atom"
http POST :8000/competitions/ distance_in_feet=2800 distance_achievement_date="2017-10-21T06:02:23.776594Z" pilot="Penelope Pitstop" drone="WonderDrone"
http POST :8000/competitions/ distance_in_feet=790 distance_achievement_date="2017-10-20T05:43:20.776594Z" pilot="Peter Perfect" drone="Atom"

curl -iX POST -H "Content-Type: application/json" -d '{"distance_in_feet":"800", "distance_achievement_date":"2017-10-20T05:03:20.776594Z", "pilot":"Penelope Pitstop", "drone":"Atom"}' localhost:8000/competitions/
curl -iX POST -H "Content-Type: application/json" -d '{"distance_in_feet":"2800", "distance_achievement_date":"2017-10-21T06:02:23.776594Z", "pilot":"Penelope Pitstop", "drone":"WonderDrone"}' localhost:8000/competitions/
curl -iX POST -H "Content-Type: application/json" -d '{"distance_in_feet":"790", "distance_achievement_date":"2017-10-20T05:43:20.776594Z", "pilot":"Peter Perfect", "drone":"Atom"}' localhost:8000/competitions/

curl -iX GET "localhost:8000/competitions/?pilot_name=Penelope+Pitstop&drone_name=WonderDrone"
curl -iX GET "localhost:8000/competitions/?min_distance_in_feet=700&max_distance_in_feet=9000&from_achievement_date=2017-10-18&to_achievement_date=2017-10-22&ordering=-achievement_date"

http://localhost:8000/competitions/?distance_in_feet=&drone_name=Atom&format=json&from_achievement_date=&max_distance_in_feet=&min_distance_in_feet=85&pilot_name=Penelope+Pitstop&to_achievement_date=

#pilot
http :8000/pilots/1
curl -iX GET localhost:8000/pilots/1

#drone
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Quadcopter"}' localhost:8000/drone-categories/
curl -iX GET "localhost:8000/drone-categories/?name=Quadcopter"
curl -iX GET "localhost:8000/drones/?drone_category=1&has_it_competed=False&ordering=-name"

#pilots
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Penelope Pitstop", "gender":"F", "races_count": 0}' localhost:8000/pilots/

#
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Need for Speed", "drone_category":"Quadcopter", "manufacturing_date": "2017-01-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Eclipse", "drone_category":"Octocopter", "manufacturing_date": "2017-02-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Gossamer Albatross", "drone_category":"Quadcopter", "manufacturing_date": "2017-03-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Dassault Falcon 7X", "drone_category":"Octocopter", "manufacturing_date": "2017-04-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Gulfstream I", "drone_category":"Quadcopter","manufacturing_date": "2017-05-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"RV-3", "drone_category":"Octocopter", "manufacturing_date": "2017-06-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Dusty", "drone_category":"Quadcopter", "manufacturing_date": "2017-07-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Ripslinger", "drone_category":"Octocopter", "manufacturing_date": "2017-08-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX POST -H "Content-Type: application/json" -d '{"name":"Skipper", "drone_category":"Quadcopter", "manufacturing_date": "2017-09-20T02:02:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl -iX GET localhost:8000/drones/
curl -iX GET "localhost:8000/drones/?limit=500"

pg 238
curl --user "hal":"hal" -iX POST -H "Content-Type: application/json" -d '{"name":"Python Drone", "drone_category":"Quadcopter", "manufacturing_date": "2017-07-16T02:03:00.716312Z", "has_it_competed": "false"}' localhost:8000/drones/
curl --user "tom":"tom" -iX PATCH -H "Content-Type: application/json" -d '{"has_it_competed": "true"}' localhost:8000/drones/12
curl --user "hal":"hal" -iX GET localhost:8000/drones/12
for i in {1..4}; do http -a "hal":"hal" :8000/competitions/; done;

#chp6, working with class-based views
#postgresql
sudo systemctl status postgresql
sudo systemctl start postgresql
sudo systemctl start docker

#new steps
1. docker-compose exec database psql -U tom -h database
2. docker-compose exec web python manage.py makemigrations toys  --pg46 
   docker-compose exec web python manage.py migrate 
3. docker-compose exec web python manage.py shell                --pg54 
4. 
from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer

toy_release_date = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
toy1 = Toy(name='Rambo', description='Rambo warrior', release_date=toy_release_date, toy_category='Action figures', was_included_in_home=True)
5.   
json_renderer = JSONRenderer()
toy1_rendered_into_json = json_renderer.render(serializer_for_toy1.data)
toy1_rendered_into_json
6.
json_string_for_new_toy = '{"name":"Clash Royale play set","description":"6 figures from Clash Royale","release_date":"2017-10-09T12:10:00.776594Z","toy_category":"Playset","was_included_in_home":false}'
json_bytes_for_new_toy = bytes(json_string_for_new_toy, encoding="UTF-8")
stream_for_new_toy = BytesIO(json_bytes_for_new_toy)
parser = JSONParser()
parsed_new_toy = parser.parse(stream_for_new_toy)
7. docker-compose logs -f
8. docker-compose exec web python manage.py startapp drones     --pg135, skips
9. docker-compose exec web python manage.py makemigrations drones     --pg135, skips
    docker-compose exec web python manage.py migrate 
10. docker-compose exec web python manage.py makemigrations drones  --pg181 
    docker-compose exec web python manage.py migrate 
11. docker-compose logs -f web 
12. docker-compose exec web python manage.py createsuperuser  --pg231 
13. docker-compose exec web python manage.py shell            --pg236 

    user = User.objects.create_user('hal', 'halvong@yahoo.com', 'hal')

   
# old steps
1. python manage.py makemigrations toys
2. python manage.py sqlmigrate toys 0001
3. python manage.py migrate 

1. python manage.py makemigrations drones
2. python manage.py migrate 
3. psql --username=tom --dbname=restful --command="\dt"
   or psql -d restful
4. psql --username=tom --dbname=restful --command="SELECT * FROM drones_dronecategory;"
   psql --username=tom --dbname=restful --command="SELECT * FROM drones_drone;"
   psql --username=tom --dbname=restful --command="SELECT * FROM drones_pilot;"
   psql --username=tom --dbname=restful --command="SELECT * FROM drones_competition;"
