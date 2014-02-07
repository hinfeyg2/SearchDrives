import wx
import os
import subprocess
import threading
import searchdrives
import searchdrivetest

class MainWindow(wx.Frame):
	
	def __init__(self, parent, title):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Drive Library Menu", pos = wx.DefaultPosition, size = wx.Size( 350,400 ), style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX )
		
		gSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/FindDatabase.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButton1.Bind(wx.EVT_BUTTON, self.Button1Select, self.m_bpButton1)
		self.m_bpButton1.Bind(wx.EVT_ENTER_WINDOW, self.DBRollButtonOn)
		self.m_bpButton1.Bind(wx.EVT_LEAVE_WINDOW, self.DBRollButtonOff)
		gSizer.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/ScanDrive.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.Button2Select, self.m_bpButton2)
		self.m_bpButton2.Bind(wx.EVT_ENTER_WINDOW, self.DriveRollButtonOn)
		self.m_bpButton2.Bind(wx.EVT_LEAVE_WINDOW, self.DriveRollButtonOff)
		gSizer.Add( self.m_bpButton2, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/SearchWithList.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.Button3Select, self.m_bpButton3)
		self.m_bpButton3.Bind(wx.EVT_ENTER_WINDOW, self.EDLRollButtonOn)
		self.m_bpButton3.Bind(wx.EVT_LEAVE_WINDOW, self.EDLRollButtonOff)
		gSizer.Add( self.m_bpButton3, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		self.m_bpButton4 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/Search.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.Button4Select, self.m_bpButton4)
		self.m_bpButton4.Bind(wx.EVT_ENTER_WINDOW, self.SearchRollButtonOn)
		self.m_bpButton4.Bind(wx.EVT_LEAVE_WINDOW, self.SearchRollButtonOff)
		gSizer.Add( self.m_bpButton4, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.SetSizer(gSizer)
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Show(True)
		
	def DBRollButtonOn(self, event):
		self.m_statusBar1.SetStatusText("Set Database Location")
		
	def DBRollButtonOff(self, event):
		self.m_statusBar1.SetStatusText("")
	
	def DriveRollButtonOn(self, event):
		self.m_statusBar1.SetStatusText("Add Hard Drive")
		
	def DriveRollButtonOff(self, event):
		self.m_statusBar1.SetStatusText("")
	
	def EDLRollButtonOn(self, event):
		self.m_statusBar1.SetStatusText("Search Using EDL")
		
	def EDLRollButtonOff(self, event):
		self.m_statusBar1.SetStatusText("")
	
	def SearchRollButtonOn(self, event):
		self.m_statusBar1.SetStatusText("Search")
		
	def SearchRollButtonOff(self, event):
		self.m_statusBar1.SetStatusText("")

	def Button1Select(self, event):
		
		frame2 = DBWindow(None, "Find DB")
		x,y = self.GetPosition() 
		frame2.SetPosition((x,y)) 
		self.Show(False)
		
	def Button2Select(self, event):
		
		frame3 = DriveWindow(None, "Add/Update Drive")
		x,y = self.GetPosition() 
		frame3.SetPosition((x,y)) 
		self.Show(False)	
	
	def Button3Select(self, event):
		
		frame4 = EDLWindow(None, "Search With EDL")
		x,y = self.GetPosition() 
		frame4.SetPosition((x,y))
		self.Show(False)		
	
	def Button4Select(self, event):
	
		frame5 = SearchWindow(None, "Search")
		x,y = self.GetPosition() 
		frame5.SetPosition((x,y)) 
		self.Show(False)		
		
class DBWindow(wx.Frame):
	
	def __init__(self, parent, title):
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Connect Database", pos = wx.DefaultPosition, size = wx.Size(350,400), style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar1 )
		
		openButton = wx.Button(self, -1, 'Find Data Base', (10,50))
		self.Bind(wx.EVT_BUTTON, self.NavToDB, openButton)
		
		if searchdrivetest.testConnection():
			self.connectionStatus = wx.StaticText(self, -1, "Connected To DB",(15,20))
			openButton.Enable(False)
		else:
			self.connectionStatus = wx.StaticText(self, -1, "Not Connected To DB",(15,20))
			openButton.Enable(True)
		
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ), (20,270), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.ButtonReturn1, self.m_bpButton28)
		
		
		self.Layout()
		
		self.Centre(wx.BOTH)
		self.Show(True)
		
	def NavToDB(self, event):
		
		filename = ''
		dlg = wx.FileDialog(self, "Choose a File:",filename, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			searchdrives.dbpath = dlg.GetPath()
			self.connectionStatus.SetLabel("Connected To DB")
		
	def ButtonReturn1(self, event):
		frame1.m_statusBar1.SetStatusText("Search With EDL")
		self.Show(False)
		x,y = self.GetPosition() 
		frame1.SetPosition((x,y)) 
		frame1.Show(True)

class DriveWindow(wx.Frame):
	
	def __init__(self, parent, title):
		
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = "Add Drive To Library", pos = wx.DefaultPosition, size = wx.Size(350,400), style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar1 )
		
		self.openDrive = wx.Button(self, -1, 'Navigate to Root of Drive', (12,15))
		self.Bind(wx.EVT_BUTTON, self.NavToDrive, self.openDrive)

		self.DriveStatus = wx.StaticText(self, -1, "",(20,57))
		#SHIT
		self.m_bpButton26 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,180), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.ParseDir, self.m_bpButton26)
		self.m_bpButton26.Enable(False)
	
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,270), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.ButtonReturn1, self.m_bpButton28)
		
		
		self.txt1 = wx.TextCtrl(self, -1, pos=(20,95), size=(140,-1))
		self.txt1.SetValue('library number')
		self.txt1.Enable(False)
		
		self.txt2 = wx.TextCtrl(self, -1, pos=(20,140),size=(140,-1))
		self.txt2.SetValue('job name')
		self.txt2.Enable(False)
		
		self.Layout()
		
		self.Centre(wx.BOTH)
		self.Show(True)
	
	def ParseDir(self, event):
		list = []
		r = searchdrives.drivelibrary()
		self.EnteredNum = self.txt1.GetValue()
		self.EnteredName = self.txt2.GetValue()
		
		list = r.addDrive(self.chosendir)
		
		r.parseEDL(list)
		
		r.createDBEntry(self.EnteredName, self.EnteredNum)
		self.m_bpButton26.Enable(False)
	
	def NavToDrive(self, event):
		
		dirDirname = ''
		dlg = wx.DirDialog(self, "Choose Root of Drive:", dirDirname, wx.DD_DIR_MUST_EXIST, (50,50), (50,50))
		if dlg.ShowModal() == wx.ID_OK:
			self.chosendir = dlg.GetPath()
			self.DriveStatus.SetLabel(self.chosendir)
			self.txt2.Enable(True)
			self.txt1.Enable(True)
			self.m_bpButton26.Enable(True)
			self.m_bpButton28.Enable(True)
	
	def ButtonReturn1(self, event):
		frame1.m_statusBar1.SetStatusText("Search With EDL")
		x,y = self.GetPosition() 
		frame1.SetPosition((x,y)) 
		self.Show(False)
		frame1.Show(True)
		
class EDLWindow(wx.Frame):
	
	def __init__(self, parent, title):
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Search With EDL", pos = wx.DefaultPosition, size = wx.Size(350,400), style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX )
		
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ), (20,270), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.ButtonReturn1, self.m_bpButton28)
		
		self.Layout()
		
		self.Centre(wx.BOTH)
		self.Show(True)
	
	def ButtonReturn1(self, event):
		frame1.m_statusBar1.SetStatusText("Search With EDL")
		x,y = self.GetPosition() 
		frame1.SetPosition((x,y)) 
		self.Show(False)
		frame1.Show(True)
		
class SearchWindow(wx.Frame):
	
	def __init__(self, parent, title):
		
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = "Search", pos = wx.DefaultPosition, size = wx.Size(350,400), style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar1 )
		
		self.txt3 = wx.TextCtrl(self, -1, pos=(20,55), size=(140,-1))
		self.txt3.SetValue('Search')
		
		searchList = ["Global", "File", "Drives", "Paths", "Job", "Dates"]
		
		self.combo = wx.ComboBox(self, value = ("Search Options"), pos=(20,15), size=(145,25), choices=searchList)
		
		self.Layout()
		
		self.Centre(wx.BOTH)
		self.Show(True)
		
		self.m_bpButton26 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,180), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.runSearch, self.m_bpButton26)
		
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "/Users/gavinhinfey/GitHub/SearchDrives/ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,270), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.ButtonReturn1, self.m_bpButton28)
		
	def runSearch(self, event):
		r = searchdrives.drivelibrary()
		searchSelection = self.combo.GetValue()
		
		if searchSelection == "Global":
			list = r.queryDBglobal(self.txt3.GetValue())
			for i in list:
				for y in i:
					print y
		
		elif searchSelection == "File":
			found = r.queryDBfile(self.txt3.GetValue())
			for i in found:
				for y in i:
					print y
			
		elif searchSelection == "Drives":
			print r.queryDBlibnum(self.txt3.GetValue())
		
		elif searchSelection == "Paths":
			print r.queryDBpath(self.txt3.GetValue())
			
		elif searchSelection == "Job":
			print r.queryDBjob(self.txt3.GetValue())
			
		elif searchSelection == "Dates":
			print r.queryDBdate(self.txt3.GetValue())
    	
	def ButtonReturn1(self, event):
		frame1.m_statusBar1.SetStatusText("Search With EDL")
		x,y = self.GetPosition() 
		frame1.SetPosition((x,y)) 
		self.Show(False)
		frame1.Show(True)
	
app = wx.App(True)
frame1 = MainWindow(None, "Drive Library")
app.MainLoop()