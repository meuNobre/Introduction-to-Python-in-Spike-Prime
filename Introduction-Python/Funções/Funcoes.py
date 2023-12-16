from hub import light_matrix, port
import runloop,motor, motor_pair, time
#Funções - São blocos de código que realizam determinadas tarefas que normalmente precisam ser executadas diversas vezes.
#-> Quando surge essa necessidade, para que várias instruções não precisem ser repetidas, elas são agrupadas em uma função.


def Batata(): #Def é utilizado para definir uma função, como já escrito def = definir
        print("batata") #O objetivo da Função batata é printar "batata" no console.

def Hello(name: str): #Str define que o parametro definido deve ser uma string = texto e não um numero(int) por exemplo.

        #Podemos criar parametros para serem adicionados sempre que a função for chamada.
        print("Hello, ", name)
        #No caso, o parametro "name" vai ser definido dentro dos parenteses quando a função for chamada.
async def main():

    #Chamada de Funções
    Batata() #Funções podem ser chamadas colocando as proprias junto a parenteses no main.
    Hello("World") #No caso "World" é o parametro 'name' sendo definido.
    

runloop.run(main())
