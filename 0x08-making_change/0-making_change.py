#!/usr/bin/python3

"""
    Interview preparation exercise: Making change
        Given a pile of coins of different values, determine the fewest number
        of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
        @coins: list of values of coins in possession
        @total: total amount that needs to be attained
        Return: fewest number of coins needed to meet total
                0, if total is 0 or less
                -1, if total cannot be met by any number of coins
        * The value of a coin will always be an integer greater than 0
        * You can assume you have an infinite number of each denomination
           of coin in the list
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    success = False
    for i in range(len(sorted_coins)):
        temp = total
        coin_count = 0
        for j in range(i, len(sorted_coins)):
            if temp >= sorted_coins[j]:
                coin_count += temp // sorted_coins[j]
                temp %= sorted_coins[j]
            if temp == 0:
                success = True
                break
        if success:
            return coin_count
    return -1
