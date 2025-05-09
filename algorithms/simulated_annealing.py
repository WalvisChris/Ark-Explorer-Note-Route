import random
import math
from utils import get_distance

class SimulatedAnnealing:
    def __init__(self, notes, start_position):
        self.notes = notes
        self.start_position = start_position

    def initial_solution(self):
        # Create a random route, but start with the starting position
        remaining_notes = [note.position for note in self.notes]
        route = [self.start_position]
        remaining_notes = [note for note in remaining_notes if note != self.start_position]
        random.shuffle(remaining_notes)
        route.extend(remaining_notes)
        return route

    def get_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += get_distance(route[i], route[i + 1])
        # Add the return distance to the starting point
        distance += get_distance(route[-1], route[0])
        return distance

    def solve(self):
        current_solution = self.initial_solution()
        current_distance = self.get_distance(current_solution)

        # Simulated Annealing Parameters
        temperature = 10000
        cooling_rate = 0.995
        total_iterations = 10000  # You can change this for more or fewer iterations
        print("\033[35mSimulated Annealing:\033[0m Starting simulated annealing...")

        for iteration in range(total_iterations):
            # Create a new solution by swapping two random positions in the current solution
            new_solution = current_solution[:]
            i, j = random.sample(range(1, len(new_solution)), 2)  # Avoid swapping the start position
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_distance = self.get_distance(new_solution)

            # Accept the new solution if it's better or with a certain probability
            if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
                current_solution = new_solution
                current_distance = new_distance

            # Cool down
            temperature *= cooling_rate

            # Print progress every 100 iterations
            if iteration % 100 == 0 or iteration == total_iterations - 1:
                print(f"\033[35mSimulated Annealing:\033[0m Iteration {iteration}/{total_iterations} - Current Distance: {current_distance:.2f}, Temperature: {temperature:.2f}")

        print("\033[35mSimulated Annealing:\033[0m completed.")
        return current_solution