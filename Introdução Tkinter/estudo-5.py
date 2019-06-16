#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verÃµes -3x


janela = Tk() #criando um container do tipo janela
janela.title("") #titulo da janela 
janela.geometry("300x300+200+200") # W x H + L + T

#________________________________________________________#
def button1_click():
    print("button_click1")

def button2_click():
    print("button_click2")

#________________________________________________________#
bt1 = Button(janela, width=20, text="Botão 1", command=button1_click)
bt1.place(x=80, y=100) 

bt2 = Button(janela, width=20, text="Botão 2", command=button2_click)
bt2.place(x=80, y=130)






                 


janela.mainloop();

  


