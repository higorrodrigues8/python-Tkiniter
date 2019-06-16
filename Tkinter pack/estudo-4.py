#coding: utf8
#GERENCIADOR PACK
#propriedade fill: expande o side
#por padrao a propriedade side é igual à top
#preenche todo o topo em sentido horizontal
#ordem de ultilização do pack muda a ordem de exibição

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="", bg="white") 
lb1.pack(side="top", fill = 'x') 

lb2 = Label(janela, text=" ", bg="white") 
lb2.pack(side="left", fill = 'y')

lb3 = Label(janela, text=" ", bg="white") 
lb3.pack(side="right", fill = 'y'),

lb4 = Label(janela, text="Horizontal", bg="lightgreen") 
lb4.pack(side="top") 

lb5 = Label(janela, text=" ", bg="white") 
lb5.pack(side="bottom", fill = 'x')


#___________________________________________________Labels

janela["bg"] = "lightgray"
janela.geometry("400x300+200+200")
janela.mainloop();

