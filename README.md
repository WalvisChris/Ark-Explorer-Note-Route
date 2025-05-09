# Ark-Explorer-Note-Route  
Using algorithms to find the best/fastest way to explore all explorer notes  

# Algorithms  
- Christofides Algorithm: A heuristic for the Traveling Salesman Problem (TSP) that guarantees a solution within 1.5 times the optimal by combining minimum spanning tree, matching, and Eulerian circuits.  
- Clustered Routing: Divides nodes into clusters and solves routing within and between clusters to simplify complex routing problems.  
- Goverwelle Algortihm: My own algorithm, similair to nearest neighbor.  
- Hilbert Curve Orderning: Orders spatial points using a space-filling curve to preserve locality and improve performance in geometric or clustering algorithms.  
- Lin-Kernighan Heuristic: An advanced local search algorithm for TSP that iteratively swaps segments to reduce tour length.  
- Minimax Genetic Algorithm: A genetic algorithm that evolves solutions by minimizing the worst-case (maximum) cost or loss, often used in adversarial settings.  
- Nearest Neighbor: A greedy algorithm for TSP that builds a tour by repeatedly visiting the nearest unvisited city.  
- Simulated Annealing: A probabilistic optimization algorithm that explores solutions by accepting worse moves with decreasing probability to avoid local minima.  

# Details
> The explorer notes in this project `utils.py > load_notes` only contain the island notes, so no cave notes.  
> The code is not optimized.  
> The algorithms will show their progress in the output console.  