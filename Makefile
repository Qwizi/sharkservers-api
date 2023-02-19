
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
	alembic upgrade head
	sleep 2
	curl -X POST http://localhost/install \
   		-H 'Content-Type: application/json' \
   		-d '{"username":"Qwizi","email":"test@test.pl", "password":"test123456", "password2":"test123456"}'

test:
	docker-compose exec app pytest -vv


generate:
	curl -X GET http://localhost/generate-openapi