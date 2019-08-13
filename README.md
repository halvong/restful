Django Restful Web Services, Packtpub
8/13, Tues

PG63


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
   --pg55
   toy1 = Toy(name='Snoopy talking action figure', description='Snoopy speaks five languages', release_date=toy_release_date, toy_category='Action figures', was_included_in_home=False)
   toy2 = Toy(name='Hawaiian Barbie', description='Barbie loves Hawaii', release_date=toy_release_date, toy_category='Dolls', was_included_in_home=True)
   
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
