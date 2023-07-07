#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:24:29 2023

@author: heinhundal


This is an extreme simplification of the game Master of Orion.  We estimate the 
growth rate of the economy with the Lambert Growth Formula

r = W(T*I/C)/T

where W is th LambertW function, T is the delay between colony ship production 
and the maturing of the colony, I is the income of the mature colony, 
and C is the cost of the colony ship

Each turn 

"""

import numpy as np
from scipy.special import lambertw
import matplotlib.pyplot as plt

# define constants
rProduction0 = 80.0   # income of the first planet
C = 550.0             # cost of colony ship
I = 80                # net income of a mature colony 
iTurns = 500          # length of the simulation
T = 30                # number of turns between the creation of a colony
                      # ship and the maturing of the new colony

# calculate Lambert growth rate
rLambertGrowth = lambertw(I * T / C).real / T
rRatEst = np.exp(rLambertGrowth)

rProduction = rProduction0
vShips = np.zeros(iTurns)
mResults = []

for i in range(iTurns):
    if i >= T:
        # this formula assumes that every colony ship produced on turn i 
        # creates a mature colony T turns later whose net production
        # is I
        rProduction += vShips[i - T] * I
    
    # unlike the real game, the number of colony ships built is float
    # rather than an integer.
    vShips[i] = rProduction / C
    mResults.append([i, rProduction, vShips[i]])

mResults = np.array(mResults)

# calculate average growth rate over the last 10 turns of the sim
rGrowthRateSim = np.log(mResults[-1, 1] / mResults[-11, 1]) / 10

print("Actual Growth Rate In Simulation: ".ljust(61), rGrowthRateSim)
print("Estimated Growth from Lambert Growth Formula: ".ljust(61), rLambertGrowth)

# you can get a more accurate estimate of the growth rate by 
# taking the log of the first root of
#   x^T - x^(T-1) 

print("Log of the unique positive root of x^(T) - x^(T-1) - I/C is: ", 0.04205855022122076)

# plot the production
plt.plot(mResults[:, 0], np.log(mResults[:, 1]))
plt.title('Production Over Time')
plt.xlabel('Time')
plt.ylabel('Log Production')
plt.grid(True)
plt.show()

print("Slope of the line in the plot above is the growth rate")
