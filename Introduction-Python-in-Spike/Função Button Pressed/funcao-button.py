from hub import light_matrix,button, sound
import runloop

def esquerdoPressionado():

            return button.pressed(button.LEFT) > 0 #condições do sensor
            # se o botão esquerdo foi pressionado por mais de 0 milissegundos, retorna

async def main():
   print('Hello World!')

async def checkButton():
    #Repita para sempre: se botao esquerdo for pressionado, emita som de beep, senão aguarde.
    while True:
        while not esquerdoPressionado():
            await runloop.sleep_ms(1)
            sound.beep(800,200,1000)
        while esquerdoPressionado():
            await runloop.sleep_ms(1)

runloop.run(main(), checkButton())
