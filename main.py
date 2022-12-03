import PySimpleGUI as sg
from translate import translate
from response import main
from error import error
import requests

sg.change_look_and_feel("DarkBlue 3")
api_url = "https://brasilapi.com.br/api/registrobr/v1/{}"

layout = [
    [sg.Text("WHOIS BR")],
    [sg.Text("Creditos da API: https://brasilapi.com.br/")],
    [sg.Text("Digite o dominio: "), sg.InputText()],
    [],
    [sg.Button("Pesquisar", key="search"), sg.Button("Sair")]
]

win = sg.Window("Whois BR", layout, icon="favicon.ico")

while True:
    event, values = win.Read()

    if event == "search":
        try:
            str(values[0].replace("https://", "").replace("www.", ""))
            json = translate(requests.get(api_url.format(str(values[0]))).json())
            print(json)
            main(json)
        except:
            error()

    if event == "Sair":
        break

win.close()