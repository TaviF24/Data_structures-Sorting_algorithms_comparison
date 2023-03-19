from sorting import shellSort,shellSort2,heapSort,heapSort2,functie_verif_sortat
from random import randint
from time import perf_counter
import sys
sys.setrecursionlimit(2000)  #Pentru algoritmul Shell sort recursiv. Daca nr_elem este foarte mare, algoritmul nu va merge.
                             # Aici, nr maxim de elemente pentru care merge este 1087
with open('input_iterative_vs_recursive.txt') as f:
    nr_teste = int(f.readline().split()[0])
    for i in range(nr_teste):
        test = f.readline().split()
        nr_max = int(test[0])
        nr_elem = int(test[1])
        print(f"Testul {i+1}: Numarul maxim din lista e {nr_max}, iar numarul de elemente este {nr_elem}\n")
        random_list = [randint(0, nr_max) for x in range(nr_elem)]

        try:
            copie = random_list.copy()
            timp_start = perf_counter()
            shellSort(copie)
            timp_final = perf_counter() - timp_start
            print('Shell sort iterativ:', end=' ')
            if functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final=round(float('{:.10f}'.format(float(timp_final))),10)
            print('Timp:',timp_final, 'seconds =', round(float(timp_final) / 60,10), 'minutes\n')
        except:
            print("Shell sort iterativ nu a putut sorta")

        try:
            copie = random_list.copy()
            timp_start = perf_counter()
            shellSort2(copie)
            timp_final = perf_counter() - timp_start
            print('Shell sort recursiv:', end=' ')
            if functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Shell sort recursiv nu a putut sorta")

        try:
            copie=random_list.copy()
            timp_start=perf_counter()
            heapSort2(copie,nr_elem)
            timp_final=perf_counter()-timp_start
            print('Heap sort iterativ:',end=' ')
            if functie_verif_sortat(copie) ==True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Heap sort iterativ a putut sorta")

        try:
            copie = random_list.copy()
            timp_start = perf_counter()
            heapSort(copie)
            timp_final = perf_counter() - timp_start
            print('Heap sort recursiv:', end=' ')
            if functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Heap sort recursiv nu a putut sorta")


