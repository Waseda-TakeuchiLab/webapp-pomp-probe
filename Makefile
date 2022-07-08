run:
	python webapp_pomp_probe

test: mypy unittest

mypy:
	mypy cropsiss tests

unittest:
	coverage run -m unittest
	coverage html
	coverage report