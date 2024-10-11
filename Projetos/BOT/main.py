import pyautogui
import time
import random
import os

pastaRaiz = os.path.dirname(os.path.abspath(__file__))
imgLike = pastaRaiz + "\\like.png"
imgDeslike = pastaRaiz + "\\deslike.png"
imgBaixar = pastaRaiz + "\\baixar.png"

imagens = [
    imgLike,
    imgDeslike
]

tempo = [2,3]

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
            img2 = pyautogui.locateCenterOnScreen(imgBaixar, confidence=0.85)
            i=0
            while i != 15:
                pyautogui.click(img2.x, img2.y)
                i+=1
        except:
            time.sleep(1)
            pyautogui.press('esc')