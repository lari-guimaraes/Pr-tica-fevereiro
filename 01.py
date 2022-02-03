

def maskify(cc):
    lista = []
    lista = list(cc)
    cont = 0
    while (cont <= (len(lista) - 5)):
        lista[cont] = '#'
        cont += 1
    cc_mascarada = ''.join(map(str,lista))
    print(f' {cc} == {cc_mascarada}')



palavra = (input('String or number: '))

maskify(palavra)

