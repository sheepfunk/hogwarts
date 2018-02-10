EMPTY:

create-secret:
	-kubectl delete secret hogwarts-secrets
	kubectl create secret generic hogwarts-secrets \
	  --from-file=./secrets.py

build: EMPTY
	docker build -t khan/hogwarts:latest .

run: build
	kubectl create -f ./deployment.yaml

stop:
	kubectl delete deployment hogwarts-bot