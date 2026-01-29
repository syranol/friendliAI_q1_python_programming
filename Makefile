.PHONY: venv test

venv:
	python3.11 -m venv .venv

# Activate with: source .venv/bin/activate

test:
	python3.11 -m unittest discover -s tests
