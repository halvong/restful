Django Restful Web Services, Packtpub
10/02, Wed

PG58


#
curl -X GET localhost:8000/toys/


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
