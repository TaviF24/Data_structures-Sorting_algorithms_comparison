# Sorting algorithms comparison

## About
A project that shows the differences between some sortings algorithms. The algorithms are tested on different inputs and the comparison is based on the execution time.

The algorithms and their complexities are:
1. **Merge Sort**: O(n logn)
2. **Radix Sort**: O(d (n + b)), where b = base and d = number of digits of the maximum number
3. **Shell Sort**: O(n<sup>2</sup>)
4. **Counting Sort**: O(n + k), where k = the maximum number
5. **Heap Sort**: O(n logn)

There are two extra comparisons:
- Radix Sort in different bases with binary operations
- Shell Sort and Heap Sort: Iterative vs Recursive

## The machine
- Operating System: MacOS
- Language: Python 3.10
- IDE: PyCharm 2022.2.5

## The files

The input files for [main.py](main.py) and [iterative_vs_recursive.py]([iterative_vs_recursive.py) should look like this:
```
#    nr of tests
# #  test_1 : max_nr  nr_of_elements
# #  test_2
.
.
.
```
The input files for [radix_binary_operations.py](radix_binary_operations.py) and [radix_sort_base_test.py](radix_sort_base_test.py) should look like this:
```
# #  max_nr  nr_of_elements
#    the base (you can add/remove without modifing other line)
#
.
.
.
```

>[!NOTE]
>For the  

- [sorting.py](sorting.py) file contains the algorithms(as functions) used in this projects
- [input_main.txt](input_main.txt) file contains the input needed in the algorithms. The input should be like this:
  ```
  2          //number of tests
  10 10000   //maximum_number  number_of_elements
  1000 1000
  ```
- [main.py](main.py) file has the main code which takes the *input_main.txt* file, the *sorting.py* file and starts the comparison

