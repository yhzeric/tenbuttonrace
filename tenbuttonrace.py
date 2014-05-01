#!/usr/bin/env python

import wx

import time

import random

import math

class NewFrame(wx.Frame):
    
    def __init__(self, parent):
        
        wx.Frame.__init__(self, parent, wx.ID_ANY, "TenButtonRace")
        
        self.panel = wx.Panel(self)
        
        self.BtnOne = wx.Button(self.panel, label = "1", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnOne.Bind(wx.EVT_BUTTON, self.OnClickOne)
        
        self.BtnTwo = wx.Button(self.panel, label = "2", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnTwo.Bind(wx.EVT_BUTTON, self.OnClickTwo)
        
        self.BtnThree = wx.Button(self.panel, label = "3", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnThree.Bind(wx.EVT_BUTTON, self.OnClickThree)
        
        self.BtnFour = wx.Button(self.panel, label = "4", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnFour.Bind(wx.EVT_BUTTON, self.OnClickFour)
        
        self.BtnFive = wx.Button(self.panel, label = "5", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnFive.Bind(wx.EVT_BUTTON, self.OnClickFive)
        
        self.BtnSix = wx.Button(self.panel, label = "6", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnSix.Bind(wx.EVT_BUTTON, self.OnClickSix)
        
        self.BtnSeven = wx.Button(self.panel, label = "7", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnSeven.Bind(wx.EVT_BUTTON, self.OnClickSeven)
        
        self.BtnEight = wx.Button(self.panel, label = "8", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnEight.Bind(wx.EVT_BUTTON, self.OnClickEight)
        
        self.BtnNine = wx.Button(self.panel, label = "9", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnNine.Bind(wx.EVT_BUTTON, self.OnClickNine)
        
        self.BtnTen = wx.Button(self.panel, label = "10", pos = (random.randint(50,250),random.randint(35,175)), size = (100,20))
        
        self.BtnTen.Bind(wx.EVT_BUTTON, self.OnClickTen)
        
        self.BtnTwo.Show(False)
        
        self.BtnThree.Show(False)
        
        self.BtnFour.Show(False)
        
        self.BtnFive.Show(False)
        
        self.BtnSix.Show(False)
        
        self.BtnSeven.Show(False)
        
        self.BtnEight.Show(False)
        
        self.BtnNine.Show(False)
        
        self.BtnTen.Show(False)
        
        
    def OnClickOne(self, e):
        
        self.timeone = time.time()
        
        self.BtnOne.Show(False)
        
        self.BtnTwo.Show(True)
        
        
    def OnClickTwo(self, e):
        
        self.BtnTwo.Show(False)
        
        self.BtnThree.Show(True)
    
    
    def OnClickThree(self, e):
        
        self.BtnThree.Show(False)
        
        self.BtnFour.Show(True)
    
    
    def OnClickFour(self, e):
        
        self.BtnFour.Show(False)
        
        self.BtnFive.Show(True)
    
    
    def OnClickFive(self, e):
        
        self.BtnFive.Show(False)
        
        self.BtnSix.Show(True)
    
    
    def OnClickSix(self, e):
        
        self.BtnSix.Show(False)
        
        self.BtnSeven.Show(True)
    
    
    def OnClickSeven(self, e):
        
        self.BtnSeven.Show(False)
        
        self.BtnEight.Show(True)
    
    
    def OnClickEight(self, e):
        
        self.BtnEight.Show(False)
        
        self.BtnNine.Show(True)
    
    
    def OnClickNine(self, e):
        
        self.BtnNine.Show(False)
        
        self.BtnTen.Show(True)
    
    
    def OnClickTen(self, e):
        
        self.BtnTen.Show(False)
        
        self.endtime = time.time()
        
        result =round(self.endtime-self.timeone)
        
        result = str(result)
        
        heading = wx.StaticText(self.panel, label = "you finished the ten button race! your time was:", pos=(60,15))
        
        heading2 = wx.StaticText(self.panel, label = result, pos = (150,45))
        
        heading3 = wx.StaticText(self.panel, label = "seconds", pos = (175,45))



app = wx.App(False)

frame = NewFrame(None)

frame.Show()

app.MainLoop()