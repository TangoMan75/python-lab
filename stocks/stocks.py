#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class Stocks:
    """
    Technical test: Return top three best average performing stocks from two lists.
    """

    def get_top_three(self, stocks: list, prices: list) -> list:
        """get_top_three"""
        if not isinstance(stocks, list):
            raise TypeError(f'{self.get_top_three.__qualname__}: expects parameter "stocks" to be of type list: {type(stocks)} given')

        if not isinstance(prices, list):
            raise TypeError(f'{self.get_top_three.__qualname__}: expects parameter "prices" to be of type list: {type(prices)} given')

        if len(stocks) != len(prices):
            raise ValueError(f'{self.get_top_three.__qualname__}: expects both lists to have same length: {len(stocks)} {len(prices)} given')

        if len(stocks) < 3:
            raise ValueError(f'{self.get_top_three.__qualname__}: expects lists to contain at least three items: {len(stocks)} {len(prices)} given')

        # declare "result" as a dictionary
        result = {}

        # storing average stock performance in dictionary as "stock_name[average]"
        for i, stock in enumerate(stocks):
            result[stock] = sum(prices[i]) / len(prices[i])

        # sort dictionary by ascending average values
        result = sorted(result.items(), key=lambda x: x[1], reverse=True)

        # return top three list as "['stock1', 'stock2', 'stock3']"
        return [result[0][0], result[1][0], result[2][0]]


def main():
    """main"""
    stocks = Stocks()

    print('Stocks')
    print('=' * 50 + '\n')

    stocks_list = ['AMZN', 'GOOGL', 'META', 'NFLX']
    prices_list = [
        [10, 11, 12, 13, 14],
        [20, 21, 22, 23, 24],
        [30, 31, 32, 33, 34],
        [40, 41, 42, 43, 44],
    ]
    print(stocks.get_top_three(stocks_list, prices_list))
    print('')


if __name__ == '__main__':
    main()
