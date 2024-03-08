#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class MinTemperature:
    """MinTemperature"""

    def get_closest_to_zero(self, temperatures: list) -> int:
        """get_closest_to_zero"""
        if not isinstance(temperatures, list):
            raise TypeError(f'{self.get_closest_to_zero.__qualname__}: expects parameter "temperatures" to be of type list: {type(temperatures)} given')

        if len(temperatures) == 0:
            raise ValueError(f'{self.get_closest_to_zero.__qualname__}: argument "temperature" cannot be empty')

        if len(temperatures) == 1:
            return temperatures[0]

        # initialize minimum integer with first value from temperatures list
        minimum = temperatures[0]

        for temperature in temperatures:
            if abs(temperature) < abs(minimum):
                minimum = temperature

            # when two absolute values are equals, keep positive temperature if any
            elif abs(temperature) == abs(minimum) and minimum < 0:
                minimum = temperature

        return minimum

    def get_minimum_positive_temperature(self, temperatures: list) -> int:
        """get_minimum_positive_temperature"""
        if not isinstance(temperatures, list):
            raise TypeError(f'{self.get_minimum_positive_temperature.__qualname__}: expects parameter "temperatures" to be of type list: {type(temperatures)} given')

        if len(temperatures) == 0:
            raise ValueError(f'{self.get_minimum_positive_temperature.__qualname__}: argument "temperature" cannot be empty')

        result = [temperature for temperature in temperatures if temperature > 0]

        if len(result) == 0:
            raise ValueError(
                f'{self.get_minimum_positive_temperature.__qualname__}: temperature list must contain at least one positive value')

        return min(result)


def main():
    """main"""
    min_temperature = MinTemperature()

    print('get_closest_to_zero')
    print('=' * 50 + '\n')

    print(min_temperature.get_closest_to_zero([-5, -4, -2, 12, -40, 4, 18, 11, 5]))
    print()

    print('get_minimum_positive_temperature')
    print('=' * 50 + '\n')

    print(min_temperature.get_minimum_positive_temperature([-5, -4, -2, 12, -40, 4, 18, 11, 5]))
    print('')


if __name__ == '__main__':
    main()
