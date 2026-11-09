PYTHON = python3
CONFIG = config.txt

install:
	pip install flake8 mypy

run:
	$(PYTHON) a_maze_ing.py $(CONFIG)

debug:
	$(PYTHON) -m pdb a_maze_ing.py $(CONFIG)

clean:
	rm -rf __pycache__ */__pycache__ .mypy_cache

lint:
	flake8 . --exclude=.venv
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports \
		--disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 . --exclude=.venv
	mypy . --strict

.PHONY: install run debug clean lint lint-stricts