import re
import os
import time
import subprocess
import sqlite3 as lite
import sys
import datetime


class drivelibrary:
	
	def __init__(self):
		
		self.con = lite.connect('/Users/gavinhinfey/Desktop/drivelibrary.db' ,detect_types=lite.PARSE_DECLTYPES)
	
	def createDBEntry(self, job, driveNum):
		
		with self.con:
			cur = self.con.cursor()
			
			try:
				cur.execute("CREATE TABLE DriveLibrary(CreateTime TEXT ,JobName TEXT, LibNum INT, FilePath TEXT, FileName TEXT)")
			
			except:
				pass
			
			for i in self.docFiles:
				
				date = datetime.datetime.today()

				cats = []
				cats = i.split('\\')
				filename = cats[-1]
				del cats[-1]
				path = ''
				for j in cats:
					path += j + '\\'
				dogs = "INSERT INTO DriveLibrary VALUES('%s', '%s', '%s', '%s', '%s')" % (date, job, driveNum, path, filename)
				cur.execute(str(dogs))
				

			cur.close()	
		
	def parseEDL(self, queryDoc):
		
		queryList = open(queryDoc, 'r+')
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
    		for i in found:
    			return i
    			
	def queryDBdate(self, date):

		with self.con:    

			cur = self.con.cursor()
			date = str(date)
			term = '%' + date + '%'
			rows = cur.execute("SELECT * from DriveLibrary where CreateTime LIKE ?",(term,))
			found = rows.fetchall()
			for i in found:
				return i
			
	def queryDBjob(self, job):
	
		with self.con:    
    
   			cur = self.con.cursor()
   			job = str(job)
   			term = '%' + job + '%'
    		rows = cur.execute("SELECT * from DriveLibrary where JobName LIKE ?",(term,))
    		found = rows.fetchall()
    		for i in found:
    			return i
			
	def queryDBpath(self, path):
	
		with self.con:    
    		
   			cur = self.con.cursor()
   			path = str(path)
   			term = '%' + path + '%'
    		rows = cur.execute("SELECT * from DriveLibrary where FilePath LIKE ?",(term,))
    		found = rows.fetchall()
    		for i in found:
    			return i
			
	def queryDBlibnum(self, libnum):
		
		with self.con:
			
			cur = self.con.cursor()
			rows = cur.execute("SELECT * from DriveLibrary where LibNum = '%s'" % (libnum))
			found = rows.fetchall()
			for i in found:
				return i
				
	def queryDBglobal(self, searchQuery):

		foundList = []
		
		foundList.append(self.queryDBfile(searchQuery))
		foundList.append(self.queryDBdate(searchQuery))
		foundList.append(self.queryDBjob(searchQuery))
		foundList.append(self.queryDBpath(searchQuery))
		foundList.append(self.queryDBlibnum(searchQuery))
		"""
		for i in foundList:
			if i == None:
				foundList[i].pop()
		
		print foundList
		"""
				
	def deleteDBEntry(self, driveNum):
		
		print "CATS"