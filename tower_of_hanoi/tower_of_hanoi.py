#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class TowerOfHanoi:
    """
    Tower of Hanoi

    The Tower of Hanoi is a mathematical puzzle where you have 3 rods
    and N disks of different sizes which can slide onto any rod. The
    puzzle starts with the disks stacked in ascending order of size on
    one rod, the smallest disk at the top.

    The objective of the puzzle is to move the entire stack to the last
    rod, obeying the following rules:

    1. Only one disk may be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks
    and placing it on top of another stack or an empty rod.
    3. No disk may be placed on top of a smaller disk.

    This class implements the Tower of Hanoi puzzle and provides a method
    to return the list of steps required to solve the puzzle for a given
    number of disks.
    """


    def tower_of_hanoi(self, num_disks: int, start_pole: str, end_pole: str, spare_pole: str) -> list:
        """
        Returns the list of steps required to solve the puzzle for a given
        number of disks.
        """

        if not isinstance(num_disks, int):
            raise TypeError(f'{self.tower_of_hanoi.__qualname__}: expects parameter "num_disks" to be of type int: {type(num_disks)} given')

        if num_disks < 1:
            raise ValueError(f'{self.tower_of_hanoi.__qualname__}: expects parameter "num_disks" to be a positive integer: {str(num_disks)} given')

        for pole in [start_pole, end_pole, spare_pole]:

            if not isinstance(pole, str):
                raise TypeError(f'{self.tower_of_hanoi.__qualname__}: expects parameter "pole" to be of type str: {type(pole)} given')

            if pole not in ['A', 'B', 'C']:
                raise ValueError(f'{self.tower_of_hanoi.__qualname__}: expects parameter "pole" to contain "A", "B", or "C": {str(start_pole)} given')

        if num_disks == 1:
            return [(num_disks, start_pole, end_pole)]

        return self.tower_of_hanoi(num_disks - 1, start_pole, spare_pole, end_pole) + [(num_disks, start_pole, end_pole)] + self.tower_of_hanoi(num_disks - 1, spare_pole, end_pole, start_pole)


def main():
    """main"""
    tower_of_hanoi = TowerOfHanoi()

    print('TowerOfHanoi')
    print('=' * 50 + '\n')

    num_disks = int(input('Number of disks: ').strip())
    print(tower_of_hanoi.tower_of_hanoi(num_disks, 'A', 'C', 'B'))

if __name__ == "__main__":
    main()
