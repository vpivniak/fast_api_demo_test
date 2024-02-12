create sqlite database file
create table if not exists

run commands below:
source env_vars.sh
python database/setup_database.py

docker build --build-arg FLAG=-r -t ldit-image .
docker run -it -p 8080:80 ldit-image


docker run -p 8080:80 -d ldit-image 
docker run -v /Users/vpk/Documents/My_Project/LDIT/database:/data -it sqlite-image

docker ps -aq | xargs docker stop | xargs docker rm
docker inspect ldit-image  | grep IPAddress

docker container ls
docker container stop 