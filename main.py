import sorting
import random
import time
with open('input.txt') as f:
    nr_teste = int(f.readline().split()[0])
    for i in range(nr_teste):
        test = f.readline().split()
        nr_max = int(test[0])
        nr_elem = int(test[1])
        print(f"Testul {i+1}: Numarul maxim din lista e {nr_max}, iar numarul de elemente este {nr_elem}\n")

        random_list = [random.randint(0, nr_max) for x in range(nr_elem)]


        try:
            copie = random_list.copy()
            timp_start = time.perf_counter()
            sorting.mergeSort(copie, 0, nr_elem - 1)
            timp_final = time.perf_counter() - timp_start
            print('Merge sort:', end=' ')
            if sorting.functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final=round(float('{:.10f}'.format(float(timp_final))),10)
            print('Timp:',timp_final, 'seconds =', round(float(timp_final) / 60,10), 'minutes\n')
        except:
            print("Merge sort nu a putut sorta")

        try:
            copie = random_list.copy()
            timp_start = time.perf_counter()
            sorting.radixSort(copie, nr_max, 10)
            timp_final = time.perf_counter() - timp_start
            print('Radix sort:', end=' ')
            if sorting.functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Radix sort nu a putut sorta")


        try:
            copie = random_list.copy()
            timp_start = time.perf_counter()
            sorting.shellSort(copie)
            timp_final = time.perf_counter() - timp_start
            print('Shell sort:', end=' ')
            if sorting.functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Shell sort nu a putut sorta")


        try:
            copie=random_list.copy()
            timp_start=time.perf_counter()
            sorting.countingSort(copie, nr_max)
            timp_final=time.perf_counter()-timp_start
            print('Counting sort:',end=' ')
            if sorting.functie_verif_sortat(copie) ==True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Counting sort a putut sorta")


        try:
            copie = random_list.copy()
            timp_start = time.perf_counter()
            sorting.heapSort(copie)
            timp_final = time.perf_counter() - timp_start
            print('Heap sort:', end=' ')
            if sorting.functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Heap sort nu a putut sorta")

        try:
            copie = random_list.copy()
            timp_start = time.perf_counter()
            copie.sort()
            timp_final = time.perf_counter() - timp_start
            print('Python sort method:', end=' ')
            if sorting.functie_verif_sortat(copie) == True:
                print('Vectorul a fost sortat')
            else:
                print('Vectorul nu a fost sortat')
            timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
            print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')
        except:
            print("Python sort method nu a putut sorta")

