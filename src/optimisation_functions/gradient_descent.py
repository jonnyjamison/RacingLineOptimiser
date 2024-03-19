#TODO
#Make learning rate and tolerance accessible in Settings via GUI

import numpy as np
from optimisation_functions.objective_function import objective_function

learning_rate = 5
tolerance = 0.0000001

 # track_coords, track_outer_coords, track_inner_coords, max_iterations):
 

def gradient_descent(racing_line, inner_bounds, outer_bounds, learning_rate=0.01, max_iterations=1000, tolerance=1e-5):
    iteration = 0
    prev_cost = float('inf')

    while iteration < max_iterations:
        # Compute the gradient of the cost function with respect to racing_line
        gradient = compute_gradient_rate_of_change_of_curvature(racing_line)

        # Update the racing line parameters
        racing_line -= learning_rate * gradient

        # Enforce boundary constraints
        racing_line = enforce_boundary_constraints(racing_line, inner_bounds, outer_bounds)

        # Compute the new cost
        new_cost = cost_function_rate_of_change_of_curvature(racing_line)

        # Check for convergence
        if abs(prev_cost - new_cost) < tolerance:
            break

        prev_cost = new_cost
        iteration += 1

    return racing_line
    
    
    
def curvature(p1, p2, p3):
    # Compute the curvature at p2 based on points p1, p2, and p3
    # Formula for curvature: |x1y2 + x2y3 + x3y1 - x1y3 - x2y1 - x3y2| / ((x1^2 + y1^2)(x2y3 - x3y2 + x3y1 - x1y3 + x1y2 - x2y1)^1.5)
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    numerator = abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)
    denominator = ((x1**2 + y1**2) * (x2*y3 - x3*y2 + x3*y1 - x1*y3 + x1*y2 - x2*y1)) ** 1.5
    if denominator == 0:
        return float('inf')
    else:
        return numerator / denominator

def rate_of_change_of_curvature(racing_line):
    # Compute the rate of change of curvature along the racing line
    n = len(racing_line)
    roc_curvature = np.zeros(n)

    for i in range(1, n-1):
        roc_curvature[i] = abs(curvature(racing_line[i-1], racing_line[i], racing_line[i+1]))

    return roc_curvature

def cost_function_rate_of_change_of_curvature(racing_line):
    # Define a cost function based on the rate of change of curvature
    roc_curvature = rate_of_change_of_curvature(racing_line)
    return np.sum(roc_curvature)



def compute_gradient_rate_of_change_of_curvature(racing_line):
    # Compute the gradient of the cost function with respect to racing_line
    # Using numerical differentiation
    epsilon = 1e-5
    gradient = np.zeros_like(racing_line)

    for i in range(len(racing_line)):
        for j in range(racing_line.shape[1]):
            perturbation = np.zeros_like(racing_line)
            perturbation[i, j] = epsilon
            gradient[i, j] = (cost_function_rate_of_change_of_curvature(racing_line + perturbation) - cost_function_rate_of_change_of_curvature(racing_line - perturbation)) / (2 * epsilon)

    return gradient


def enforce_boundary_constraints(racing_line, inner_bounds, outer_bounds):
    # Project the racing line onto the nearest point on the inner and outer track boundaries
    for i in range(len(racing_line)):
        inner_point = inner_bounds[np.argmin(np.linalg.norm(racing_line[i] - inner_bounds, axis=1))]
        outer_point = outer_bounds[np.argmin(np.linalg.norm(racing_line[i] - outer_bounds, axis=1))]
        racing_line[i] = (inner_point + outer_point) / 2  # Project onto the midpoint between inner and outer boundaries
    return racing_line