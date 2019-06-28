Django Restful Web Services, Packtpub
6/28, Fri


#chp6, working with class-based views
#postgresql
#sudo systemctl status postgresql
#sudo systemctl start postgresql

#new steps
docker-compose exec database psql -U tom -h database

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