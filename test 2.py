import random

# define the objective function


def objective_function(x):
    return x**2 + x + 1

# define the rules or conditions for the solution


def rules(x):
    return x > -5 and x < 5

# define the kicks or transformations applied to the solution


def kick(x):
    return x + random.uniform(-1, 1)


# initialize the solution
x = 0

# iterate until the solution meets the rules
while not rules(x):
    # apply a kick to the solution
    x = kick(x)

# print the optimal solution
print(x)
