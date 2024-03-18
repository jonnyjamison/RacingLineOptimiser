#TODO
#Make learning rate and tolerance accessible in Settings via GUI

import numpy as np
from optimisation_functions.objective_function import objective_function

learning_rate = 0.5
tolerance = 0.0000001


def gradient_descent(track_coords, track_outer_coords, track_inner_coords, max_iterations):
    
    # Intitial solution = original track coordinates
    current_solution = track_coords
    
    for i in range(max_iterations):
        gradient = gradient_function(track_outer_coords, track_inner_coords,current_solution)
        new_solution = current_solution - learning_rate * gradient
        if np.linalg.norm(new_solution - current_solution) < tolerance:
            print(f"i: {i} here")
            print((new_solution - current_solution))
            break
        current_solution = new_solution
    return current_solution
    

# Gradient function (approximated using finite differences)
def gradient_function(track_outer_coords, track_inner_coords, racing_line, epsilon=1e-5):

    gradient = np.zeros_like(racing_line)
    
    for i in range(len(racing_line)):
        perturbed_racing_line = np.copy(racing_line)
        perturbed_racing_line[i] += epsilon
        gradient[i] = (objective_function(track_outer_coords, track_inner_coords, 
            perturbed_racing_line) - objective_function(track_outer_coords, track_inner_coords,racing_line)) / epsilon
    return gradient