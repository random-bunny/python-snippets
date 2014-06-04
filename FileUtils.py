import re
import os
import fnmatch

def gen_file_list(base_path):
	for base, unused, filelist in os.walk(base_path):
		for name in filelist:
			yield os.path.join(base, name)

def files_matching_regex(base_path, regex, ignore_case=False):
	try:
		if ignore_case:
			pat = re.compile(regex, re.IGNORECASE)
		else:
			pat = re.compile(regex)
	except re.error:
		raise StopIteration
	else:
		for filename in gen_file_list(base_path):
			if pat.search(filename) is not None:
				yield filename

def files_matching_glob(base_path, glob):
	for filename in gen_file_list(base_path):
		if fnmatch.fnmatch(filename, glob):
			yield filename

if __name__ == '__main__':
	print 'Unfiltered:'
	print '\n'.join([item for item in gen_file_list('/bin')])
	print 'Filtered Regex'
	print '\n'.join([item for item in files_matching_regex('/bin', '/ch.+')])
	print 'Filtered Glob'
	print '\n'.join([item for item in files_matching_glob('/bin', '*ch*')])