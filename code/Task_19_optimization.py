
import numpy as np
from scipy.optimize import minimize

# x = number/capacity units of Type A server
# y = number/capacity units of Type B server

# Cost per unit: A = 12, B = 22
# Capacity per unit: A = 100, B = 170
# Required total capacity: at least 1000

def cost(z):
    x, y = z
    return 12 * x + 18 * y

def capacity_constraint(z):
    x, y = z
    return 100 * x + 170 * y - 1000

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Minimum cost: {cost(solution.x):.3f}")
print(f"Total capacity: {100*x + 170*y:.3f}")
