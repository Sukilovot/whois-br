import PySimpleGUI as sg

def error():
    layout = [
        [sg.Text("WHOIS BR")],
        [sg.Text("Dominio nao encontrado ou algum erro aconteceu.\nTente novamente")],
        [sg.Button("Sair")]
    ]

    window = sg.Window("Whois BR", layout, icon="favicon.ico")

    while True:
        event, values = window.read()

        if event == "Sair":
            break

    window.close()