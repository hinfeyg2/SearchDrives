import searchdrives
import os


def test():
	
	#r.parseEDL('testEDL1.edl')
	
	#r.createDBEntry("TestJob1", 000003)
	
	#r = searchdrives.drivelibrary()
	
	#r.deleteDBEntry(000003)
	#r = drivelibrary()
	
	r = searchdrives.drivelibrary()
	#r.addDrive("TestJob1", 000000, "/Users/gavinhinfey/GitHub/")
	print r.queryDBfile("GOPR0084A02.CE270C452014DB0.mxf")
	

def testConnection():
	
	if os.path.isfile(searchdrives.dbpath):
		return True
		
	else:
		return False

	
	
if __name__ == "__main__":
	test()