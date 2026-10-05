IMAGE ?= aperture-evidence-ledger
PORT ?= 8787
LLM_NAME ?= swiss-ai/Apertus-v1.5-8B
LLM_BASE_URL ?= http://host.docker.internal:8000/v1
LLM_API_KEY ?=

.PHONY: run build test

build:
	docker build -t $(IMAGE) .

run: build
	docker run --rm --name aperture-evidence-ledger \
		--add-host=host.docker.internal:host-gateway \
		-p $(PORT):8787 \
		-e LLM_NAME="$(LLM_NAME)" \
		-e LLM_BASE_URL="$(LLM_BASE_URL)" \
		-e LLM_API_KEY="$(LLM_API_KEY)" \
		$(IMAGE)

test:
	docker run --rm --entrypoint python $(IMAGE) -m unittest discover -s /app/tests -v
