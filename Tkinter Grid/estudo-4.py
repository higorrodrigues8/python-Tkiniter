#coding: utf8
#GERENCIADOR GRID
#propriedade rowspan qtd de linhas mescladas
#propriedade colownspan qtd de colunas mescladas



from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="", width="15", height=6, bg="lightblue") 
lb2 = Label(janela, text="",width="15", height=6, bg="lightgreen")
lb3 = Label(janela, text="",width="15", height=6, bg="gray")
lb4 = Label(janela, text="",width="15", height=6, bg="yellow")

lb5 = Label(janela, text="", height='3', bg="lightgreen")
lb6 = Label(janela, text="",width="5", bg="pink")

lb1.grid(row="0", column="0")
lb2.grid(row="1", column="0") 
lb3.grid(row="0", column="1") 
lb4.grid(row="1", column="1") 

lb5.grid(row="2", column="0", columnspan='2', sticky=W+E)
lb6.grid(row="0", column="2", rowspan='2', sticky=N+S)

#___________________________________________________Labels
janela["bg"] = "lightgray"
janela.geometry("200x100+100+100")
janela.mainloop();

