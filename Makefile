.PHONY: make-requirement

make-requirements:
	pip freeze > requirements.txt

install-requirements:
	pip install -r requirements.txt


