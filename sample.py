#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

Config.set('graphics','fullscrean',"auto")

class AikotobaWidget(Screen):
    def __init__(self, *args, **kwargs):
        super(AikotobaWidget, self).__init__(*args, **kwargs)

sm = ScreenManager()
class PongApp(App):
    def build(self):
        sm.add_widget(AikotobaWidget(name='prewidget'))
        sm.current = 'prewidget'
        return sm

if __name__ == '__main__':
    PongApp().run()
