import searchdrives
import os


def test():
	
	#r.parseEDL('testEDL1.edl')
	
	#r.createDBEntry("TestJob1", 000003)
	
	#r = searchdrives.drivelibrary()
	
	#r.deleteDBEntry(000003)
	#r = drivelibrary()
	
	
	r = searchdrives.drivelibrary("./drivelibrary.db")
	r.addDrive("TestJob1", 000000, "/Users/gavinhinfey/GitHub/")
	

def testConnection():
	
	if os.path.isfile(searchdrives.dbpath):
		return True
		
	else:
		return False

	
	
if __name__ == "__main__":
	test()