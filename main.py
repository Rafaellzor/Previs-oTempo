
import requests
from tkinter import *

import tkinter as tk
from tkinter import ttk

API_KEY = "5d5a5cb24e05732757924affa7ec9e31"
cidade = "curitiba"
LINK = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

def buscar():
    requisicao = requests.get(LINK)
    requisicao_dic = requisicao.json()

    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15

    #print(descricao, f"{temperatura}°C")
    exibir_clima["text"] = temperatura, descricao

janela = Tk()
janela.title("Previsão do Tempo")

instrucao = Label(janela, text="Clique para saber o clima atual de sua região")
instrucao.grid(column=0, row=0, padx=10, pady=20)

botao = Button(janela, text="BUSCAR", command=buscar)
botao.grid(column=0, row=1)

exibir_clima = Label(janela, text="")
exibir_clima.grid(column=0, row=2, padx=5, pady=5)

janela.mainloop()

