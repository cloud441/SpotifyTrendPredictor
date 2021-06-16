all: run


init:
	pip install -r requirements.txt
	chmod 755 src/spotifyPredictor.py


run:
	./src/spotifyPredictor.py


.PHONY: init
