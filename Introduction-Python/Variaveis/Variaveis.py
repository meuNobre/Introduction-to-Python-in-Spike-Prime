from hub import light_matrix
import runloop

async def main():
    #Variaveis
    '''Variaveis são espaços vazios a serem preenchidos com algum dado, como se fosse uma caixa sendo preenchida por algum objeto. Tipos de variaveis:
    -> Int utilizado para números inteiros(1,2,3); (Variavel de numero)
    -> Float utilizado para numeros decimais(3,1415, etc); (Variavel de Numero)
    -> String utilizado para textos/palavras(utilizado entre aspas 'Nobre') (Variavel de Texto)
    -> Bool utilizado para condicionais de True or False. (Variavel de verdadeiro ou falso) '''
    #Segue os exemplos:
    idade = 0 #Variavel do Tipo Int
    pi = 3,1415 #Variavel do Tipo Float
    nome = 'Nobre' #Variavel do tipo String
    toque = True #Variavel do tipo Bool

    #Podemos mostrar o que temos armazenado nessa variavél, no caso o dado armazenado usando o print
    print(idade)
    print(pi)
    print(nome)
    print(toque)


runloop.run(main())
