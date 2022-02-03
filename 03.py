

def get_sum(a, b):
    lista = {}
    if (a > b):
        maior = a
        menor = b
    elif (a < b):
        maior = b
        menor = a
    else:
        soma = a
        menor = maior = False
        print(f' {a} Não há soma pois os números são iguais')
    if maior or menor is True:
        lista[0] = menor
        i = 1
        menor_int = int(menor)
        while (menor_int < int(maior)):
            menor_int += 1
            lista[i] = menor_int
            i += 1
        soma = 0
        for (item, k) in lista.items():
            print(k)
        for (item, k) in lista.items():
            kint = int(k)
            soma += kint
        print(f' A soma entre os numeros escolhidos (incluindo eles) é {soma}')
    else:
        print('Fim!')


a = input('Entre com o primeiro valor:')
b = input('Entre com o segundo valor:')
get_sum(a,b)

