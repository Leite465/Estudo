#importando a biblioteca para operações matematicas
import math
#definindo alguns valores para 0
res=0
num1=0
num2=0
reps=0
r=int(0)
#menu de escolha simples
print("1-Soma")
print("2-subtração")
print("3-multiplicação")
print("4-divisão")
print("5-raiz")
print("6-potenciação")
print("7-seno")
print("8-coseno")
print("9-tangente")
desc=int(input("Qual operação deseja realizar? "))

while r==0:
    #menu de escolha em caso de repetição
    if reps==1:
        print("1-Soma")
        print("2-subtração")
        print("3-multiplicação")
        print("4-divisão")
        print("5-raiz")
        print("6-potenciação")
        print("7-seno")
        print("8-coseno")
        print("9-tangente")

        desc=int(input("Qual operação deseja realizar? "))
    #soma
    if desc==1:
        num1=int(input("qual é o primeiro número? "))
        num2=int(input("qual é o segundo número? "))

        res=num1+num2

        print("O resultado da operação é {}!".format(res))
    #subtração
    elif desc==2:
        num1 = int(input("qual é o primeiro número? "))
        num2 = int(input("qual é o segundo número? "))

        res = num1 - num2

        print("O resultado da operação é {}!".format(res))
    #multiplicação
    elif desc==3:
        num1 = int(input("qual é o primeiro número? "))
        num2 = int(input("qual é o segundo número? "))

        res = num1 * num2

        print("O resultado da operação é {}!".format(res))
    #divisão
    elif desc==4:
        num1 = int(input("qual é o primeiro número? "))
        num2 = int(input("qual é o segundo número? "))

        res = num1 / num2

        print("O resultado da operação é {}!".format(res))
    #raiz quadrada com a função sqrt da biblioteca math
    elif desc==5:
        num1 = int(input("qual é o número? "))

        res = math.sqrt(num1)

        print("O resutado da operação é {}!".format(res))
    #potenciação
    elif desc==6:
        num1 = int(input("qual é o número a ser elevado? "))
        num2 = int(input("qual é o número a se elevar? "))

        res = math.pow(num1, num2)

        print("O resultado da operação é {}!".format(res))
    #seno
    elif desc==7:
        num1 = int(input("qual é o angulo que desega encontrar o seno? "))

        res=math.radians(num1)#converto o angulo para radianos
        res=math.sin(res)#calculo o seno

        print("O seno de {} é {}!".format(num1, res))
    #coseno
    elif desc==8:
        num1 = int(input("qual é o angulo que desega encontrar o coseno? "))

        res=math.radians(num1)
        res=math.cos(res)

        print("O coseno de {} é {}!".format(num1, res))
    #tangente
    elif desc==8:
        num1 = int(input("qual é o angulo que desega encontrar a tangente? "))

        res=math.radians(num1)
        res=math.tan(res)

        print("A tangente de {} é {}!".format(num1, res))
    #caso o numero escolhido fot invalido
    else:
        print("Erro 1 - opção invalida!")

    reps=1#define a variavel reps pra 1, sendo assim o menu de seleção ira aparecer
    t=int(input("deseja realizar outra operação? sim-0, não-1: "))#escolha se continua ou não a realizar operações
    if t==1:#se a escolha for 1(não) r vai receber 1, sendo assim ira sair do loop while
        r=r+1

else:
    print("Obrigado por utilizar a calculadora!")#mensagem final.