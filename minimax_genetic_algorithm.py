import random
import time
from utils import get_distance

class MinimaxGeneticAlgorithm:
    def __init__(self, notes, start_position, population_size=100, generations=500, mutation_rate=0.01, penalty_weight=2.0):
        self.notes = notes
        self.start_position = start_position
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.penalty_weight = penalty_weight

    def initial_population(self):
        return [random.sample(self.notes, len(self.notes)) for _ in range(self.population_size)]

    def fitness(self, individual):
        total_distance = 0
        max_leg = 0
        current_pos = self.start_position

        for note in individual:
            dist = get_distance(current_pos, note.position)
            total_distance += dist
            max_leg = max(max_leg, dist)
            current_pos = note.position

        # Return fitness: lower is better
        return total_distance + self.penalty_weight * max_leg

    def select_parents(self, population):
        # Tournament selection
        tournament_size = 5
        return min(random.sample(population, tournament_size), key=self.fitness)

    def crossover(self, parent1, parent2):
        # Ordered crossover (OX)
        size = len(parent1)
        start, end = sorted(random.sample(range(size), 2))
        child_p1 = parent1[start:end]
        child_p2 = [note for note in parent2 if note not in child_p1]
        return child_p2[:start] + child_p1 + child_p2[start:]

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                j = random.randint(0, len(individual) - 1)
                individual[i], individual[j] = individual[j], individual[i]

    def evolve(self, population):
        new_population = []
        for _ in range(self.population_size):
            parent1 = self.select_parents(population)
            parent2 = self.select_parents(population)
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        return new_population

    def solve(self):
        population = self.initial_population()
        start_time = time.time()

        for gen in range(1, self.generations + 1):
            population = self.evolve(population)
            best = min(population, key=self.fitness)
            best_fitness = self.fitness(best)

            elapsed = time.time() - start_time
            print(f"Generation {gen}/{self.generations} | Best Fitness: {best_fitness:.2f} | Elapsed: {elapsed:.1f}s")

        # Final best solution
        best = min(population, key=self.fitness)
        route = [self.start_position] + [note.position for note in best]
        return route
