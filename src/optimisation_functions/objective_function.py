import numpy as np

def objective_function(outer_track, inner_track, racing_line):
    
    lambda_smoothness = 0.1  # Adjust this parameter to control the importance of smoothness
    
    # Calculate curvature of the racing line
    racing_line_curvature = calculate_curvature(racing_line[:, 0], racing_line[:, 1])
    
    # Calculate penalty for abrupt changes in curvature
    curvature_change_penalty = np.abs(np.diff(racing_line_curvature))
    
    # Combine curvature and smoothness penalty
    objective = np.sum(racing_line_curvature) + lambda_smoothness * np.sum(curvature_change_penalty)
    
    return objective


def calculate_curvature(x, y):
    # Calculate curvature at each point along the racing line
    dx_dt = np.gradient(x)
    dy_dt = np.gradient(y)
    d2x_dt2 = np.gradient(dx_dt)
    d2y_dt2 = np.gradient(dy_dt)
    curvature = np.abs(dx_dt * d2y_dt2 - dy_dt * d2x_dt2) / (dx_dt**2 + dy_dt**2)**1.5
    return curvature
