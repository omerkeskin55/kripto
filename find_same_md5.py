import sys
import os
import hashlib
import collections
from collections import defaultdict


BUF_SIZE = 65536 
path = sys.argv[1]##  Command line arguman olarak path alır


##  Verilen bir pathdeki file isimlerini return eder
def get_filepaths(path):
	filenames = next(os.walk(path))[2]
	return filenames
	


##  Bir file için md5 hash uretir
def hash_file(filename):
	md5 = hashlib.md5()
	f = open(filename, 'rb')
	while True:
	    data = f.read(BUF_SIZE)
	    if not data:
	        break
	    md5.update(data)
	return md5       


## main method

def main():
	hashCodes = []
	filenames =[]
	

	for filename in get_filepaths(path):
		filenameWithPath = path + "\\" + filename
		#print(filenameWithPath)
		hashCodes.append(hash_file(filenameWithPath).hexdigest())
		filenames.append(filename)
		#print(filename + "  ---->>  " + hash_file(filenameWithPath).hexdigest())
		
		
	# hashcode ve filename lerden dictionary olustur
	#dictionary = dict(zip(hashCodes, filenames))
	s = list(zip(hashCodes, filenames))
	d = defaultdict(list)


	## dictionary i bir keyin virden fazla value si olan defaultdick te cevirmek
	for k, v in s:
		d[k].append(v)
	
	for k, v in s:
		if (len(d.get(k)) > 1):
			print(d.get(k))



if __name__ == "__main__": main()