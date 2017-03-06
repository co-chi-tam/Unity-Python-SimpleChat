# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ClientFrame
###########################################################################

class ClientFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Client chat", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Server" ), wx.HORIZONTAL )
		
		self.m_ServerHostLabel = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Server host:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ServerHostLabel.Wrap( -1 )
		sbSizer1.Add( self.m_ServerHostLabel, 0, wx.ALL, 5 )
		
		self.m_ServerHostText = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ServerHostText.SetMaxLength( 100 ) 
		sbSizer1.Add( self.m_ServerHostText, 0, wx.ALL, 5 )
		
		self.m_ServerPortLabel = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Server port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ServerPortLabel.Wrap( -1 )
		sbSizer1.Add( self.m_ServerPortLabel, 0, wx.ALL, 5 )
		
		self.m_ServerPortText = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"5000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ServerPortText.SetMaxLength( 10 ) 
		sbSizer1.Add( self.m_ServerPortText, 0, wx.ALL, 5 )
		
		self.m_ConnectButton = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ConnectButton.SetToolTip( u"Connect server" )
		
		sbSizer1.Add( self.m_ConnectButton, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( sbSizer1, 0, wx.ALIGN_CENTER|wx.EXPAND, 1 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_ChatReceiverText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_ChatReceiverText.Wrap( 1 )
		bSizer4.Add( self.m_ChatReceiverText, 1, wx.ALL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer4 )
		self.m_scrolledWindow1.Layout()
		bSizer4.Fit( self.m_scrolledWindow1 )
		bSizer3.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Client" ), wx.HORIZONTAL )
		
		self.m_staticText18 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Chat :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		sbSizer4.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_ClientChatText = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ClientChatText.SetMaxLength( 30 ) 
		self.m_ClientChatText.SetMinSize( wx.Size( 300,-1 ) )
		self.m_ClientChatText.SetMaxSize( wx.Size( 300,-1 ) )
		
		sbSizer4.Add( self.m_ClientChatText, 0, wx.ALL, 5 )
		
		self.m_ClientSubmitButton = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_ClientSubmitButton, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 5, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		self.Show(True)
		# Connect Events
		self.m_ConnectButton.Bind( wx.EVT_BUTTON, self.OnClientConnectServer )
		self.m_ClientSubmitButton.Bind( wx.EVT_BUTTON, self.OnClientChatSubmit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClientConnectServer( self, event ):
		event.Skip()
	
	def OnClientChatSubmit( self, event ):
		event.Skip()
	

