up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

build:
	docker-compose build

health:
	curl -f http://localhost/health || echo "App not healthy"

clean:
	docker-compose down -v --rmi all
