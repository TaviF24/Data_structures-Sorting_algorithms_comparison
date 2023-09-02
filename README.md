# Sorting algorithms comparison

## About
A project that shows the differences between some sortings algorithms. The algorithms are tested on different inputs and the comparison is based on the execution time.

The algorithms and their complexities are:
1. **Merge Sort**: O(n logn)
2. **Radix Sort**: O(d (n + b)), where b = base and d = number of digits of the maximum number
3. **Shell Sort**: O(n<sup>2</sup>)
4. **Counting Sort**: O(n + k), where k = the maximum number
5. **Heap Sort**: O(n logn)

There are three extra comparisons:
- Radix Sort in different bases;
- Radix Sort: Binary operations vs Normal
- Shell Sort and Heap Sort: Iterative vs Recursive

## The machine
- Operating System: MacOS
- Language: Python 3.10
- IDE: PyCharm 2022.2.5

## The input format

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
.
.
.
```
>[!NOTE]
>For the [input_radix_binary.txt](input_radix_binary.txt) file, the bases are only powers of 2 because there are binary operations.

## The files

- the [sorting.py](sorting.py) file contains the algorithms(as functions) used in this projects;
- the [input_main.txt](input_main.txt) file contains the input needed in the algorithms. The input should be like this:
  ```
  2          //number of tests
  10 10000   //maximum_number  number_of_elements
  1000 1000
  ```
- the [main.py](main.py) file has the main code which takes the *input_main.txt* file, the *sorting.py* file and starts the comparison;
- the [iterative_vs_recursive.py](iterative_vs_recursive.py), [radix_sort_base_test.py](radix_sort_base_test.py) and [radix_binary_operations.py](radix_binary_operations.py) files are the three extra comparisons, with their input files [input_iterative_vs_recursive.txt](input_iterative_vs_recursive.txt), [input_radix_base_test.txt](input_radix_base_test.txt) and [input_radix_binary.txt](input_radix_binary.txt). The input for the last two should be like this:
  ```
  10000000 10000000  //maximum_number  number_of_elements
  2                  //bases (I put only powers of two, but you can change it however you want)
  4
  8
  16
  32
  64
  128
  ```
- [Sortari-SD.pptx](Sortari-SD.pptx) is a PowerPoint file in which I put all the final results.

