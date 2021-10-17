import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from Brute_force import Brute_force

class Sistema_brute_force:
    @staticmethod 
    def __janela_principal():
        
        layout = [
            [sg.Text('Insira a senha:', justification='left'), sg.Input(key='senha')],
            [sg.Button('Enviar'), sg.Button('Cancelar')]
        ]

        return sg.Window(title='Brute force', layout=layout)
    

    def window_init(self):
        window = self.__janela_principal()

        while True:
            event, values = window.read()

            if event == 'Cancelar' or event == WINDOW_CLOSED:
                break

            elif event == 'Enviar':
                try: 
                    brute_force = Brute_force(values['senha'])
                except Exception as E:
                    sg.popup(E)
                else:
                    sg.popup(f'Número de tentativas: {brute_force.tentativas} vezes ')


if __name__ == '__main__':
    brute_force = Sistema_brute_force()
    brute_force.window_init()
