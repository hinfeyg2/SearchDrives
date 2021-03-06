import re
import os
import time
import subprocess
import sqlite3 as lite
import sys
import datetime
import unicodedata

dbpath = "\\\\192.168.1.110\\avid\\GavinH\\SearchDrives\\drivelibrary.db"

class drivelibrary:
	
	def __init__(self):
		
		global dbpath
		self.con = lite.connect(dbpath ,detect_types=lite.PARSE_DECLTYPES)
	
	def createDBEntry(self, job, driveNum):
		
		with self.con:
			cur = self.con.cursor()
			
			# Check to see if db exists.
			try:
				cur.execute("CREATE TABLE DriveLibrary(CreateTime TEXT ,JobName TEXT, LibNum INT, FilePath TEXT, FileName TEXT)")
			
			except:
				
				pass
			
			
			# Check to see if my new drive has already been added to the library.
			if self.queryDBlibnum(driveNum):
				
				deleteVal = "DELETE FROM DriveLibrary WHERE LibNum=%s" % (driveNum)
				cur.execute(deleteVal)
				
				self.addquery(job, driveNum)
			
			else:
				
				self.addquery(job, driveNum)
	
	def addDrive(self, drivePath):
		
		proc = subprocess.Popen('dir /a-d /s /b /ogen ' + '"' + str(drivePath) + '"', shell=True, stdout=subprocess.PIPE)
		outputlines = filter(lambda x:len(x)>0,(line.strip() for line in proc.stdout))
		print outputlines
		return outputlines
	
	def not_combining(self, char):
		return unicodedata.category(char) != 'Mn'
        
	def strip_accents(self, text, encoding):
		unicode_text= unicodedata.normalize('NFD', text.decode(encoding))
		return filter(self, not_combining, unicode_text).encode(encoding)
		
	def addquery(self, job, driveNum):
			
			with self.con:
				cur = self.con.cursor()
			
				for i in self.docFiles:

					date = datetime.datetime.today()

					cats = []
					cats = i.split('\\')
					filename = cats[-1]
					del cats[-1]
					path = ''
					for j in cats:
						path += j + '\\'
					
					cur.execute("""INSERT INTO DriveLibrary VALUES(?, ?, ?, ?, ?)""", (date, job, driveNum, path, filename))
				
				cur.close()	
		
	def parseEDL(self, queryList):
		
		self.docFiles = []
		for line in queryList:
			line = str(line)
			self.docFiles.append(line)
	
	def queryDBfile(self, file):
	
		with self.con:    
    
   			cur = self.con.cursor()
   			file = str(file)
   			FileString = file
    		term = '%' + FileString + '%'
    		rows = cur.execute("SELECT * from DriveLibrary where FileName LIKE ?",(term,))
    		found = rows.fetchall()
    		"""
    		for i in found:
    			return i
    		"""
    		return found
    				
	def queryDBdate(self, date):

		with self.con:    

			cur = self.con.cursor()
			date = str(date)
			term = '%' + date + '%'
			rows = cur.execute("SELECT * from DriveLibrary where CreateTime LIKE ?",(term,))
			found = rows.fetchall()
			"""
			for i in found:
				return i
			"""
			return found
			
	def queryDBjob(self, job):
	
		with self.con:    
    
   			cur = self.con.cursor()
   			job = str(job)
   			term = '%' + job + '%'
    		rows = cur.execute("SELECT * from DriveLibrary where JobName LIKE ?",(term,))
    		found = rows.fetchall()
    		"""
    		for i in found:
    			return i
    		"""
    		return found
			
	def queryDBpath(self, path):
	
		with self.con:    
    		
   			cur = self.con.cursor()
   			path = str(path)
   			term = '%' + path + '%'
    		rows = cur.execute("SELECT * from DriveLibrary where FilePath LIKE ?",(term,))
    		found = rows.fetchall()
    		"""
    		for i in found:
    			return i
    		"""
    		return found
					
	def queryDBlibnum(self, libnum):
		
		with self.con:
			
			cur = self.con.cursor()
			rows = cur.execute("SELECT * from DriveLibrary where LibNum = '%s'" % (libnum))
			found = rows.fetchall()
			"""
			for i in found:
				return i
			"""
			return found
	
	#Has a bug.
	def queryDBglobal(self, searchQuery):

		foundList = []
		
		foundList.append(self.queryDBfile(searchQuery))
		foundList.append(self.queryDBdate(searchQuery))
		foundList.append(self.queryDBjob(searchQuery))
		foundList.append(self.queryDBpath(searchQuery))
		foundList.append(self.queryDBlibnum(searchQuery))
		
		return foundList
		
	#This delete method doesn't work.			
	def deleteDBEntry(self, driveNum):
		
		
		driveNum = int(driveNum)
		cur = self.con.cursor()
		deleteVal = "DELETE FROM DriveLibrary WHERE LibNum=%s" % (driveNum)
		cur.execute(deleteVal)
		print "Great!"		
		cur.close()
		
	def openDB(self, dbpath):
		
		self.con = lite.connect(dbpath ,detect_types=lite.PARSE_DECLTYPES)
