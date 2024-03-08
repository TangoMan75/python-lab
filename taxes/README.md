Taxes
===

This script was inspired by the following Grafikart video :
- [Coding Challenge : JS Impot.calculate()](https://www.youtube.com/watch?v=cX-5J_cy8TM)

## 📑 Overview

A class to calculate taxes on French incomes based on specified brackets.

- Income bracket up to €11294 taxed at 0%
- Income bracket from €11294 to €28797 taxed at 11%
- Income bracket from €28797 to €82341 taxed at 30%
- Income bracket from €82341 to €177106 taxed at 41%
- Income bracket over €177106 taxed at 45%

https://www.economie.gouv.fr/particuliers/tranches-imposition-impot-revenu

## 📚 Implementation Details

`FrenchIncomeTaxCalculator` calculates the tax owed on a given annual income by dividing the income into tax brackets and applying the corresponding tax rate to each bracket.
It takes in the annual income as input.
It outputs the total calculated tax amount.

The class first defines the `BRACKETS` constant, which is a list of dictionaries representing the tax brackets.
Each dictionary has keys for the lower limit, upper limit, and tax rate for that bracket.

When initialized, `FrenchIncomeTaxCalculator` takes the annual income and saves it to `self.income`.

The `calculate_tax()` method does the tax calculation.
It initializes the total tax to _0_ and sets `remaining_income` to the full income amount.

It then loops through the `BRACKETS`, using the lower and upper limits to find the taxable amount for that bracket.
It applies the bracket's tax rate to that amount, adds it to the running tax total, and subtracts the taxable amount from `remaining_income`.

This continues until `remaining_income` drops below _0_, at which point the loop breaks.
Finally, it returns the total tax rounded to _2_ decimal places.

## ⏳ TLDR;

So in summary, `FrenchIncomeTaxCalculator` takes an annual income, divides it into tax brackets, calculates the tax per bracket, sums the bracket taxes, and returns the total tax amount.
The key steps are splitting the income into brackets and applying the correct rates per bracket.

