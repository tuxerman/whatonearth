clean:
	rm -rf venv;

install:
	virtualenv -p python3 venv --no-site-packages; \
	venv/bin/pip install -r requirements.txt;
