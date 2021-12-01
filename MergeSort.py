import time

def merge(array, left_array, right_array):
    """
    The function evaluates both the sub arrays, sorts and merges into a single array.
    :param array: Array to be sorted.
    :param left_array: Sub array to the left of middle element.
    :param right_array: Sub array to the right of middle element.
    :return: Array of sorted numbers.
    """
    i = 0
    j = 0
    k = 0

    # Copy data to temp arrays from both the sub-arrays.
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # Append remaining elements of the array
    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    # Append remaining elements of the array
    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(arr):
    """
    Recursive function to divide the main array into smaller arrays.
    :param arr: Array that needs to be sorted.
    :return: Array of sorted numbers.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        l_array = arr[:mid]
        r_array = arr[mid:]
        merge_sort(l_array)
        merge_sort(r_array)

        merge(arr, l_array, r_array)


def sort_array_merge(arr):
    """
    The function will sort the input array using merge sort approach and return the time taken for sort.
    :param arr: Array to be sorted.
    :return: Time taken for sorting the array.
    """
    start_time = time.time()
    merge_sort(arr)
    elapsed_time = (time.time() - start_time) * 1000

    return elapsed_time


def main():
    print("Use DriverSort.py to execute")

if __name__ == "__main__":
    main()