#coding: utf8

#Tkinter nome da biblioteca 
#tk interface grafica

import tkinter 

janela = tkinter.Tk(); #ultilizar o sistema tk #janela é referencia para instancia de tk

janela.title("janela principal") #titulo da janela

janela["bg"] = "lightgreen" #alterar a chave bg do dicionario janela | toda janela é um dicionario
##ou
janela["background"] = "lightblue" #alterar a chave bg do dicionario janela | toda janela é um dicionario

#Largura x Altura + Distancia da esquerda + distancia da Direita
#LxA + Eesquerda + Topo #parametros podem ser ocultados #pixel
janela.geometry("500x300+500+300") #edição de tamanho

janela.mainloop() #executa a applicação #laço de repetição executado enquanto a exibição


