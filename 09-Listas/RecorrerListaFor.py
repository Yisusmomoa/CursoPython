
# pasarlo a función y que el usuario pida una consonante a buscar

consonants = ['b', 'f', 'g', 'h', 'j', 'k']
def buscaConsonante(_letra):
    position=-1
    for i in range(len(consonants)):
        if consonants[i]==_letra:
            position=i
            return position
    return position

print(f"Elige una consonante: {consonants}")
check = input("Elige una consonante para mostrarte su posición en el arreglo: ")

if check.isnumeric():
    print("Captura una letra por favor")
else:
    auxposition=buscaConsonante(check)
    if auxposition > -1:
        print("Element's Index in the list is:",auxposition)
    else:
        print("Element's Index does not exist in the list:",auxposition)



# consonants = ['b', 'f', 'g', 'h', 'j', 'k']
# print(f"Elige una consonante: {consonants}")
# check = 'j'
# position = -1
# for i in range(len(consonants)):
#     if consonants[i] == check:
#         position = i
#         break
# if position > -1:
#     print("Element's Index in the list is:",position)
# else:
#     print("Element's Index does not exist in the list:", position)