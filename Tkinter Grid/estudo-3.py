#coding: utf8
#GERENCIADOR GRID
#propriedade stick


from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="ESPAÇO", width="15", height='3', bg="lightblue") 
lb2 = Label(janela, text="HORIZONTAL", bg="lightgreen")
lb3 = Label(janela, text="VERTICAL", bg="gray")

lb1.grid(row="0", column="0")
lb2.grid(row="1", column="0", sticky="E") 
lb3.grid(row="0", column="1") 

#___________________________________________________Labels
janela["bg"] = "lightgray"
janela.geometry("200x100+100+100")
janela.mainloop();

