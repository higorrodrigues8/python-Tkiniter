#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="Label 1", bg="lightgreen") 
lb1.pack()
#ordem de ultilização do pack muda a ordem de exibição
lb2 = Label(janela, text="Label 2", bg="red") 
lb2.pack()

lb3 = Label(janela, text="Label 3", bg="#008B8B") 
lb3.pack()

lb4 = Label(janela, text="Label 4", bg="lightblue") 
lb4.pack()
#___________________________________________________Labels

janela.mainloop();

