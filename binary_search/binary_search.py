#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class BinarySearch:
    """
    A binary search algorithm is a search technique that finds the position of a target value within a sorted array.
    It works by repeatedly dividing the search interval in half until the target is found.
    """

    def binary_search(self, array, thing_to_find, start=0, end=None) -> bool:
        """
        @param array: (list) The sorted list in which to search for the target value.
        @param thing_to_find: The target value to search for in the array.
        @param start: (int) The starting index of the search interval. Default is 0.
        @param end: (int) The ending index of the search interval. Default is the last index of the array.
        @return bool: True if the target value is found in the array, False otherwise.
        """
        if not isinstance(array, list):
            raise TypeError(f'{self.binary_search.__qualname__}: expects parameter "array" to be of type list: {type(array)} given')

        if len(array) == 0:
            return False

        if thing_to_find is None:
            raise ValueError(f'{self.binary_search.__qualname__}: argument "thing_to_find" cannot be empty')

        if not isinstance(start, int):
            raise TypeError(f'{self.binary_search.__qualname__}: expects parameter "start" to be of type int: {type(start)} given')

        if start < 0:
            raise ValueError(f'{self.binary_search.__qualname__}: expects parameter "start" to be greater than "-1": {str(start)} given')

        # set "end" default value
        if end is None:
            end = len(array) - 1

        if not isinstance(end, int):
            raise TypeError(f'{self.binary_search.__qualname__}: expects parameter "end" to be of type int: {type(end)} given')

        if start > end:
            return False

        mid = (start + end) // 2

        if array[mid] == thing_to_find:
            return True

        if thing_to_find < array[mid]:
            return self.binary_search(array, thing_to_find, start, mid - 1)

        if thing_to_find > array[mid]:
            return self.binary_search(array, thing_to_find, mid + 1, end)

        return False



def main():
    """main"""
    binary_search = BinarySearch()

    print('BinarySearch')
    print('=' * 50 + '\n')

    print(binary_search.binary_search([1,2,3,4,5,6,7,8,9], 7))
    print('')


if __name__ == '__main__':
    main()
