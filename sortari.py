def counting_sort(lista,nr_max):
    v_frecventa=[0]*(nr_max+1)
    for element in lista:
        v_frecventa[element]+=1
    j=0
    for x in range(0,nr_max+1):
        for i in range(0,v_frecventa[x]):
            lista[j]=x
            j+=1

# lista=[2,1,100,45,24,24,2000,46,45,6,3,89,0,35,1000]
# print(lista)
# counting_sort(lista,2000)
# print(lista)