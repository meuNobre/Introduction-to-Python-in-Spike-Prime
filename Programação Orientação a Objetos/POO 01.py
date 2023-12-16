from hub import light_matrix, port
import hub
import runloop, motor, motor_pair, force_sensor

#Variaveis
frente = 'Frente'; re = 'Ré'; 
direita = 'Direita'; esquerda = 'Esquerda'
subir = 'Cima'; descer = 'Baixo'

class Robo: 
    
    async def __init__(self): #Primeira função a ser criada na classe é o __init__: serve para dizer as caracteristicas/atributos da classe que são definidas ao iniciar/instanciar ela.
        self.velocidade = 0 #Self dita que aquilo é uma caracteristica DA classe e não apenas uma variavel declarada dentro dela, 
        self.anexovelocity = 0 #no caso self.velocidade pode ser chamado novamente por exemplo 'print(spike.velocidade)' e isso retornará a caracteristica armazenada na velocidade, no caso 0.
    
    async def Velocidade(self, velocidade): 
        self.velocidade = velocidade * 10
    
    async def AnexoVelocity(self, velocidade: int):
        self.anexovelocity = velocidade * 10 #A multiplicação por 10 é para se aproximar a programação com blocos, onde 100% DE Velocidade seria 1000 no python. 
                                             #Então ao colocar 100 quando a função for chamada, ela se tornará 1000.

    async def Motores(self, port1:int , port2: int):
        motor_pair.pair(motor_pair.PAIR_1, port1, port2)
    
    async def toque(self, sensor: int):
        force_sensor.force = sensor
    
    async def Andar(self, direcao: str, duracao: int, orientacao: int): #todas as funções dentro da classe devem ser chamadas com o self, para encaixar elas como algo que faz parte da classe e que pode ser chamada depois.
        if direcao == 'Frente': #No caso, mais tarde poderia ser chamada essa como, spike.Andar(direcao, duracao, orientacao) e encaixando os parametros necessarios para a função
            motor_pair.move_for_time(motor_pair.PAIR_1, duracao, orientacao, velocity= self.velocidade * 1)
        elif direcao == 'Ré':
            motor_pair.move_for_time(motor_pair.PAIR_1, duracao, orientacao, velocity= self.velocidade * -1)
    
    async def MovimentoDuasRodas(self, velocidadeEsquerda: int, velocidadeDireita: int, duracao: int):
        motor_pair.move_tank_for_time(motor_pair.PAIR_1, velocidadeEsquerda, velocidadeDireita, duracao)        
    
    async def GiroReto(self, direcao: str):
        if (direcao == 'Direita'):
            motor_pair.move_tank_for_time(motor_pair.PAIR_1, 500, 0, 670)
        elif(direcao == 'Esquerda'):
            motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 500, 670)

    async def Anexo(self, duracao: int, direction):
        if direction == 'Cima':
            motor.run_for_time(port.C, duracao, velocity=self.anexovelocity * 1)
        if direction == 'Baixo':
            motor.run_for_time(port.C, duracao, velocity=self.anexovelocity * -1)

spike = Robo() #Criando instancia da classe Robo. -> Simplificando tudo

async def main():

    await spike.Motores(port.A, port.B) #Defina o par de motores.
    await spike.Velocidade(100) #-> Defina a velocidade 
    await spike.toque(port.C) #Defina a porta do Sensor de Toque.
    await spike.Andar(frente, 1000, 0) #Ande para frente.
    await spike.MovimentoDuasRodas(1000, 800,1200) #Ande como um tanque nas velocidades definidas
    await spike.GiroReto(direita) #Gire 90 Graus para Direita.
    

runloop.run(main())
