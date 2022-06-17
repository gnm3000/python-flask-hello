install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

test-unit:
	python -m pytest -vv --cov=app tests/unit/

test-integration:
	python -m pytest -vv --cov=app tests/integration/

lint:
	pylint --disable=R,C app.py