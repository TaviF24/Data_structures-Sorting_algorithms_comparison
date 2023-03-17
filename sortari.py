def functie_verif_sortat(lista):
    for i in range(1,len(lista)):
        if lista[i-1]>lista[i]:
            return False
    return True

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
    while i <= mijloc and j <= sf:
        if lista[i] < lista[j]:
            copie[indice_copie] = lista[i]
            indice_copie += 1
            i += 1
        else:
            copie[indice_copie] = lista[j]
            indice_copie += 1
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
def mergeSort(lista,inc,sf):
    if inc<sf:
        mijloc=(inc+sf)//2
        mergeSort(lista,inc,mijloc)
        mergeSort(lista,mijloc+1,sf)
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


def radixSort(lista,nr_max,baza):
    i=0
    lungime=len(lista)
    poz=1
    while nr_max//(poz*baza)>0:
        v_frecv=[0]*baza
        poz=baza**i
        for j in range(lungime):
            index=lista[j]//poz
            v_frecv[index%baza]+=1
        for j in range(1,baza):
            v_frecv[j]+=v_frecv[j-1]
        copie = lista.copy()
        for j in range(lungime-1,-1,-1):
            index=copie[j]//poz
            v_frecv[index%baza] -= 1
            lista[v_frecv[index%baza]] = copie[j]
        i+=1


def shellSort2(lista):
    lungime = len(lista)
    gap=lungime//2
    while gap>0:
        for i in range(gap, lungime):
            for j in range(i-gap,-1,-gap):
                if lista[j+gap]<lista[j]:
                    lista[j+gap],lista[j]=lista[j],lista[j+gap]
                else:
                    break
        gap//=2



def findSwap(inc,lungime,lista,gap):
    for i in range(inc,lungime):
        if lista[i-gap]>lista[i] and i-gap>=0:
            lista[i - gap],lista[i]=lista[i],lista[i-gap]
            findSwap(i-gap,lungime,lista,gap)
def shellSort1(lista):
    lungime=len(lista)
    gap=lungime//2
    while gap>0:
        findSwap(gap,lungime,lista,gap)
        gap//=2

#neeficienta


def heapSort2(lista,nr_elem):
    while nr_elem>0:
        for inc in range(nr_elem//2-1,-1,-1):
            i=inc
            nodul_stang=inc*2+1
            nodul_drept=inc*2+2
            if nodul_stang<nr_elem and lista[i]<lista[nodul_stang]:
                i=nodul_stang
            if nodul_drept<nr_elem and lista[i]<lista[nodul_drept] :
                i=nodul_drept
            if i!=inc:
                lista[i], lista[inc] = lista[inc], lista[i]
        if lista[0]!=lista[nr_elem-1]:
            lista[0],lista[nr_elem-1]=lista[nr_elem-1],lista[0]
        nr_elem-=1





def heapify(lista, n, i):
    inc = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2
    if left_node < n and lista[i] < lista[left_node]:
        inc = left_node
    if right_node < n and lista[inc] < lista[right_node]:
        inc = right_node
    if inc != i:
        (lista[i], lista[inc]) = (lista[inc], lista[i])
        heapify(lista, n, inc)

def heapSort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        (lista[i], lista[0]) = (lista[0], lista[i])
        heapify(lista, i, 0)
#mai eficienta
