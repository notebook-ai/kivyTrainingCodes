from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class Manager(ScreenManager):
	pass

class Main(Screen):
	pass

class Second(Screen):
	pass

style = Builder.load_file("multiscreen_style.kv")

class MyMSApp(App):
	def build(self):
		return style


if __name__ == '__main__':
    MyMSApp().run()