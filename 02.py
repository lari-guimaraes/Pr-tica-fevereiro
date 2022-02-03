
def dig_pow(n,p):
    lista = lista_alterada = []
    lista = list(n)
    lista_alterada = [int(x) for x in lista]
    cont = 0
    soma = 0
    print(lista_alterada)
    while (cont < (len(lista_alterada))):
        soma += lista_alterada[cont] ** (p + cont)
        print(f'{lista_alterada[cont]}**{(p + cont)}')
        cont += 1
    print(soma)
    n_int = int(n)
    mult = soma * p
    if mult == n_int:
        i = 0
        while (i < len(lista_alterada)):
            print(f'{lista_alterada[i]}^{p+i} + ')
            i += 1
        print(f' = {soma} * {p} = {n}')
    else:
        print('Não tem a propriedade avaliada!')


a = str(input('Entre com o valor de a:'))
b = int(input('Entre com o valor de b:'))
dig_pow(a, b)

