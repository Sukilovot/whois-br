import PySimpleGUI as sg

def main(json):
    layout = [
        [sg.Text("WHOIS BR")],
        [sg.Text("Dominio: {}".format(json["fqdn"]))],
        [sg.Text("Status: {}".format(json["status"]))],
        [sg.Text("Hosts: {}".format(json["hosts"]))],
        [sg.Text("Status da publicacao: {}".format(json["publication-status"]))],
        [sg.Text("Expira em: {}".format(json["expires-at"]))],
        [sg.Button("Sair")]
    ]

    window = sg.Window("Whois BR", layout, icon="favicon.ico")

    while True:
        event, values = window.read()

        if event == "Sair":
            break


    window.close()