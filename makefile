default: help


run: ## Executa projeto localmente
	@poetry run python manage.py runserver


test: ## Executa testes do projeto
	@poetry run python manage.py test


shell: ## Entra no ambiente virtual
	@poetry shell


help: ## Exibe essa mensagem de ajuda
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | \
	sed -e 's/:.*##\s*/:/' \
	-e 's/^\(.\+\):\(.*\)/\\x1b[36mmake \1\\x1b[m:\2/' | \
	column -c2 -t -s :']]')"
