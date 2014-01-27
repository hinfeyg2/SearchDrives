import searchdrives


def test():
	
	a = "a"
	b = "b"
	r = searchdrives.drivelibrary()
	#r.parseEDL('testEDL.edl')
	
	#r.createDBEntry("TestJob1", 34123)
	
	r.queryDBglobal("A001_1213ZT")
	
if __name__ == "__main__":
	test()