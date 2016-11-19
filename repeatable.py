#! /usr/bin/env python
import sys


def test_main():
    import this
    pass


def sort(arr):
    length = len(arr)
    for i in range(length):
        while arr[i] != i+1:
            current_data = arr[i]
            swap_data = arr[current_data - 1]
            if current_data == swap_data:
                return swap_data
            arr[current_data - 1] = current_data
            arr[i] = swap_data
            pass
        pass
    return 0
    pass


if __name__ == '__main__':
    #test_main()
    arr = [1, 5, 4, 3, 3, 7, 6]
    result = sort(arr)
    print 'repeatablenumber:' , result
    arr = [1, 2, 6, 7, 9, 8, 10, 11, 5, 4, 4]
    result = sort(arr)
    print 'repeatablenumber:', result
    arr = [5, 7, 3, 6, 9, 8, 2, 11, 1, 2, 4]
    result = sort(arr)
    print 'repeatablenumber:', result