EMPTY:

create-secret:
	-kubectl --namespace=hogwarts-bot delete secret hogwarts-secrets
	kubectl --namespace=hogwarts-bot create secret generic hogwarts-secrets \
	  --from-file=./secrets.py

create-namespace:
	kubectl create -f ./namespace.yaml

build: EMPTY
	docker build -t hogwarts-bot .
	docker tag hogwarts-bot gcr.io/khan-internal-services/hogwarts-bot
	gcloud docker -- push gcr.io/khan-internal-services/hogwarts-bot

run: build
	kubectl create -f ./deployment.yaml

stop:
	kubectl --namespace=hogwarts-bot delete deployment hogwarts-bot