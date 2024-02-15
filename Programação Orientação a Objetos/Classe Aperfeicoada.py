from hub import light_matrix, port, sound, button
import motor, motor_pair, runloop

frente = 'Frente'
re = 'Re'
subir = 'subir'
descer = 'descer'


class Robo:

    #Iniciar
    def __init__(self):
        self.velocidade = 0
        self.velocidadedoanexo = 0
    
    #Definir Motores
    async def DefinirMotores(self, port1:int, port2:int):
        motor_pair.pair(motor_pair.PAIR_1, port1, port2)
    
    #Definição de Velocidade
    async def DefinirVelocidade(self, velocidade):
        self.velocidade = velocidade * 10
    
    #Definição da Velocidade do Anexo
    async def DefinirVelocityA(self, velocidade):
        self.velocidadedoanexo = velocidade * 10

    #Locomoção
    async def Locomover(self, direcao, duracao, orientacao):
        #Mover Reto
        if direcao == 'Frente':
            await motor_pair.move_for_time(motor_pair.PAIR_1, duracao, orientacao, velocity= self.velocidade * 1)

        #Mover em ré
        if direcao == 'Re':
            await motor_pair.move_for_time(motor_pair.PAIR_1, duracao, orientacao, velocity= self.velocidade * -1)
    
    #Mover Motores - Prioridade a Anexos
    async def MoverMotor(self, direcao: str, port1: int, duracao:int):
        #Subir Anexo/Direita
        if direcao == 'subir':
            await motor.run_for_time(port1, duracao, self.velocidadedoanexo * 1)
        
        #Descer Anexo/Esquerda
        if direcao == 'descer':
            await motor.run_for_time(port1, duracao, self.velocidadedoanexo * -1)
    
    #Parar de Locomover
    async def PararDeMover(self):
        motor_pair.stop(motor_pair.PAIR_1)

#Instância
spike = Robo()

async def main():

    await spike.Locomover(frente,1000,0)

runloop.run(main())
