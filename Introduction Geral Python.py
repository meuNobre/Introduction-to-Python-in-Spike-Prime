from hub import light_matrix, port, light, button, sound
import runloop, time, motor, motor_pair, math, random, color, light, force_sensor

#Funções - def é utilizado para definir uma função, como já escrito def = definir
def Função():
    print("batata")

def Hello(name: str): #Str define que o parametro definido deve ser uma string = texto e não um numero(int) por exemplo.

    #Podemos criar parametros para serem adicionados sempre que a função for chamada.
    print("Hello, " + name + "batata") 
    #No caso, o parametro "name" vai ser definido dentro dos parenteses quando a função for chamada.
def Esperar(espera):
    time.sleep_ms(espera)
    #serve para esperar uma quantidade de tempo - definida em ms/milissegundos, no caso acima, 2 segundos(2000 ms).

def Movimento1():
    #Girar um motor por 360 a 720 graus por segundo
    motor.run_for_degrees(port.A, 360, 720)
    # primeiro parametro = porta(motor)
    # segundo parametro = Numero de graus a girar
    # terceiro parametro = A velocidade do giro em graus por segundo
        # 360 = 1 rotação
        # 720 = 2 rotações
        # Resumo do comando:
            #Girar 360 por 720 por segundo = vai girar á 360 numa velocidade que giraria 720 graus em 1 segundo.

def movimento2():
    motor.run_for_degrees(port.A, 360, 720)
    motor.run_for_degrees(port.B, 360, 720)
    #Os dois motores irão girar ao mesmo tempo pois o "run for degress" é aguardável. Ou seja:
    #Aguardar o final da operação é opcional. Por padrão se continua para a próxima linha de código enquanto o aguardavel é executado até sua conclusão.
    #Isso possibilita a execução de diversos comandos ao mesmo tempo.

def esquerdoPressionado():
    return button.pressed(button.LEFT) > 0


async def main():

    #variaveis
    idade = 0 #Variavel do tipo int
    pi = 3,1415 #Variavel do tipo Float
    nome = 'Miguel' #Variavel do tipo String
    toque = True #Variavel do tipo Bool
    pi2 = math.pi
    velocidade = 720 #Padroniza a velocidade, dando á variavel um numero fixo e auxiliando a sempre utilizar o mesmo valor.
    grau = 360
    #Int usado para números inteiros, float para numeros decimais, String para textos e bool para condicionais de True or False.
    print(velocidade and grau and pi and pi2)
    
    #Chamada de Funções
    Função() #Funções podem ser chamadas colocando as proprias junto a parenteses no main.
    Hello("World") #No caso "World" é o parametro 'name' sendo definido.
    Esperar(2000) #O esperar nesse caso é para que o Movimento1 não rode em conjunto com as outras funções e sim aguarde a finalização delas. 
    Movimento1()

    #Para evitar comandos serem executados de forma seguida eles podem ser chamados juntos ao await:
    await motor.run_for_degrees(port.B, grau, velocidade)
    await motor.run_for_degrees(port.B, -grau, velocidade)
    #Isso faz com que ele espere a conclusão da primeira linha para realizar a próxima.
    #Não funciona com funções(pode ser contornada via criação de classes: Tópico numa anotação de estudos futura)

    #Laços de repetição
    #for i in range (3) = repetir 3 vezes.
    #while True = repetir para sempre.

    for i in range(3):
        velocidade = velocidade * 90
        await motor.run_for_degrees(port.A, grau, velocidade)
        #A cada vez executada, a velocidade vai ser multiplicada por 90, aumentando a velocidade de movimento do giro
        #A cada execução.
    
async def Aleatorio():
    #Aleatoridade:
    # random.randint = int || Numeros aleatorios num intervalo
    # random.choice = str || Escolha aleatoria de uma lista

    print(random.randint(500,1500)) #Gerar um numero aleatorio entre 500 e 1500
    sleep_time = random.randint(1000, 1500)
    time.sleep_ms(sleep_time)
    colors = [color.RED, color.GREEN, color.BLUE] #Lista > Tem que ser colocada entre colchetes

    while True:
        for i in range(5):
            random_color = random.choice(colors) #Escolha uma cor aleatoria da lista
            light.color(light.POWER, random_color)
            time.sleep_ms(sleep_time)
            light.color(light.POWER, color.WHITE)

        force = force_sensor.force(port.A)
        print(force)
        # if(force >= 10, force_sensor.pressed == True):
        #    time.sleep_ms(1000)
        #    motor_pair.move_for_time(motor_pair.PAIR_1, 100,100)
        #    print("iniciando")

async def checkButton():
    while True:
        while not esquerdoPressionado():
            await runloop.sleep_ms(1)
            sound.beep(800,200,1000)
        while esquerdoPressionado():
            await runloop.sleep_ms(1)

runloop.run(main(),checkButton(), Aleatorio())