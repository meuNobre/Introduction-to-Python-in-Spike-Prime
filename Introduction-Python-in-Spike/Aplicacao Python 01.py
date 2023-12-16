from hub import port, button
import runloop, motor, motor_pair, force_sensor, time

#Definição de Funções

def DefinirMotores(motoresquerdo: int, motordireito: int, sensor_de_toque:int):
    motor_pair.pair(motor_pair.PAIR_1, motoresquerdo, motordireito)
    force_sensor.force(sensor_de_toque)

def Esperar(espera: int):
    time.sleep_ms(espera)

def Andar(velocidadeesquerdo: int, velocidadedireito: int, tempo: int):
    motor_pair.move_tank_for_time(motor_pair.PAIR_1, velocidadeesquerdo, velocidadedireito, tempo)

def Direita90():
    motor_pair.move_tank_for_time(motor_pair.PAIR_1, 500, 0, 670)

def Esquerda90():
    motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 500, 670)

def ButtonPressionado():
    
    return button.pressed(button.LEFT) > 0

async def main():
   
   #Variaveis
   toque = 0

   #Iniciação
   DefinirMotores(port.B, port.D, port.A) #Defina a porta dos motores e sensores
   
   #Movimentos/Lançamentos:
   Andar(1000, 1000, 1500)
   Esperar(1500)
   motor_pair.stop(motor_pair.PAIR_1)
   motor.run(port.F, 500)
   Esperar(500)
   motor.stop(port.F)
   Andar(-1000, -1000, 1500)
   
   while True: #Laço de repetição
    
    
    #Se o sensor de toque for pressinado, adicione uma a variavel 'toque'.
    
    
    if force_sensor.pressed(port.A) == True: #Condicional
        toque += 1
    
    if (toque >= 1): #se a variavel toque for maior ou igual a 1, rode a programação a seguir.
        Esperar(1000)
        Andar(500,500,1000)
        Esperar(1000)
        Andar(-500,-500,600)
        Esperar(600)
        Andar(550, 400, 1000)
        Esperar(1000)
        Andar(500,500, 1000)
        Esperar(1000)
        Andar(300, 500,1000)
        Esperar(100)
        Andar(960,1000,6000)
        exit() 

        
runloop.run(main())
