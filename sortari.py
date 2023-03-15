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