#!/usr/bin/env python3
import numpy as np

def assert_condition(condition, message):
    if not condition:
        raise ValueError(message)

# B0 - initial balance
def simBank1(B0, r1, r2, c, tbuy, tend, bPrint):
    assert_condition(B0 > 0, "failed assertion")
    assert_condition(r1 > 0, "failed assertion")
    assert_condition(r2 > r1, "failed assertion")
    assert_condition(c > 0, "failed assertion")
    assert_condition(tend > 0, "failed assertion")

    if B0 * np.exp(r1 * tbuy) <= c:
        print(f"Insufficient funds available to buy the rate increase at time {tbuy}")
        raise ValueError("InsufficientFunds")

    vOut = []
    balance = B0

    for t in range(1,tend + 1):
        if bPrint:
            print(f"t={t} balance={balance}")

        if tbuy - t >= 1:
            balance = balance * np.exp(r1)
        elif 0 <= tbuy - t < 1:
            bal1 = balance * np.exp(r1 * (tbuy - t))
            bal2 = bal1 - c
            balance = bal2 * np.exp(r2 * (t + 1 - tbuy))
            
            if bPrint:
                print([bal1, bal2, balance])
        else:
            balance = balance * np.exp(r2)

        vOut.append(balance)

    return vOut

# Example usage:
result = simBank1(1000, .05, .08, 1100, 50, 40, False)
print(result)
result = simBank1(1000, .05, .08, 1100, 21.5228, 40, False)
print(result)
