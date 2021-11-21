import random

def separar():
    print("-"*100)

def calcular_N(P, Q):
    N = P * Q
    return N

def calcular_Z(P,Q):
    Z = (P - 1) * (Q - 1)
    return Z

P = 11          #Valor definido para o modelo experimental
Q = 13          #Valor definido para o modelo experimental
N = calcular_N(P,Q)
Z = calcular_Z(P,Q)
E = 7     #Valor definido verificado manualmente
D = 103   #Valor calculado por um algoritmo euclidiano extendido fora desse programa.

calcular_N(P,Q)
calcular_Z(P,Q)

def cifra(mensagem,E,N):
    limite = len(mensagem)
    cont = 0
    lista = []
    while(cont < limite):
        letra = mensagem[cont]
        X = ord(letra)
        resultado = (X**E) % N
        lista.append(resultado)
        cont += 1
    return lista

def descifra(cifra,N,D):
    lista = []
    cont = 0
    limite = len(cifra)
    while cont < limite:
        result = cifra[cont]**D
        texto = result % N
        letra = chr(texto)
        lista.append(letra)
        cont += 1
    return lista

def invalido():
    print("Opção inválida, tente novamente!")

def main():
    separar()
    texto_puro = str(input("Digite sua mensagem: "))
    separar()
    print(f"Chave Pública: {E}")
    chave_publica = int(input("Digite a chave pública para cifrar a mensagem: "))
    while chave_publica not in [E]:
        invalido()
        chave_publica = int(input("Digite uma chave pública para cifrar a mensagem: "))
    texto_cifrado = cifra(texto_puro,E,N)
    separar()
    print(f"Sua mensagem cifrada é: {texto_cifrado}")
    separar()

    print("Para encerrar o programa digite: nao")
    print("Para decifrar a mensagem digite: sim")
    opcao = str(input("Você gostaria de decifrar essa mensagem?: "))
    if opcao not in ["sim","nao"]:
        while True:
            invalido()
            opcao = str(input("Você gostaria de decifrar essa mensagem?: "))
            if opcao in ["sim", "nao"]:
                break
    if opcao == "sim":
        separar()
        print(f"Chave privada: {D}")
        chave_privada = int(input("Digite a chave privada: "))
        if chave_privada not in [D]:
            print("Você errou, reinicie o programa!")
        else:
            auxiliar_final = descifra(texto_cifrado,N,D)
            separar()
            texto_final = "".join(auxiliar_final)
            print(f"Sua mensagem decifrada é: {texto_final}")
    else:
        print("Fim do programa")

main()

"""def gerar_P():     #Código ilustrado apenas como 
                        #uma possivel implementação para tornar o algoritmo mais seguro
    auxiliar = random.randint(0,10000)
    while verificar_primo(auxiliar) != 1:
        auxiliar = random.randint(0,10000)
    P = auxiliar"""

"""def gerar_Q():        #Código ilustrado apenas como 
                        #uma possivel implementação para tornar o algoritmo mais seguro
    auxiliar = random.randint(0,10000)
    while verificar_primo(auxiliar) != 1:
        auxiliar = random.randint(0,10000)
    Q = auxiliar"""

"""def verificar_primo(x):   #Código ilustrado apenas como 
                            #uma possivel implementação para tornar o algoritmo mais seguro
 cont = 0
    for c in range(1, x):
        auxiliar = x % c
        if auxiliar == 0:
            cont += 1
    if cont > 1:
        return 0
    else:
        return 1"""

"""def mdc(a,b):         #Código ilustrado apenas como 
                        #uma possivel implementação para tornar o algoritmo mais seguro
    while b !=0:
        resto = a % b
        a = b
        b = resto
    return a"""

"""def calcular_E(Z):    #Código ilustrado apenas como 
                        #uma possivel implementação para tornar o algoritmo mais seguro
    while True:
        aleatorio = random.randint(2,Z-1)
        while verificar_primo(aleatorio) != 1:
            break
        else:
            auxiliar = mdc(Z, aleatorio)
            print(f"O mdc deu: {auxiliar}")
            if auxiliar == 1:
                E = aleatorio
                print(f"O e é: {E}")
                return E
        
calcular_E(Z)"""