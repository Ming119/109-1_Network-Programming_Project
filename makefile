.PHONY: run

init:
	pip3 install -r ./doc/requirements.txt

run:
	python3 ./bin/main.py

test_route: mkDEBUG
	python3 ./bin/route.py > ./DEBUG/routeDEBUG.txt

mkDEBUG:
	mkdir -p DEBUG
