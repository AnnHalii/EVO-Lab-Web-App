IMAGE ?= app_web:develop
COMPOSE ?= docker-compose

.EXPORT_ALL_VARIABLES:

.default: run

build:
	docker build -t $(IMAGE) .

run:
	docker-compose up -d
stop:
	$(COMPOSE) stop

logs:
	$(COMPOSE) logs -f web

exec:
	docker exec -it lab-web-app_web_1 bash