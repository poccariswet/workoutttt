#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from kivy.lang import Builder
Builder.load_file('pong.kv')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials as SAC

url = 'https://spreadsheets.google.com/feeds'
key = '1pFF43iF-srEzm8tLcPIro7U-OhlkGi7Xku4W09DpRcw'
gss_path = '/Users/soeyu/python/Project/Project_noguchi/asset/gss/noguchi_gss.json'

def Gss_Sheet(x, y):
    scope = [url]
    credentials = SAC.from_json_keyfile_name(gss_path, scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open_by_key(key).sheet1

    return worksheet.cell(x, y).value

class TimerMngObject(object):
    def TimerStart(self):
        self.cyclicTimer = 10
        Clock.schedule_interval(self.cyctim, 1)

    def cyctim(self, dt):
        self.cyclicTimer -= 1
        if(self.cyclicTimer == 0):
            self.TimerTO('dummy')

    def TimerExtension(self):
        self.cyclicTimer = 10

    def TimerTO(self, dt):
        self.cyclicTimer = 10
        papp.SetString()
        sm.current = 'prewidget'

class PreWidget(Screen):
    def nextsc(self):
        timobj.TimerExtension()
        papp.SetString()
        sm.current = 'aikotobawidget'

def randgss():
    scope = [url]
    credentials = SAC.from_json_keyfile_name(gss_path, scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open_by_key(key).sheet1

    values_list = worksheet.col_values(2)
    i = 0
    for v in values_list:
        if v != '':
            i+=1
    r = random.randint(2, i)
    return r


class AikotobaWidget(Screen):
    def __init__(self, *args, **kwargs):
        super(AikotobaWidget, self).__init__(*args, **kwargs)
        timobj.TimerStart()
        r = randgss()
        self.tenpo=Gss_Sheet(r, 2)
        self.aikot=Gss_Sheet(r, 4)
        self.kupon=Gss_Sheet(r, 3)

    def nextsc(self):
        timobj.TimerExtension()
        sm.current = 'prewidget'


sm = ScreenManager()
timobj = TimerMngObject()

class PongApp(App):
    tenpo = StringProperty('')
    aikot = StringProperty('')
    kupon = StringProperty('')
    def build(self):
        sm.add_widget(PreWidget(name='prewidget'))
        sm.add_widget(AikotobaWidget(name='aikotobawidget'))
        sm.current = 'prewidget'
        return sm

    def SetString(self):
        r = randgss()
        self.tenpo = Gss_Sheet(r, 2)
        self.aikot = Gss_Sheet(r, 4)
        self.kupon = Gss_Sheet(r, 3)

papp=PongApp()

if __name__ == "__main__":
    papp.run()
