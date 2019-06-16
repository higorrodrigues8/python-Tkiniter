#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
#___________________________________________________Função Botão
def bt_onclick():
    print(ed.get()) #pega valor do entry
    lb["text"] = ed.get() #atribui valor ao label
#___________________________________________________Janela

janela = Tk() #criando um container do tipo janela
janela.title("") #titulo da janela 
janela.geometry("300x300+200+200") # W x H + L + T
#___________________________________________________Entry
ed = Entry(janela)     #caixa de entrada
ed.place(x=80, y=100)  #caixa de entrada
#___________________________________________________Label
lb = Label(janela, text="Label")
lb.place(x=100, y=200)
#___________________________________________________Botão
bt = Button(janela, width=5, text="OK", command=bt_onclick)
bt.place(x=160, y=130)
#___________________________________________________Janela loop

janela.mainloop();

