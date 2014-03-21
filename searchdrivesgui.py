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
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/FindDatabase.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButton1.Bind(wx.EVT_BUTTON, self.Button1Select, self.m_bpButton1)
		self.m_bpButton1.Bind(wx.EVT_ENTER_WINDOW, self.DBRollButtonOn)
		self.m_bpButton1.Bind(wx.EVT_LEAVE_WINDOW, self.DBRollButtonOff)
		gSizer.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/ScanDrive.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.Button2Select, self.m_bpButton2)
		self.m_bpButton2.Bind(wx.EVT_ENTER_WINDOW, self.DriveRollButtonOn)
		self.m_bpButton2.Bind(wx.EVT_LEAVE_WINDOW, self.DriveRollButtonOff)
		gSizer.Add( self.m_bpButton2, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/SearchWithList.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.Button3Select, self.m_bpButton3)
		self.m_bpButton3.Bind(wx.EVT_ENTER_WINDOW, self.EDLRollButtonOn)
		self.m_bpButton3.Bind(wx.EVT_LEAVE_WINDOW, self.EDLRollButtonOff)
		gSizer.Add( self.m_bpButton3, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		self.m_bpButton4 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/Search.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
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
		
		self.frame5 = SearchWindow(None, "Search")
		x,y = self.GetPosition() 
		self.frame5.SetPosition((x,y)) 
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
		
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ), (20,270), wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButton28.Bind(wx.EVT_ENTER_WINDOW, self.BackButtonOn)
		self.m_bpButton28.Bind(wx.EVT_LEAVE_WINDOW, self.BackButtonOff)
		
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
			print searchdrives.dbpath
		
	def ButtonReturn1(self, event):
		frame1.m_statusBar1.SetStatusText("Search With EDL")
		self.Show(False)
		x,y = self.GetPosition() 
		frame1.SetPosition((x,y)) 
		frame1.Show(True)

	def BackButtonOn(self, event):
		self.m_statusBar1.SetStatusText("Back")

	def BackButtonOff(self, event):
		self.m_statusBar1.SetStatusText("")

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
		self.m_bpButton26 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,180), wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButton26.Bind(wx.EVT_ENTER_WINDOW, self.BackButtonOn)
		self.m_bpButton26.Bind(wx.EVT_LEAVE_WINDOW, self.BackButtonOff)
		
		self.Bind(wx.EVT_BUTTON, self.ParseDir, self.m_bpButton26)
		self.m_bpButton26.Enable(False)
	
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,270), wx.DefaultSize, wx.BU_AUTODRAW )
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

	def BackButtonOn(self, event):
		self.m_statusBar1.SetStatusText("Back")

	def BackButtonOff(self, event):
		self.m_statusBar1.SetStatusText("")
	
class EDLWindow(wx.Frame):
	
	def __init__(self, parent, title):
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Search With EDL", pos = wx.DefaultPosition, size = wx.Size(350,400), style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX )
		
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ), (20,270), wx.DefaultSize, wx.BU_AUTODRAW )
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
		
		self.m_bpButton26 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,180), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.runSearch, self.m_bpButton26)
		
		self.m_bpButton28 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( "./ICONS/backbutton.png", wx.BITMAP_TYPE_ANY ),(18,270), wx.DefaultSize, wx.BU_AUTODRAW )
		self.Bind(wx.EVT_BUTTON, self.ButtonReturn1, self.m_bpButton28)
		
	def runSearch(self, event):
		
		fr = CallResults()
		fr.Show(True)
		
		
	def ButtonReturn1(self, event):
		frame1.m_statusBar1.SetStatusText("Search With EDL")
		x,y = self.GetPosition() 
		frame1.SetPosition((x,y)) 
		self.Show(False)
		frame1.Show(True)
		

class CallResults(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'Search Results')
		sz = wx.BoxSizer(wx.VERTICAL)
		pa = AScrolledWindow(self)
		sz.Add(pa, 1, wx.EXPAND)
		self.SetSizer(sz)
		
	

class AScrolledWindow(wx.ScrolledWindow):

	def __init__(self, parent):
		self.parent = parent
		wx.ScrolledWindow.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)

		gb = wx.GridBagSizer(vgap=0, hgap=3)
		self.sizer = gb
		self._labels = []
		self._show_but = wx.Button(self, -1, "Show")
		self._hide_but = wx.Button(self, -1, "Hide")
		gb.Add(self._show_but, (0,0), (1,1))
		gb.Add(self._hide_but, (0,1), (1,1))

		r = searchdrives.drivelibrary()
		
		
		searchSelection = frame1.frame5.combo.GetValue()
		
		searchresults = []
		
		if searchSelection == "Global":
			list = r.queryDBglobal(frame1.frame5.txt3.GetValue())
			for i in list:
				for y in i:
					searchresults.append(y)
		
		elif searchSelection == "File":
			found = r.queryDBfile(frame1.frame5.txt3.GetValue())
			for i in found:
				for y in i:
					searchresults.append(y)
			
		elif searchSelection == "Drives":
			searchresults.append(r.queryDBlibnum(frame1.frame5.txt3.GetValue()))
		
		elif searchSelection == "Paths":
			searchresults.append(r.queryDBpath(frame1.frame5.txt3.GetValue()))
			
		elif searchSelection == "Job":
			searchresults.append(r.queryDBjob(frame1.frame5.txt3.GetValue()))
			
		elif searchSelection == "Dates":
			searchresults.append(r.queryDBdate(frame1.frame5.txt3.GetValue()))
			
		newline= ""
		count = 0
		#THIS CURRENT SEARCH WORKS SLIGHTLY FOR SEARCHING FILES!
		
		mouse = "Mouse!"
		mouselist = ["Bats","Jacks","Frogs","Cats"]
		catslist = ["dogs", "People", "Horses"]
		listmoustlist = [mouselist, catslist]



		
		try:
			assert not isinstance(searchresults, basestring)
			
		except:
			

			self._labels.append(wx.StaticText(self, -1, str(searchresults)))
			gb.Add(self._labels[-1], (1,1), (1,1))
			pass
		
		else:
			

			for i in searchresults:
				count += 1
				try:
					assert not isinstance(i, (basestring, int))
					
				except:
					
					
					self._labels.append(wx.StaticText(self, -1, str(i)))
					gb.Add(self._labels[-1], (count,1), (1,1))
					print "1"
					pass

				else:
					
					
					for y in i:
						count += 1
						try:
							assert not isinstance(y, (basestring, int))
					
						except:

							self._labels.append(wx.StaticText(self, -1, str(y)))
							gb.Add(self._labels[-1], (count,1), (1,1))
							
							pass
						else:
							for z in y:
								count += 1
								
								try:
									assert not isinstance(z, (basestring, int))

					
								except:

									self._labels.append(wx.StaticText(self, -1, str(z)))
									gb.Add(self._labels[-1], (count,1), (1,1))
									
									pass
									
								else:
									pass



		self._labels.append(wx.StaticText(self, -1,newline))
		self._show_but.Bind(wx.EVT_BUTTON, self.OnShow)
		self._hide_but.Bind(wx.EVT_BUTTON, self.OnHide)
		self.SetSizer(self.sizer)
		fontsz = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT).GetPixelSize()
		self.SetScrollRate(fontsz.x, fontsz.y)
		self.EnableScrolling(True,True)
		
	def OnShow(self, event):
		for lab in self._labels:
			self.sizer.Show(lab, True)
			self.OnInnerSizeChanged()
	
	def OnHide(self, event):
		for lab in self._labels:
			self.sizer.Show(lab, False)
			self.OnInnerSizeChanged()
	
	def OnInnerSizeChanged(self):
		w,h = self.sizer.GetMinSize()
		self.SetVirtualSize((w,h))
		
		#self.Layout()
		#self.Show(True)
				
				

app = wx.App(True)
frame1 = MainWindow(None, "Drive Library")
app.MainLoop()
