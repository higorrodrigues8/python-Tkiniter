#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *
#___________________________________________________Função Botão
def bt_onclick():
    x = ed1.get() #pega valor do entry1
    y = ed2.get() #pega valor do entry2
    soma = int(x) + int(y)
    lb3["text"] = "O resultado da soma é: \n" + str(soma) #atribui valor da variavel soma ao label
#___________________________________________________Janela
janela = Tk() #criando um container do tipo janela
janela.title("") #titulo da janela 
janela.geometry("300x300+200+200") # W x H + L + T
#___________________________________________________Entry1
lb1 = Label(janela, text="Número 1:")
lb1.place(x=16,y=100)

ed1 = Entry(janela)     #caixa de entrada
ed1.place(x=80, y=100)  #caixa de entrada
#___________________________________________________Entry2
lb2 = Label(janela, text="Número 2:")
lb2.place(x=16,y=130)

ed2 = Entry(janela)     #caixa de entrada
ed2.place(x=80, y=130) #caixa de entrada
#___________________________________________________Label 3 (resposta)
lb3 = Label(janela, text='')
lb3.place(x=80,y=180)
#___________________________________________________Botão
bt = Button(janela, width=5, text="OK", command=bt_onclick)
bt.place(x=160, y=220)
#___________________________________________________Janela loop


janela.mainloop();

