from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 2 # columns
		self.add_widget(Label(text="You'r Email:"))	 # add label widget
		self.add_widget(TextInput(hint_text="Enter your Email", multiline=False)) # add text input widget

class MyKivy(App):

	def build(self):
		return MyGrid()

if __name__ == "__main__":
	MyKivy().run()