up:
	@echo "Starting containers"
	docker-compose up -d
	@echo "Containers started"

stop:
	@echo "Starting stopping containers"
	docker-compose stop
	@echo "Containers stopped"

down:
	@echo "Starting removing containers"
	docker-compose down
	@echo "Containers removed"

logs:
	@echo "Starting logs"
	docker-compose logs -f

uninstall:
	@echo "Starting removing containers"
	docker-compose down
	@echo "Containers removed"
	@echo "Started removing instalation file"
	rm -rf src/installed
	@echo "Instalation file removed"


install:
	@echo "Staring database container"
	docker-compose up -d
	sleep 2
	alembic upgrade head
	sleep 2
	curl -X POST http://localhost/install \
   		-H 'Content-Type: application/json' \
   		-d '{"username":"Qwizi","email":"test@test.pl", "password":"test123456", "password2":"test123456"}'

test:
	docker-compose exec app pytest -vv


generate:
	curl -X GET http://localhost/generate-openapi