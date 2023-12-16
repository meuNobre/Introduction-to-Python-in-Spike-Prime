
from hub import light, light_matrix, button, port
import motor_pair, time, motor, runloop, math
import color

#Variaveis
velocidade = 500 #Padroniza a velocidade para ser usada
toque = 0
re = "Ré"
frente = "frente"
direita = "direita"
esquerda = 'esquerda'

#Funções

def Definicao(port1, port2):
        motor_pair.pair(motor_pair.PAIR_1, port1, port2)

def ButtonPressionado():
    return button.pressed(button.LEFT) > 0 

def Andar(direcao: str, tempo: int, orientacao: int, velocidade: int):
        if(direcao == 'frente'): #Se quando a função for chamada, a direcao for = 'frente'
            motor_pair.move_for_time(motor_pair.PAIR_1, tempo, orientacao, velocity=velocidade * 1) #Andar Reto/Em frente
        elif(direcao == 'Ré'): #Senão se quando a função for chamada, a direcao for = 'Ré'
            motor_pair.move_for_time(motor_pair.PAIR_1, tempo, orientacao, velocity=velocidade * -1) #Andar para trás/Em ré
        #As velocidades multiplicadas por 1 ou -1 servem para determinar a direção sendo : positiva = Reto; Negativa = Ré
def Giro(direcao: str):
        if (direcao == direita): #Se quando a função for chamada, a direcao for = 'direita'
            motor_pair.move_tank_for_time(motor_pair.PAIR_1, 500, 0, 670) #Gire a 90 Graus a direita

        elif(direcao == esquerda): #Senão se quando a função for chamada, a direcao for = 'esquerda'
            motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 500, 670) #Gire a 90 Graus a Esquerda

async def main():
    global toque; #Permite alterar a variavel dentro da função
    light.color(light.POWER, color.GREEN) #Mudar a cor do botão do play
    light.color(light.CONNECT, color.YELLOW) #Mudar cor do botão do bluetooth
    
    Definicao(port.A, port.B) #Definir motores de movimento
    
    while True:
        while not ButtonPressionado():#Se Button não estiver pressionado:
            await runloop.sleep_ms(1)#Espere.
        while ButtonPressionado():
            await runloop.sleep_ms(1)
        toque += 1                    #Quando for pressionado, adicione um á variavél.
        if (toque == 1): #Caso toque seja = 1; Rode:
            light_matrix.write("1.1") #Escreva no Hub "1.1"
            Andar('frente', 1000,0, velocidade)
            await runloop.sleep_ms(1000)
            await motor.run_for_degrees(port.D, -170, velocidade)
            runloop.sleep_ms(1000)
            Andar(frente, 1980,0, velocidade)
            await runloop.sleep_ms(2000)
            Andar(re, 2500, 0, velocidade)
            await runloop.sleep_ms(1)
        if (toque == 2): #Caso toque seja igual a 2, Rode:
            light_matrix.write("1.2") #Escreva no Hub "1.2"
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 550, -15, velocity=velocidade)
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1300, 50, velocity=1000)
            Andar(re, 3000, 0, velocidade)
runloop.run(main())