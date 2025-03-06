'''
Question 83
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints: Use timeit() function to measure the running time.

'''

#timeit is a Python module used to measure the execution time of small code 
# snippets. It's particularly useful for benchmarking code to evaluate its performance. 
# The module provides an accurate way to determine how long a specific piece of code takes to
# run by isolating it from other system activities and overhead.


import timeit

# Measure time for "1+1" executed 100 times
execution_time = timeit.timeit("1 + 1", number=100)
print("Execution Time for '1 + 1' (100 iterations):", execution_time)
