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
import requests

GUI = Builder.load_file("tela.kv")


class Application(App):
    def build(self):
        return GUI
 
    def on_start(self):
        
        self.root.ids["moeda1"].text = f"Dolar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"
        
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL" # URL da api de cotação de moeda
        requisicao = requests.get(link) # request framework responsavel pela requisição webs em que é retornado um JSON
        valor_moeda = requisicao.json()  # o valor da requisição é transformado para dicionário em python
        return valor_moeda[f"{moeda}BRL"]["bid"] 
    
Application().run()