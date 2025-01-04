from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def buold(self):
        return MDLabel(text="Welcome to roshan",halign=" center ")
if __name__ == '__main__':
    Main_App().run()
    