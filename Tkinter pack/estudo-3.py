#coding: utf8
#GERENCIADOR PACK

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="SIDE 1", bg="lightgreen") 
lb1.pack(side="right")
#ordem de ultilização do pack muda a ordem de exibição
lb2 = Label(janela, text="SIDE 2", bg="red") 
lb2.pack(side="left")
#por padrao a propriedade side é igual à top
lb3 = Label(janela, text="ANCHOR 1", bg="#008B8B") 
lb3.pack(anchor='w')

lb4 = Label(janela, text="ANCHOR 2", bg="lightblue") 
lb4.pack(anchor='w')
#___________________________________________________Labels

janela["bg"] = "lightgray"
janela.geometry("400x300+200+200")
janela.mainloop();

