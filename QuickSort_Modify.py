""" This function takes first element as pivot """
import time
from InsertionSort import sort_array_insertion_quick
from MergeSort import sort_array_merge
import sys
# import resource
from RandomArrayGenerator import gen_random_array


def median_of_three_pivot(array, low, high):
    """
    The function returns the median amongst three elements of array.
    :param array: Input array for which median to be calculated.
    :param low: First element index of array.
    :param high: Last element index of array.
    :return: Element to considered as pivot.
    """
    mid_elem = (low + high) // 2
    pivot_elem = array[mid_elem]
    if len(array) == 2:
        if array[low] > array[high]:
            array[low], array[high] = array[high], array[low]
            pivot_elem = array[low]
    else:
        if array[low] < array[mid_elem]:
            if array[low] > array[high]:
                array[low], array[mid_elem] = array[mid_elem], array[low]
                pivot_elem = array[mid_elem]
            elif array[mid_elem] < array[high]:
                pivot_elem = array[mid_elem]
                # array[low], array[mid_elem] = array[mid_elem], array[low]
            else:
                array[mid_elem], array[high] = array[high], array[mid_elem]
                pivot_elem = array[high]
        elif array[low] > array[mid_elem]:
            if array[low] < array[high]:
                array[low], array[mid_elem] = array[mid_elem], array[low]
                pivot_elem = array[mid_elem]
            elif array[mid_elem] > array[high]:
                pivot_elem = array[mid_elem]
                # array[low], array[mid_elem] = array[mid_elem], array[low]
            else:
                pivot_elem = array[high]
                array[mid_elem], array[high] = array[high], array[mid_elem]

    # print("Pivot Element is : ", pivot_elem)
    # print("New array is : ", array)
    return pivot_elem


def partition(array, low, high):
    """"
    The function takes in input array along with its indexes, assumes the first element as a pivot
    around which rest of the array element will be sorted.
    :param array: Input array.
    :param low: First element index of array.
    :param high: Last element index of array.
    :return: Index of the pivot element after the array is sorted around the pivot.
    """
    # pivot (Element to be placed at correct position)
    pivot = median_of_three_pivot(array, low, high)

    while low <= high:
        # If current element from the end is greater than the pivot, skip it.
        while array[high] > pivot:
            high -= 1

        # If current element from the start is lesser than the pivot, skip it.
        while array[low] < pivot:
            low += 1

        if low <= high:
            # swap array[low] and array[high]
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1

    # Return the lower index when it becomes greater than higher index of the array.
    return low


def quick_sort_modified(array, low, high):
    """
    The function divides the array into sub-arrays based on the index of pivot elements.
    :param array: Array to be sorted.
    :param low: Minimum index of the array.
    :param high: Maximum index of the array.
    """
    if low < high and high - low > 10:
        # p_index is index at which the pivot exists, arr[p_index] is now at right place
        p_index = partition(array, low, high)

        quick_sort_modified(array, low, p_index - 1)  # Before p_index
        quick_sort_modified(array, p_index, high)  # After p_index
    elif low < high and high - low <= 10:
        sort_array_insertion_quick(array, low, high)


def sort_array_quicksort_modified(arr):
    """
    The function will sort the input array using quick sort approach ("median-of-three" approach for pivot)
    and return the time taken for sort.
    :param arr: Array to be sorted.
    :return: Time taken for sorting the array.
    """
    start_time = time.time()
    quick_sort_modified(arr, 0, (len(arr) - 1))
    elapsed_time = (time.time() - start_time)

    return elapsed_time * 1000


def main():
    print("Use DriverSort.py to execute")


if __name__ == "__main__":
    main()
