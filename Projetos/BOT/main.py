import pyautogui
import time
import random

imagens = [
    'E:\\Programação\\Python\\Projetos\\BOT\\like.png',
    'E:\\Programação\\Python\\Projetos\\BOT\\deslike.png'
]

tempo = [1,2,3,4]

procurar = "sim"

while procurar == "sim":
    try:
        imagem_escolhida = random.choice(imagens)
        img = pyautogui.locateCenterOnScreen(imagem_escolhida, confidence=0.85)
        pyautogui.click(img.x, img.y)
        tempoescolhido = random.choice(tempo)
        time.sleep(tempoescolhido)
    except:
        time.sleep(1)
        print("não encontrei")
        try:
            img2 = pyautogui.locateCenterOnScreen('E:\\Programação\\Python\\Projetos\\BOT\\baixar.png', confidence=0.85)
            i=0
            while i != 13:
                pyautogui.click(img2.x, img2.y)
                i+=1
        except:
            time.sleep(1)
            pyautogui.press('esc')