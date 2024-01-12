from hub import light_matrix, port
import runloop
import motor_pair
import motor 

#Variaveis
frente = 'Frente'
re = 'Ré'
direita = 'Direita'
esquerda = 'Esquerda'
subir = 'Cima'
descer = 'Baixo'

class Robo:

    def __init__(self): #Primeira função a ser criada na classe é o __init__: serve para dizer as caracteristicas/atributos da classe que são definidas ao iniciar/instanciar ela.
        self.velocidade = 0 #Self dita que aquilo é uma caracteristica DA classe e não apenas uma variavel declarada dentro dela,
        self.anexovelocity = 0 #no caso self.velocidade pode ser chamado novamente por exemplo 'print(spike.velocidade)' e isso retornará a caracteristica armazenada na velocidade, no caso 0.

    async def Velocidade(self, velocidade):
        self.velocidade = velocidade * 10

    async def AnexoVelocity(self, velocidade: int):
        self.anexovelocity = velocidade * 10 #A multiplicação por 10 é para se aproximar a programação com blocos, onde 100% DE Velocidade seria 1000 no python.
                                            #Então ao colocar 100 quando a função for chamada, ela se tornará 1000.

    async def Motores(self, port1:int , port2: int):
        motor_pair.pair(motor_pair.PAIR_1, port1, port2)

    async def Andar(self, direcao: str, duracao: int, orientacao: int): 
        if direcao == 'Frente':
            await motor_pair.move_for_time(motor_pair.PAIR_1, duracao, orientacao, velocity= self.velocidade * 1)
        elif direcao == 'Ré':
            await motor_pair.move_for_time(motor_pair.PAIR_1, duracao, orientacao, velocity= self.velocidade * -1)

    async def MovimentoDuasRodas(self, velocidadeEsquerda: int, velocidadeDireita: int, duracao: int):
        await motor_pair.move_tank_for_time(motor_pair.PAIR_1, velocidadeEsquerda, velocidadeDireita, duracao)

    async def GiroReto(self, direcao: str):
        if (direcao == 'Direita'):
            await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 500, 0, 670)
        elif(direcao == 'Esquerda'):
            await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 500, 670)
    async def Anexo11(self, duracao: int, direction: str):
        if direction == 'Cima':
            await motor.run_for_time(port.F, duracao, velocity=self.anexovelocity * 1)
        if direction == 'Baixo':
            await motor.run_for_time(port.F, duracao, velocity=self.anexovelocity * -1)
    async def PararDeMovimentar(self):
        motor_pair.stop(motor_pair.PAIR_1)


spike = Robo()

async def main():

    await spike.Motores(port.E, port.A) 
    await spike.Velocidade(100) 
    await spike.AnexoVelocity(75)
    await spike.Andar(frente, 3600, -6)
    await spike.Andar(re, 600, -8)
    await spike.Anexo11(7000, subir)
    await spike.PararDeMovimentar()
    
runloop.run(main())
    