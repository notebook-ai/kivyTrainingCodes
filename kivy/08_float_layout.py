from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MyLayout(FloatLayout):
	pass

class designFloatLayoutApp(App):
	 def build(self):
	 	return MyLayout()

if __name__ == "__main__":
	designFloatLayoutApp().run()