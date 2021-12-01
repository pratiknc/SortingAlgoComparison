Project name: Comparison of Sorting Algorithms
<br>
<br>The project implements five sorting algorithms –
<br>• Insertion sort
<br>• Merge sort
<br>• Heap sort
<br>• In-place quick sort
<br>• Modified quick sort (Using median-of-three as pivot with insertion sort)
<br>
<br>A driver code will generate arrays of random positive numbers which will be sorted using these five 
<br>algorithms. An average is calculated by running the sorting algorithms multiple times. Based on the 
<br>times reported, a graph depicting the behavior for various inputs is plotted.
<br>
<br>Prerequisites:
<br>Before you begin, ensure you have met the following requirements:
<br>• You have installed Python version 3.7+
<br>• You have installed pandas and matplotlib libraries.
<br>All Operating Systems are supported.
<br>
<br>Usage:
<br>1. Extract the zip file on desired path.
<br>2. Navigate to src folder.
<br>3. Run DriverSort.py –
<br>python DriverSort.py
<br>
<br>On execution, follow the prompts –
<br>"Enter number of sample sizes to run for:" – This is the number of arrays to generate for sorting.
<br>"Enter initial sample size:" – This is the minimum input size of the array to sort.
<br>"Enter number to increment initial sample size by:" – This is the number by which the array size is to be 
<br>incremented.
<br>"Enter number of runs for calculating average time:" – This is the number of runs to be considered for 
<br>calculating average.
<br>If any of the inputs are not provided by the user, the program will assume below values(default):
<br>Enter number of sample sizes to run for: 10
<br>Enter initial sample size: 1000
<br>Enter number to increment initial sample size by: 1000
<br>Enter number of runs for calculating average time: 5
