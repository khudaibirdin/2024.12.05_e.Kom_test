build:
	docker build -t fastapi_app .
run:
	docker run -it -d --env-file .env --restart=unless-stopped --name fastapi_app_container fastapi_app
stop:
	docker stop fastapi_app_container
attach:
	docker attach fastapi_app_container
dell:
	docker rm fastapi_app_container
testing:
	cd test && python test.py