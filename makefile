default: help


run: ## Executa projeto localmente
	@poetry run python manage.py runserver


test: ## Executa testes do projeto
	@poetry run python manage.py test


shell: ## Entra no ambiente virtual
	@poetry shell


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
