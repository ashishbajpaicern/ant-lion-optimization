# ant lion optimization
import matplotlib.pyplot as plt
import math
import random
import numpy as np


def antlion_optimization():
    # initialization
    n = 1000
    x = np.zeros((n, 2))
    v = np.zeros((n, 2))
    f = np.zeros((n, 1))
    fbest = np.zeros((n, 1))
    xbest = np.zeros((n, 2))
    # initializing the population
    for i in range(n):
        x[i, 0] = random.uniform(-5, 5)
        x[i, 1] = random.uniform(-5, 5)
        v[i, 0] = random.uniform(-5, 5)
        v[i, 1] = random.uniform(-5, 5)
        f[i] = 100*(x[i, 1] - x[i, 0]**2)**2 + (1 - x[i, 0])**2
        fbest[i] = f[i]
        xbest[i] = x[i, :]
    # initializing the best solutions
    fbestglobal = fbest[0]
    xbestglobal = xbest[0, :]
    for i in range(n):
        if fbest[i] < fbestglobal:
            fbestglobal = fbest[i]
            xbestglobal = xbest[i, :]
    # initializing the ant lions
    antlion = np.zeros((n, 2))
    for i in range(n):
        antlion[i, 0] = random.uniform(-5, 5)
        antlion[i, 1] = random.uniform(-5, 5)
    # optimization loop
    for k in range(1000):
        for i in range(n):
            for j in range(n):
                if f[i] < f[j]:
                    v[i, :] = v[i, :] + (x[i, :] - x[j, :])
                    x[i, :] = x[i, :] + v[i, :]
                    f[i] = 100*(x[i, 1] - x[i, 0]**2)**2 + (1 - x[i, 0])**2
                    if f[i] < fbest[i]:
                        fbest[i] = f[i]
                        xbest[i, :] = x[i, :]
                    if f[i] < fbestglobal:
                        fbestglobal = f[i]
                        xbestglobal = x[i, :]
            # for ant lions
            for j in range(n):
                if f[i] > f[j]:
                    v[i, :] = v
                    x[i, :] = antlion[j, :]
                    f[i] = 100*(x[i, 1] - x[i, 0]**2)**2 + (1 - x[i, 0])**2
                    if f[i] < fbest[i]:
                        fbest[i] = f[i]
                        xbest[i, :] = x[i, :]
                    if f[i] < fbestglobal:
                        fbestglobal = f[i]
                        xbestglobal = x[i, :]
            for j in range(n):
                if f[i] == f[j]:
                    if random.uniform(0, 1) < 0.5:
                        v[i, :] = v[i, :] + (x[i, :] - x[j, :])
                        x[i, :] = x[i, :] + v[i, :]
                        f[i] = 100*(x[i, 1] - x[i, 0]**2)**2 + (1 - x[i, 0])**2
                        if f[i] < fbest[i]:
                            fbest[i] = f[i]
                            xbest[i, :] = x[i, :]
                        if f[i] < fbestglobal:
                            fbestglobal = f[i]
                            xbestglobal = x[i, :]
                    else:
                        v[i, :] = v
                        x[i, :] = antlion[j, :]
                        f[i] = 100*(x[i, 1] - x[i, 0]**2)**2 + (1 - x[i, 0])**2
                        if f[i] < fbest[i]:
                            fbest[i] = f[i]
                            xbest[i, :] = x[i, :]
                        if f[i] < fbestglobal:
                            fbestglobal = f[i]
                            xbestglobal = x[i, :]

    print('The best solution is: ', xbestglobal)
