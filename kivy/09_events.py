from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MyLayout(FloatLayout):

	btn = ObjectProperty(None)
	
	def on_touch_down(self, touch):
		print(f"TouchDown: {touch}")
		if(touch.pos[0] > self.size[0]/2) and (touch.pos[1] > self.size[1]/2):
			# self.btn.text = "Asefy.com"
			self.btn.background_color = [0.2, 0.7, 0.8, 1]

	def on_touch_up(self, touch):
		print(f"TouchUp: {touch}")
		if(touch.pos[0] > self.size[0]/2) and (touch.pos[1] > self.size[1]/2):
			# self.btn.text = "Asefy.com"
			self.btn.background_color = [0.9, 0.2, 0.3, 1]

	def on_touch_move(self, touch):
		print(f"TouchMove: {touch}")

class designEventApp(App):
	 def build(self):
	 	return MyLayout()

if __name__ == "__main__":
	designEventApp().run()