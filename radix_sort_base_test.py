from sorting import radixSort,functie_verif_sortat
import random
import time

with open('input_radix_sort_base_test.txt') as f:
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
