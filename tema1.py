lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("lista este", list) #1
list_asc = lista
list_desc = lista
list_asc.sort()
print("lista ascendenta este", list_asc) #2
list_desc.reverse()
print("lista descendenta este", list_desc) #3
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_imp_slice = lista[1::2]
print("lista cu indici impari este", lista_imp_slice) #4
lista_p_slice = lista[0::2]
print("lista cu indici pari este", lista_p_slice) #5

for i in range(1,100):
    if i % 3 == 0:
        print(i) #6

