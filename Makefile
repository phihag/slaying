
default: download-libs

tar: deploytar

deploytar:
	tar --dereference -cjf ../slaying.tar.bz2 -C .. --exclude data --exclude slaying.tar.bz2 --exclude libs slaying 

download-libs:
	mkdir -p libs
	./.getgit.sh git://github.com/phihag/tornado.git libs/tornado
	cd libs/tornado && python3 setup.py build

gather-events:
	mkdir -p data
	nohup python3 -B github_events.py >data/github-events.log 2>&1 &

clean:
	rm -rf libs
