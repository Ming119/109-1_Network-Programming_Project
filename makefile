.PHONY: run

run:
	python3 ./bin/main.py

run_web:
	python3 ./bin/app.py

test_main: mkDEBUG
	python3 ./bin/main.py > ./DEBUG/mainDEBUG.txt

test_route: mkDEBUG
	python3 ./bin/route.py > ./DEBUG/routeDEBUG.txt

test_api: mkDEBUG
	python3 ./bin/api.py > ./DEBUG/apiDEBUG.txt

mkDEBUG:
	mkdir -p DEBUG
