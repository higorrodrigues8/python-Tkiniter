#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verÃµes -3x
from functools import *

janela = Tk() #criando um container do tipo janela
janela.title("") #titulo da janela 
janela.geometry("300x300+200+200") # W x H + L + T

#________________________________________________________#
def button_click(botao):
    print(botao["text"])




#________________________________________________________#
bt1 = Button(janela, width=20, text="Botão 1")
bt1["command"] = partial(button_click, bt1) #reescrever uma função com lista de parametros
bt1.place(x=80, y=100) 

bt2 = Button(janela, width=20, text="Botão 2")
bt2["command"] = partial(button_click, bt2)
bt2.place(x=80, y=130)






                 


janela.mainloop();

  


