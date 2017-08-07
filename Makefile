VIRITUALENV = virtualenv
VENV = ./env
PYTHON = $(VENV)/bin/python
PIP = $(VEN)/bin/pip
SOLUTION = ./solution
APP = ./app

variable:
	echo $(PIP)
	echo $(VENV)
	echo $(PYTHON)

init:
	@$(VIRTUALENV) env
	exec source $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

spider:
	$(PYTHON) spider.py

clean:
	find . -not \( -path './$(VENV)' -prune \) -name '*.pyc' -exec rm -f {} \;

delete:
	rm -r ./solution

test:
    $(PYTHON)