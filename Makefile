all:
	nosetests

init:
	virtualenv --python=python2 env
	. env/bin/activate && pip install -r requirements.txt --use-mirrors

pypdf2:
	mkdir -p env/build;\
	cd env/build;\
	wget "http://github.com/knowah/PyPDF2/tarball/master" -O pypdf2.tar.gz;\
	tar xvzf pypdf2.tar.gz;\
	cd knowah*;\
	python setup.py install
