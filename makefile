ENV_FILE=.env_dev


default: help


run: ## Executa projeto localmente
	@export $$(cat ${ENV_FILE} | xargs); \
	poetry run python manage.py runserver


test: ## Executa testes do projeto
	@export $$(cat ${ENV_FILE} | xargs); \
	poetry run python manage.py test


shell: ## Entra no ambiente virtual
	@export $$(cat ${ENV_FILE} | xargs); \
	poetry shell


requirements: ## Gera arquivo de dependencias do projeto
	@poetry export --without-hashes > requirements.txt


dc_up: dc_down ## Executa containers docker
	@docker-compose -f docker/docker-compose.yml up -d --remove-orphans || true


dc_down: ## Encerra containers docker
	@docker-compose -f docker/docker-compose.yml down || true


lint: lint_black lint_flake8 ## Analisa sintaxe e estilo


lint_black: ## Analisa sintaxe
	@poetry run black \
		--skip-string-normalization \
		--line-length 79 \
		--diff \
		--check .

lint_flake8: ## Analisa estilo
	@poetry run flake8 --ignore=W583,W503,W504,E501,E303 .


help: ## Exibe essa mensagem de ajuda
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | \
	sed -e 's/:.*##\s*/:/' \
	-e 's/^\(.\+\):\(.*\)/\\x1b[36mmake \1\\x1b[m:\2/' | \
	column -c2 -t -s :']]')"
