import pyautogui
from time import sleep

# Clicar e Digitar usuario
#         - Coordenadas | Duracao
pyautogui.click(771,387, duration=2)
pyautogui.write('gustavo')

# Clicar e Digitar senha
pyautogui.click(675,411, duration=2)
pyautogui.write('123456')

# Clicar em Entrar
pyautogui.click(593,441, duration=2)