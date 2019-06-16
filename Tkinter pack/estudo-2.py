#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="RIGHT", bg="lightgreen") 
lb1.pack(side="right")
#ordem de ultilização do pack muda a ordem de exibição
lb2 = Label(janela, text="LEFT", bg="red") 
lb2.pack(side="left")

lb3 = Label(janela, text="BOTTOM", bg="#008B8B") 
lb3.pack(side="bottom")

lb4 = Label(janela, text="TOP", bg="lightblue") 
lb4.pack(side="top")
#___________________________________________________Labels

janela["bg"] = "lightgray"
janela.geometry("400x300+200+200")
janela.mainloop();

