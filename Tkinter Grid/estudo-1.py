#coding: utf8
#GERENCIADOR GRID

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="Linha 1", bg="lightblue") 
lb1.grid(row="1", column='1')

lb2 = Label(janela, text="Linha 2", bg="lightgreen") 
lb2.grid(row="2000", column='2000') 
'''
lb3 = Label(janela, text="Linha 3", bg="orange") 
lb3.pack(side="top", fill = 'both', expand='true'),

lb4 = Label(janela, text="Linha 4", bg="black")
lb4.pack(side="top", fill = 'both', expand='true') 

lb5 = Label(janela, text=" ", bg="white") 
lb5.pack(side="bottom", fill = 'x')'''
#___________________________________________________Labels
janela["bg"] = "lightgray"
janela.geometry("500x200+-600+200")
janela.mainloop();

