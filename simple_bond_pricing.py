#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:36:05 2020

@author: shavak
"""

import numpy as np
import scipy.optimize as optimize

def cheapest_to_deliver_helper(quoted_price, settlement_price,
                               conversion_factor):
    a = quoted_price - (settlement_price * conversion_factor)
    return np.argmin(a), a 

x0 = 100 * np.exp(-0.052 * 1.5)

x1 = 2 * np.exp(-0.052 * 0.5) +\
    2 * np.exp(-0.052 * 1.0) +\
    102 * np.exp(-0.052 * 1.5)
    
x2 = 2 / (1.026) + 2 / (1.026**2) + 102 / (1.026**3)

R = 2 * ((102.0 / (x2 - 2 / (1.025) - 2 / (1.025**2))) ** (1 /3) - 1)

x = np.linspace(-0.040, -0.048, 5)
t = np.linspace(0.5, 2.5, 5)
B = 0.02 * np.sum(np.exp(x * t)) + np.exp(-0.048 * 2.5)

t = np.linspace(0.5, 3.0, 6)
f = lambda y : 4.0 * np.sum(np.exp(-y * t)) + 100 * np.exp(-y * 3.0) - 104.0
y = optimize.root(f, x0 = 0.08)["x"][0] * 100

t = np.linspace(0.5, 2.0, 4)
r = np.array([0.05, 0.06, 0.065, 0.07])
c = 100.0 * 2.0 * (1.0 - np.exp(-0.07 * 2.0)) / (np.sum(np.exp(-r * t)))

t = np.linspace(1.0, 5.0, 5)
y = 0.068
c = 8.0 * np.ones(5)
c[4] += 100.0
B = np.sum(c * np.exp(-y * t))
D = np.sum(t * c * np.exp(-y * t)) / B

r = -(2 / 3) * np.log((94.84 - 4 * 0.94 - 4 * 0.89) / 104.0)

r = -0.5 * np.log((97.12 - 5 * 0.94 - 5 * 0.89 -
                  5 * ((94.84 - 4 * 0.94 - 4 * 0.89) / 104.0)) / 105.0)

F0 = 30.0 * np.exp(0.05 * 0.5) 
F0 = 350.0 * np.exp(0.01 / 3)
F0 = 40.0 * np.exp(0.05)
F0 = 45.0 * np.exp(0.05 / 2)
F0 = 1300 * np.exp((0.04 * 5 / 12) - (0.05 * 2 + 0.02 * 3) / 12)
F0 = 400.0 * np.exp((0.06 - 0.04) / 3)

r_delta = np.log(0.94320 / 0.94105) * 400

t = np.linspace(0.0, 0.75, num = 4)
F_0 = (25 + 0.06 * np.sum(np.exp(-t * 0.05))) * np.exp(0.75 * 0.05)
R = (3.2 * (440 - 350) + 3.0 * 350) / 440
N_star = (6.0e6  * 8.2) / (1000 * (108 + 15/32) * 7.6)
