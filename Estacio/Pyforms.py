# import pyforms
# from pyforms.basewidget import BaseWidget
# from pyforms.controls import ControlText
# from pyforms.controls import ControlButton

# class ExemploSimples(BaseWidget):

#     def __init__(self):
#         super(ExemploSimples,self).__init__('ExemploSimples')
#         #Definition of the forms fields
#         self._nome = ControlText('Nome', 'Default value')
#         self._sobrename = ControlText('Sobrenome')
#         self._nomeCompleto = ControlText('Nome completo')
#         self._button = ControlButton('Pressione o Botão')


# #Execute the application
# if __name__ == " __main__":
#     from pyforms import start_app
#     start_app(ExemploSimples)

# import tkinter 
# tkinter._test()

# from flexx import flx
# class Exemplo(flx.Widget):

#     def init(self):
#         flx.Button(text='Olá')
#         flx.Button(text='Mundo')

# if __name__ == '__main__':
#     a = flx.App(Exemplo, title='Flexx demonstração')
#     m = a.launch()
#     flx.run()

# from cefpython3 import cefpython as cef
# import platform
# import sys

# def main():
#     check_versions()
#     sys.excepthook = cef.ExceptHook # To shutdown all CEF processes on error
#     cef.Initialize()
#     cef.CreateBrowserSync(url=" https://www.google.com/",window_title="Olá, mundo! Este é o primeiro exemplo do CEF python") 
#     cef.MessageLoop() 
#     cef.Shutdown()

# def check_versions(): 
#     ver=cef.GetVersion()
#     print("[hello_world.py] CEF python {ver}".format(ver=ver["version"]))
#     print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
#     print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
#     print("[hello_world.py] python {ver} {arch}".format(ver=platform.python_version(),arch=platform.architecture()[0])) assert cef.__version__>= "57.0", "CEF python v57.0+ required to run this"
    
# if __name__ == '__main__':
#     main()

# from kivy.app import App
# from kivy.uix.button import Button

# class ExemploApp(App):
#     def build(self):
#         return Button(text='Olá, Mundo!')


# import pyautogui
# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.moveTo(100, 150)
# pyautogui.click()
# pyautogui.click(100, 200)
# pyautogui.move(0, 10)
# pyautogui.doubleClick()
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# pyautogui.write('Olá, Mundo!', interval=0.25)
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.press(['left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.alert('Esta é a mensagem para Tela.')


# import PySimpleGUI as sg

# sg.theme('DarkAmber')

# layout = [ [sg.Text('Texto na linha 1')],
#   [sg.Text('Entre com um texto na linha 2'), sg.InputText()],
#   [sg.Button('Ok'), sg.Button('Cancel')] ]
# window = sg.Window('Bem-Vindo ao PySimpleGUI', layout)

# while True:
#   event, values = window.read()
#   if event == sg.WIN_CLOSED or event == 'Cancel':
#     break
#   print('Você entrou com: ', values[0])

# window.close()

