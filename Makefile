install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C app.py

test-unit:
	python -m pytest -vv --cov=app tests/unit/

test-integration:
	python -m pytest -vv --cov=app tests/integration/
