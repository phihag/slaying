
default: download-libs

tar: deploytar

deploytar:
	tar --dereference -cjf ../slaying.tar.bz2 -C .. --exclude data slaying 

download-libs:
	mkdir -p libs
	./.getgit.sh git://github.com/phihag/tornado.git libs/tornado
	cd libs/tornado && python3 setup.py build

clean:
	rm -rf libs
