VENV = env
PYTHON = $(VENV)/bin/python
PIP = $(VEN)/bin/pip
SOLUTION = ./solution
init:
	$(PIP) install -r requirements.txt

spider:
	$(PYTHON) spider.py

clean:
	find . -not \( -path './$(VENV)' -prune \) -name '*.pyc' -exec rm -f {} \;

delete:
	rm -r ./solution
