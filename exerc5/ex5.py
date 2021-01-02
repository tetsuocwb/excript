# # 5.1
# def estudo():
#     print('Estamos estudando as funções')
# estudo()

# # 5.2
# def estudo2(x):
#     print("Função invocada com sucesso. O",
#     "valor passado pelo argumento é: " , x)

# estudo2(10)

# # 5.4
# def ascendMedia(a, b, c):
#     lista = [a, b, c]
#     lista.sort()
#     print('ascendente: ',lista)


# def descendMedia(a, b, c):
#     lista = [a, b, c]
#     lista.sort(reverse=True)
#     print(round(sum(lista)/len(lista),2), ' é a média.')
#     print(lista)
# ascendMedia(1, 100, 3)
# descendMedia(1 , 100 ,3)

# 5.5
# def opcional(a, b = None):
#     print(a , b)


# def opcional(a, *args):
#     for y in args:
#         print(y)
#     print(a , args)

# def opcional(prim, *args):
#     entrada_b = list(map(chr, range(97, 97 + len(args))))
#     # ind = args
#     # [*entrada_b] = [*ind]
#     dicn = {entrada_b[i]:list(args)[i] for i in range(len(args))}
#     a = 90
#     for key, val in dicn.items():
#         print(key, val)
#         exec('global ' + key)
#         exec('a = 10')
#         print(a)
#     #print(a)
#     print(dicn['a'])
#     print(entrada_b)
#     print(prim )

# opcional(1, 2, 'e' ,'r' ,5, 'i', 'aksjf', '0012')
# #print(a)

# # 5.6

# def func2(a, b):
#     return a + b

# def func1(a, b):
#     return func2(a, b)

# print(func1(2,3))

# # 5.7
# def nao_sei_quantos(*args):
#     for i in args:
#         print(i)
# nao_sei_quantos(1 , 'ewqe' , 're', 4, 5, 9 ,'afoi')

# # 5.9
# def func(a, b, c, d):
#     print(a+b+c+d)
# lista = [1, 2, 3, 4]
# func(*lista)

# # 5 .10, 11, 12
# def func(*args):
#     lista = list(args)
#     print('Soma = ', sum(lista))
#     print('Maior numero: ', sorted(lista, reverse = True)[0]) #retorna a lista decrescente sem alterar a lista original
#     print(lista) #lista original
#     produto = 1
#     for i in lista:
#         produto *= i
#     print(produto)
# func(1, 5, 8, 9, 10, 8, 27)

# # 5.13
# '''Escreva uma função que inverta a ordem dos elementos
#  de uma lista manualmente. Não utilize a função interna do Python que
#   faz inversão, crie o algoritmo que faça a inversão.
# Lista: "1234abcd"
# Saída: "dcba4321"'''
# lista = "1234abcd"
# #lista = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
# def inverte(l):
#     saida = ""
#     for i in range(len(l)-1, -1, -1):
#         saida += (l[i])
#        # print(i, l[i])
#     #print(saida)
#     return saida

# print(inverte(lista))

# # 5.14
# '''Escreva uma função que calcule o fatorial de um
#  número (um inteiro não negativo). Envie o valor 
# do número que será calculado como argumento da função.'''
# def fat(n):
#     fatorial = 1 #se iniciliizar com 0....
#     for i in range(1, n + 1):
#         fatorial *= i
#         #print(fatorial)
#         #print(n, i)
#     return fatorial

# print(fat(int(input("Numero para calcular o fatorial: "))))

# # 5.15
# '''Escreva uma função que verifique se um número está 
# num intervalo determinado.'''
# def contem(n, inicio, fim):
#     intervalo = list(range(int(inicio), int(fim) + 1))
#     if n in intervalo:
#         return 'contem'
#     else:
#         return 'não contem'
# c = 'y'
# while c == 'y':
#     n = int(input('Verifica se  um numero "n" esta entre "a" e "b".\nn:'))
#     a = int(input('\na:'))
#     b = int(input('\nb:'))
#     print(contem(n, a, b))
#     c = input('\nContinuar? y ou n: ')


# # 5.16
# '''Escreva uma função que aceite Strings e calcule a quantidade de letras 
# em mauisculas e minúsculas que a String possui.'''
# #cap letters ascii 65-90 lower case 97-122
# def maiusMinus(s):
#     lower = 0
#     cap = 0
#     for i in s:
#         if 65 <= ord(i) <= 90:
#             cap += 1
#         if 97 <= ord(i) <= 122:
#             lower += 1
#     print(lower, "minusculas\n")
#     print(cap, "maiusculas")


# r ='y'
# while r == "y":
#     t = input("insira um string: ")

#     maiusMinus(t)
#     r = input('Continuar y/n ?')


# # 5.19
# # Imprima somente os numeros positivos

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# saida = [i for i in lista if i % 2 == 0]
# print(saida)

# # 5.20
# # verificar se um string é um palindromo

# def palind():

#     frase = input("Palindromo: ")
#     if frase == ''.join(reversed(frase)):
#         print(frase, ' é um palindromo.')
#     else:
#         print(frase,' não é um palindromo.')

#    # print(''.join(reversed(frase)))


# palind()