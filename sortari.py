def counting_sort(lista,nr_max):
    v_frecventa=[0]*(nr_max+1)
    for element in lista:
        v_frecventa[element]+=1
    for i in range(1,len(v_frecventa)):
        v_frecventa[i]+=v_frecventa[i-1]
    copie=lista.copy()
    for i in range(len(lista)-1,-1,-1):
        v_frecventa[copie[i]]-=1
        lista[v_frecventa[copie[i]]]=copie[i]

# lista=[2,1,100,45,24,24,2000,46,45,6,3,89,0,35,1000]
# print(lista)
# counting_sort(lista,2000)
# print(lista)


def interclasare(lista,inc,sf):
    copie=[0]*(sf-inc+1)
    i=inc
    mijloc=(inc+sf)//2
    j=mijloc+1
    indice_copie=0
    while i<=mijloc and j<=sf:
        if lista[i]<lista[j]:
            copie[indice_copie]=lista[i]
            indice_copie+=1
            i+=1
        elif lista[i]>lista[j]:
            copie[indice_copie] = lista[j]
            indice_copie += 1
            j += 1
        else:
            copie[indice_copie] = lista[i]
            indice_copie += 1
            copie[indice_copie] = lista[j]
            indice_copie += 1
            i += 1
            j += 1
    while i <= mijloc:
        copie[indice_copie] = lista[i]
        indice_copie += 1
        i += 1
    while j <= sf:
        copie[indice_copie] = lista[j]
        indice_copie += 1
        j += 1
    lista[inc:sf+1]=copie
def divide(lista,inc,sf):
    if inc<sf:
        mijloc=(inc+sf)//2
        divide(lista,inc,mijloc)
        divide(lista,mijloc+1,sf)
        interclasare(lista,inc,sf)
# lista=[7,2,3,9,4,178,0,2,2,2]
# print(lista)
# divide(lista,0,len(lista)-1)
# print(lista)

# 0 2 4 1 3 5
# 0 1 2 3 4 5     nr=6 i=0 mij=3

# lista2=[6,3,3,5,1,3]
# lista3=[0,2,4,6,8,1,3,5,7,9]
# print(lista2)
# divide(lista2,0,len(lista2)-1)
# print(lista2)