import sorting
import random
import time
random_list = [random.randint(0, 1000000) for x in range(1000000)]


copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 2)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 2:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')


copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 6)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 6:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')


copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 10)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 10:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')


copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 50)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 50:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')


copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 150)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 150:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')



copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000,500)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 500:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')


copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 2000)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 2000:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')

copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 100000)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 100000:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')


copie=random_list.copy()
timp_start = time.perf_counter()
sorting.radixSort(copie, 1000000, 1000000)
timp_final = time.perf_counter() - timp_start
print('Radix sort, baza 1000000:', end=' ')
if sorting.functie_verif_sortat(copie) == True:
    print('Vectorul a fost sortat')
else:
    print('Vectorul nu a fost sortat')
    timp_final = round(float('{:.10f}'.format(float(timp_final))), 10)
print('Timp:', timp_final, 'seconds =', round(float(timp_final) / 60, 10), 'minutes\n')

