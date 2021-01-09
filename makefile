.PHONY: run

run:
	python3 ./bin/main.py

test_route: mkDEBUG
	python3 ./bin/route.py > ./DEBUG/routeDEBUG.txt

test_api: mkDEBUG
	python3 ./bin/api.py > ./DEBUG/apiDEBUG.txt

mkDEBUG:
	mkdir -p DEBUG

setup:
	pip3 install -r ./doc/requirements.txt
