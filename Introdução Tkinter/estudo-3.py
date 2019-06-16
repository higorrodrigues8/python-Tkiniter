#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verões -3x

janela = Tk()

lb = Label(janela, text="OPA!") #pai do label: janela
                           #container: janela principal
                           #propriedade texto
                           #label == widget

lb.place(x=100, y=100) #gerenciador de layout: place


                              
#  → W x H + L + T
janela.geometry("300x300+200+200")

janela.mainloop();

  


