#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   SECOND BANKER'S PROBLEM

import numpy as np
import matplotlib.pyplot as plt

def balance(t, t1, r1, r2, c, b0):
    tdone = t1 + c / (b0 * r1 * np.exp(r1 * t1))
    constbal = b0 * np.exp(r1 * t1)
    
    if t < t1:
        return b0 * np.exp(r1 * t)
    elif t < tdone:
        return constbal
    else:
        return constbal * np.exp(r2 * (t - tdone))

b0 = 1000
r1 = 0.05
r2 = 0.08
c = 1100
tbuy = 1 / r1 * np.log(c * r2 / (b0 * (r2 - r1)))
tsurpass = tbuy + 1 / r1
ttest = int(np.round(tsurpass + 1))

print("optimal buy time =", tbuy)
print("balance at year", ttest, "using optimal strategy", balance(ttest, tbuy, r1, r2, c, b0))

data = [[t1, balance(ttest, t1, r1, r2, c, b0)] for t1 in range(1, 41)]
print("\nYear of Purchase and Balance at  t=" + str(ttest))
for row in data:
    print(row)

t1_values = np.arange(1, 41)
balance_values = [balance(ttest, t1, r1, r2, c, b0) for t1 in t1_values]

plt.plot(t1_values, balance_values)
plt.scatter(tbuy, balance(ttest, tbuy, r1, r2, c, b0), color='red', label='Optimal Buy Time')
plt.xlabel('Year of Purchase')
plt.ylabel('Balance at t='+str(ttest) )
plt.grid(True)
plt.legend()
plt.show()
