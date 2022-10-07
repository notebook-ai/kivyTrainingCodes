from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color, Line


class MyPaintWidget(Widget):

	# def __init__(self, **kwargs):
	# 	super().__init__(**kwargs)

	# 	with self.canvas:
	# 		Color(0,1,1)
	# 		self.rect = Rectangle(pos=(0, 0), size=(50,30))

    
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
    	


class MyPaintApp(App):
	def build(self):
		return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()