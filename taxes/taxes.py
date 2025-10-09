#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class FrenchIncomeTaxCalculator:
    """
    A class to calculate taxes on French incomes based on specified brackets.

    Attributes:
        BRACKETS (dict): A dictionary containing information about income brackets,
                        including lower and upper limits and corresponding tax rates.
                        Keys represent bracket names.
    """

    BRACKETS = [
        {'upper_limit': 11294, 'rate': 0.0},
        {'lower_limit': 11294, 'upper_limit': 28797, 'rate': 0.11},
        {'lower_limit': 28797, 'upper_limit': 82341, 'rate': 0.3},
        {'lower_limit': 82341, 'upper_limit': 177106, 'rate': 0.41},
        {'lower_limit': 177106, 'rate': 0.45}
    ]

    def __init__(self, income, familly_quotient=1):
        """
        Initialize the FrenchIncomeTaxCalculator with the provided income.

        Parameters:
            income (float): The annual income for tax calculation.
            familly_quotient (int): The number of tax household shares.
        """

        self.income = income
        self.familly_quotient = familly_quotient

    def calculate_tax(self):
        """
        Calculate the tax on the provided income based on the specified French tax brackets.

        Returns:
            float: The calculated tax amount rounded to two decimal places.
        """

        tax = 0
        remaining_income = self.income // self.familly_quotient

        for bracket in self.BRACKETS:
            lower_limit = bracket.get('lower_limit', 0)
            upper_limit = bracket.get('upper_limit', float('inf'))
            rate = bracket['rate']

            taxable_amount = min(remaining_income, upper_limit - lower_limit)
            tax += taxable_amount * rate
            remaining_income -= taxable_amount

            if remaining_income <= 0:
                break

        return round(tax, 2)


def main():
    """main"""
    print('Taxes')
    print('=' * 50 + '\n')

    annual_income = int(input('Annual taxable income: ').strip())
    familly_quotient = int(input('Familly quotient: ').strip())
    tax_calculator = FrenchIncomeTaxCalculator(annual_income, familly_quotient)
    calculated_taxes = tax_calculator.calculate_tax()

    print(f"Taxes calculated for an annual income of {annual_income} €: {calculated_taxes} €")

    available_income = round(annual_income - calculated_taxes, 2)

    print(f"Available income after taxes : {available_income} €")


if __name__ == '__main__':
    main()
