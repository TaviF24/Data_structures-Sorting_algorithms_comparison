from sorting import radixSort,functie_verif_sortat
import random
import time
random_list = [random.randint(0, 1000000) for x in range(1000000)]

with open('input_radix_sort_base_test.txt') as f:
    rand=f.readline()
    while rand !="":
        baza = int(rand.split()[0])
        copie=random_list.copy()
        timp_start = time.perf_counter()
        radixSort(copie, 1000000, baza)
        timp_final = time.perf_counter() - timp_start
        print('Radix sort, baza ',baza,':',sep='', end=' ')
        if functie_verif_sortat(copie) == True:
            print('Vectorul a fost sortat')
        else:
            print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
        print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        rand=f.readline()
