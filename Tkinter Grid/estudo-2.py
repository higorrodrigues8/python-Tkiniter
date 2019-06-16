#coding: utf8
#GERENCIADOR GRID

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
janela = Tk()
#___________________________________________________Labels
lb1 = Label(janela, text="Login: ") 
lb2 = Label(janela, text="Senha: ")
 
ed1 = Entry(janela, )
ed2 = Entry(janela, )

bt1 = Button(janela, text="confirmar")

lb1.grid(row="0", column="0")
lb2.grid(row="1", column="0") 

ed1.grid(row="0", column="1")
ed2.grid(row="1", column="1")

bt1.grid(row="2", column="1")


#___________________________________________________Labels
janela["bg"] = "lightgray"
janela.geometry("200x100+100+100")
janela.mainloop();

