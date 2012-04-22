#!/usr/bin/env python3

import collections
import datetime
import os
import tarfile

import github_events
import util

def main():
	d = github_events.GITHUB_EVENTS_DIR
	backupDir = os.path.join(d, 'backups')
	files = os.listdir(d)
	today = datetime.datetime.utcnow().date()

	byDate = collections.defaultdict(list)
	for f in filter(lambda fn: fn.endswith('.json'), files):
		assert f.startswith('events-')
		date = util.extractDate(f)
		if date < today or True:
			byDate[date.isoformat()].append(f)
	if byDate:
		util.ensureDir(backupDir)
		for date,files in byDate.items():
			tarfn = os.path.join(d, 'events-' + date + '.tar.bz2')
			assert not os.path.exists(tarfn)
			with tarfile.open(tarfn, 'w:bz2') as tf:
				for f in files:
					fn = os.path.join(d, f)
					tf.add(fn, f, recursive=False)
			for f in files:
				os.rename(os.path.join(d, f), os.path.join(backupDir, f))

if __name__ == '__main__':
	main()
