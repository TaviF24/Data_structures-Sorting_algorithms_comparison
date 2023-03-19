from sorting import functie_verif_sortat, radixSort
import random
import time
def aflare_putere(baza):
    k = 0
    i=1
    while baza > i:
        i=i<<1
        k += 1
    return k
def radixSort_binary(lista,nr_max,baza):
    i=0
    lungime=len(lista)
    poz=1
    while nr_max//(poz*baza)>0:
        v_frecv=[0]*baza
        poz=baza**i
        k=aflare_putere(poz)
        for j in range(lungime):
            index=lista[j]>>k
            v_frecv[index%baza]+=1
        for j in range(1,baza):
            v_frecv[j]+=v_frecv[j-1]
        copie = lista.copy()
        for j in range(lungime-1,-1,-1):
            index=copie[j]>>k
            v_frecv[index%baza] -= 1
            lista[v_frecv[index%baza]] = copie[j]
        i+=1

with open('input_radix_binary.txt') as f:
    rand = f.readline().split()
    nr_max = int(rand[0])
    nr_elem = int(rand[1])
    random_list = [random.randint(0, nr_max) for x in range(nr_elem)]
    rand = f.readline()
    while rand !="":
        baza = int(rand.split()[0])
        try:
            copie=random_list.copy()
            timp_start = time.perf_counter()
            radixSort_binary(copie, nr_max, baza)
            timp_final = time.perf_counter() - timp_start
            print('Radix sort pe biti, baza ',baza,':',sep='', end=' ')
            if functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
                timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Radix sort nu a putut sorta in baza",baza)
        try:
            copie=random_list.copy()
            timp_start = time.perf_counter()
            radixSort(copie, nr_max, baza)
            timp_final = time.perf_counter() - timp_start
            print('Radix sort, baza ',baza,':',sep='', end=' ')
            if functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
                timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Radix sort nu a putut sorta in baza",baza)
        rand=f.readline()