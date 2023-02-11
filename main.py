# from tkinter import *
# class Application:
#     def __init__(self, master=None):
#         self.widget1 = Frame(master)
#         self.widget1.pack()
#         self.msg = Label(self.widget1, text="Primeiro widget feito em python")
#         self.msg.pack ()
# root = Tk()
# Application(root)
# root.mainloop()
# widget = Tk()
# widget.title("Meu primeiro app PY")
# widget.mainloop()

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")


class Application(App):
    def build(self):
        return GUI
 
    
Application().run()