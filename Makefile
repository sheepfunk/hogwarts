EMPTY:

create-secret:
	-kubectl --namespace=hogwarts-bot delete secret hogwarts-secrets
	kubectl --namespace=hogwarts-bot create secret generic hogwarts-secrets \
	  --from-file=./secrets.py --from-file=./hogwarts-bot-credentials.json

create-namespace:
	kubectl create -f ./namespace.yaml

build: EMPTY
	docker build -t hogwarts-bot .
	docker tag hogwarts-bot sheepfunk/hogwarts-bot
	gcloud docker -- push sheepfunk/hogwarts-bot

run: build
	kubectl create -f ./deployment.yaml

stop:
	kubectl --namespace=hogwarts-bot delete deployment hogwarts-bot