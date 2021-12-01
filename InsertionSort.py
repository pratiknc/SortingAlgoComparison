import time


def insertion_sort(arr, low, high):
    """
    The function takes in input array along with its indexes, assumes the left side of the array is sorted
    and inserts the right side elements of the array to give a sorted array.
    :param arr: Input array.
    :param low: First element of the array.
    :param high: Last element of the array.
    """
    for index in range(low, high):
        curr_element = arr[index]
        curr_index = index
        while curr_index > low - 1 and arr[curr_index - 1] > curr_element:
            arr[curr_index] = arr[curr_index - 1]
            curr_index -= 1
        arr[curr_index] = curr_element


def sort_array_insertion(arr):
    """
    The function will sort the input array using insertion sort approach and return the time taken for sort.
    :param arr: Input array.
    :return: The time taken for sorting the array.
    """
    start_time = time.time()
    insertion_sort(arr, 1, len(arr))
    elapsed_time = (time.time() - start_time) * 1000
    return elapsed_time


def sort_array_insertion_quick(arr, low, high):
    """
    Additional function that uses the functionality of insertion sort. The calling goes to
    insertion sort method written above and is used for modified quick sort method.
    :param arr: Input array
    :param low: First element of the array.
    :param high: Last element of the array.
    """
    insertion_sort(arr, low + 1, high + 1)


def main():
    print("Use DriverSort.py to execute")

if __name__ == "__main__":
    main()
