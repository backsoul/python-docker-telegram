docker-compose down --remove-orphans &&
docker-compose build &&
docker-compose up -d &&
echo "El bot ya se esta ejecutando.." &&
echo "- Docker logs -" &&
docker logs -f bot-python
