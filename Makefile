init:
	pip install -r requirements.txt

test:
	tox

run:
	python app.py
