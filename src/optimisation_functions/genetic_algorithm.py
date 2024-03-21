import numpy as np
from optimisation_functions.objective_function import objective_function

import random

# Genetic Algorithm
def genetic_algorithm(center_coords, inner_coords, outer_coords, max_iterations, population_size=100, mutation_rate=0.1):
    population = []

    # Initialize population with random racing lines
    for _ in range(population_size):
        racing_line = np.zeros(len(inner_coords))
        for i in range(len(inner_coords)):
            racing_line[i] = random.uniform(inner_coords[i], outer_coords[i])
        population.append(racing_line)

    # Main loop
    for generation in range(max_iterations):
        # Evaluate fitness of each racing line
        fitness_scores = [objective_function(racing_line) for racing_line in population]

        # Select parents for crossover
        parents = [population[i] for i in np.argsort(fitness_scores)[:population_size//2]]

        # Crossover
        children = []
        while len(children) < population_size - len(parents):
            parent1, parent2 = random.sample(parents, 2)
            crossover_point = random.randint(0, len(inner_coords) - 1)
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            children.append(child)

        # Mutation
        for i in range(len(children)):
            if random.random() < mutation_rate:
                mutation_point = random.randint(0, len(inner_coords) - 1)
                children[i][mutation_point] = random.uniform(inner_coords[mutation_point], outer_coords[mutation_point])

        # Replace old population with new generation
        population = parents + children

        # Print best solution in current generation
        best_index = np.argmin(fitness_scores)
        best_racing_line = population[best_index]
        print(f"Generation {generation+1}, Best Fitness: {fitness_scores[best_index]}")

    return best_racing_line
