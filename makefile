run:
	@poetry run python manage.py runserver


test:
	@poetry run python manage.py test


shell:
	@poetry shell


help: ## Exibe essa mensagem de ajuda
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | \
	sed -e 's/:.*##\s*/:/' \
	-e 's/^\(.\+\):\(.*\)/\\x1b[36mmake \1\\x1b[m:\2/' | \
	column -c2 -t -s :']]')"
