from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color, Line
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class Main(Screen):
	draw = ObjectProperty(None)

class About(Screen):
	pass

class Manager(ScreenManager):
	mgr = ObjectProperty(None)

	def cleaner(self):
		self.mgr.draw.clean()


class MyPaintWidget(Widget):

	def clean(self):
		self.canvas.clear()
    
	def on_touch_down(self, touch):
		# self.rect.pos = touch.pos
		color = (random(),random(),random())
		with self.canvas:
			Color(*color)
			Ellipse(pos=(touch.x, touch.y), size=(20,20))
			touch.ud['line'] = Line(points=(touch.x, touch.y))

	def on_touch_move(self, touch):
		# self.rect.pos = touch.pos
		touch.ud['line'].points += [touch.x, touch.y]
    	

main_style = Builder.load_file("ms_paint.kv")

class MyPaintApp(App):
	def build(self):
		return main_style


if __name__ == '__main__':
    MyPaintApp().run()