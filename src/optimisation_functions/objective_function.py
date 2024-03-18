import numpy as np

def objective_function(track_outer_coords, track_inner_coords, racing_line):
    
    # Penalty for deviating too far from the track boundaries
    boundary_penalty = np.mean(np.linalg.norm(racing_line - (track_inner_coords + track_outer_coords) / 2, axis=1))
    
    # Penalty for sharp changes in direction (lack of smoothness)
    smoothness_penalty = np.mean(np.abs(np.diff(np.diff(racing_line, axis=0), axis=0)))
    
    # Calculate cornering speeds based on curvature of the racing line
    curvature = np.abs(np.gradient(np.arctan2(np.gradient(racing_line[:, 1]), np.gradient(racing_line[:, 0]))))
    cornering_speed = 1 / (1 + curvature)
    max_cornering_speed = np.max(cornering_speed)
    
    # Normalize penalties and cornering speed to the range [0, 1]
    boundary_penalty /= np.max(np.linalg.norm(track_outer_coords - track_inner_coords, axis=1))
    smoothness_penalty /= np.max(np.abs(np.diff(track_inner_coords, axis=0)))
    max_cornering_speed /= np.max(cornering_speed)
    
    # Combine penalties and cornering speed into an overall score
    score = 1 - (0.3 * boundary_penalty + 0.3 * smoothness_penalty + 0.4 * (1 - max_cornering_speed)) # Default values: 0.3 0.3 0.4
    
    return score