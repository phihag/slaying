
tar:
	tar --dereference -cjf ../slaying.tar.bz2 -C .. slaying

download-libs:
	mkdir -p libs
	./.getgit.sh git://github.com/facebook/tornado.git libs/tornado
	cd libs/tornado && python3 setup.py build
