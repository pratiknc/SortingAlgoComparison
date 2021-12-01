from RandomArrayGenerator import gen_random_array
from InsertionSort import sort_array_insertion
from HeapSort import sort_array_heap
from MergeSort import sort_array_merge
from QuickSort_Mid import sort_array_quick
from QuickSort_Modify import sort_array_quicksort_modified
import Plotter
import pandas as pd

'''
Get sample sizes from users. If no input given, use defaults
Defaults:
    Number of sample sizes - 10
    Initial sample size - 1000
    Increment sample size by - 1000
    Number of runs to calculate average - 5
Generate and display sample sizes and get Yes/No confirmation
Generate seed for consistent results
'''

confirmation = False
while not confirmation:
    ip_size = int(input("Enter number of sample sizes to run for: ") or "10")
    init_ip_size = int(input("Enter initial sample size: ") or "1000")
    incr_num = int(input("Enter number to increment initial sample size by: ") or "1000")
    iter_per_ip = int(input("Enter number of runs for calculating average time: ") or "5")
    input_size_array = [init_ip_size+(i*incr_num) for i in range(0, ip_size)]
    seed_arr = gen_random_array(iter_per_ip, 500)

    print(input_size_array)
    print("program will run " + str(iter_per_ip) + " times for the above input sizes")
    confirmation_ip = input("Proceed? (Y/N) ")
    if confirmation_ip.lower() == 'y' or confirmation_ip.lower() == 'yes':
        confirmation = True
'''
Initialize arrays to store timings for unsorted, sorted and reverse sorted arrays
'''
timings_random = []
timings_random_sorted = []
timings_random_rev_sorted = []

'''
For each sample size and iteration, generate unsorted, sorted and reverse sorted array.
Execute each sorting algorithm and store timings in lists
'''

for n in input_size_array:
    for seed_val in seed_arr:
        timing_iter = [n]
        timing_iter_sorted = [n]
        timing_iter_rev_sorted = [n]
        arr = gen_random_array(n, seed_val)
        arr_sorted = arr.copy()
        arr_rev_sorted = arr.copy()
        arr_sorted.sort()
        arr_rev_sorted.sort(reverse=True)

        timing_iter.append(sort_array_insertion(arr[:]))
        timing_iter_sorted.append(sort_array_insertion(arr_sorted[:]))
        timing_iter_rev_sorted.append(sort_array_insertion(arr_rev_sorted[:]))

        timing_iter.append(sort_array_heap(arr[:]))
        timing_iter_sorted.append(sort_array_heap(arr_sorted[:]))
        timing_iter_rev_sorted.append(sort_array_heap(arr_rev_sorted[:]))

        timing_iter.append(sort_array_merge(arr[:]))
        timing_iter_sorted.append(sort_array_merge(arr_sorted[:]))
        timing_iter_rev_sorted.append(sort_array_merge(arr_rev_sorted[:]))

        timing_iter.append(sort_array_quick(arr[:]))
        timing_iter_sorted.append(sort_array_quick(arr_sorted[:]))
        timing_iter_rev_sorted.append(sort_array_quick(arr_rev_sorted[:]))

        timing_iter.append(sort_array_quicksort_modified(arr[:]))
        timing_iter_sorted.append(sort_array_quicksort_modified(arr_sorted[:]))
        timing_iter_rev_sorted.append(sort_array_quicksort_modified(arr_rev_sorted[:]))

        timings_random.append(timing_iter)
        timings_random_sorted.append(timing_iter_sorted)
        timings_random_rev_sorted.append(timing_iter_rev_sorted)

'''
Create pandas dataframe from list
Calculate average from iterations for each sample size
Convert from milliseconds to seconds and plot Unsorted, Sorted and Reverse Sorted timings separately
'''

timings_df = pd.DataFrame(timings_random,columns=['Input_Size','Insertion','Heap','Merge','Quick','Quick_Modified'])
timings_df_sorted = pd.DataFrame(timings_random_sorted,columns=['Input_Size','Insertion','Heap','Merge','Quick','Quick_Modified'])
timings_df_rev_sorted = pd.DataFrame(timings_random_rev_sorted,columns=['Input_Size','Insertion','Heap','Merge','Quick','Quick_Modified'])

timings_avg = timings_df.groupby(['Input_Size']).mean()
timings_avg_sorted = timings_df_sorted.groupby(['Input_Size']).mean()
timings_avg_rev_sorted = timings_df_rev_sorted.groupby(['Input_Size']).mean()


timings_avg_sorted = timings_avg_sorted/1000
timings_avg= timings_avg/1000
timings_avg_rev_sorted = timings_avg_rev_sorted/100

Plotter.plot_group(timings_avg, ['Insertion','Heap','Merge','Quick','Quick_Modified'], 'Comparison of Algorithms - Unsorted Array')
Plotter.plot_group(timings_avg_sorted, ['Insertion','Heap','Merge','Quick','Quick_Modified'], 'Comparison of Algorithms - Sorted Array')
Plotter.plot_group(timings_avg_rev_sorted, ['Insertion','Heap','Merge','Quick','Quick_Modified'], 'Comparison of Algorithms - Reverse Sorted Array')