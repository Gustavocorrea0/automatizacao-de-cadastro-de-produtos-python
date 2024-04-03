import pyautogui
from time import sleep

# Criar novo usuario
pyautogui.click(704, 442, duration=0.5)

pyautogui.click(701, 384, duration=0.5)
pyautogui.write('admin')

pyautogui.click(680, 411, duration=0.5)
pyautogui.write('123456')

pyautogui.click(665, 440, duration=2)

# Clicar e Digitar usuario
#         - Coordenadas | Duracao
pyautogui.click(771, 387, duration=2)
pyautogui.write('admin')

# Clicar e Digitar senha
pyautogui.click(675, 411, duration=2)
pyautogui.write('123456')

# Clicar em Entrar
pyautogui.click(593, 441, duration=2)


# Abrir arquivos
#       Nome do Arquivo | Tipo: Leitura | Nome da atividade
with open('produtos.txt', 'r') as arquivo:
    # Pegar dados
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        # Clicar e Digitar o produto
        pyautogui.click(392, 372, duration=0.5)
        pyautogui.write(produto)

        pyautogui.click(391, 398, duration=0.5)
        pyautogui.write(quantidade)

        pyautogui.click(396, 426, duration=0.5)
        pyautogui.write(preco)

        pyautogui.click(323, 578, duration=0.5)
        sleep(1)

pyautogui.click(383, 584, duration=2)
