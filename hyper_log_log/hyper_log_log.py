#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

import math
import hashlib


class HyperLogLog:
    """HyperLogLog"""

    def __init__(self, precision=14):
        self.precision = precision
        self.register_size = 2 ** precision
        self.registers = [0] * self.register_size

    def hash_function(self, element):
        """hash_function"""
        hash_value = hashlib.sha256(str(element).encode()).hexdigest()
        return int(hash_value, 16)

    def count_leading_zeros(self, binary_string):
        """count_leading_zeros"""
        count = 0
        for bit in binary_string:
            if bit == '0':
                count += 1
            else:
                break
        return count

    def add_element(self, element):
        """add_element"""
        hash_value = self.hash_function(element)
        index = hash_value % self.register_size
        binary_representation = bin(hash_value)[2:]
        leading_zeros = self.count_leading_zeros(binary_representation)
        self.registers[index] = max(self.registers[index], leading_zeros + 1)

    def estimate_cardinality(self):
        """estimate_cardinality"""
        alpha = 0.7213 / (1 + 1.079 / self.register_size)
        harmonic_mean = sum(2 ** -reg for reg in self.registers)
        raw_estimate = alpha * self.register_size ** 2 / harmonic_mean
        if raw_estimate <= 2.5 * self.register_size:
            zero_registers = self.registers.count(0)
            if zero_registers != 0:
                return round(self.register_size * math.log(self.register_size / zero_registers))
            return raw_estimate
        if raw_estimate <= (1 << 32) / 30.0:
            return round(raw_estimate)
        return -2**32 * math.log(1 - raw_estimate / 2**32)


def main():
    """main"""
    print('HyperLogLog')
    print('=' * 50 + '\n')

    hyper_log_log = HyperLogLog(precision=14)

    # Add elements to the HyperLogLog sketch
    elements = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'kiwi']
    for element in elements:
        hyper_log_log.add_element(element)

    # Estimate the cardinality
    estimated_cardinality = hyper_log_log.estimate_cardinality()
    print(f"Estimated Cardinality: {estimated_cardinality}")


if __name__ == '__main__':
    main()
