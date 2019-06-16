#coding: utf8
#GERENCIADOR PLACE

from tkinter import * #ou Tkinter em verões -3x

def bt_click():
    print("bt_click");
    lb["text"] = "funcionou!!!"





janela = Tk()
           
bt = Button(janela, width=20, text="OK", command=bt_click )
bt.place(x=80, y=100) 


lb = Label(janela, text="teste")
lb.place(x=100,y=150)




                 
#  → W x H + L + T
janela.geometry("300x300+200+200")

janela.mainloop();

  


