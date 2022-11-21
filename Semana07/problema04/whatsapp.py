import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class BoxLayout(Widget):
    pass

class WhatsApp(App):
    def build(self):
        return BoxLayout()

if __name__ == "__main__":
    WhatsApp().run()
    