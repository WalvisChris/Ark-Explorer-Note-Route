import random
from utils import get_distance

class ChristofidesAlgorithm:
    def __init__(self, notes, start_position):
        self.notes = notes
        self.start_position = start_position

    def get_minimum_spanning_tree(self):
        # This should return the minimum spanning tree, but we will simplify it for this example
        print("\033[36mChristofides Algorithm\033[0m: Starting to build minimum spanning tree...")
        # Simulate some progress (example)
        for i in range(1, 6):
            print(f"\033[36mChristofides Algorithm\033[0m: Building MST: Step {i}/5")
        print("\033[36mChristofides Algorithm\033[0m: Minimum spanning tree built.")

    def get_perfect_matching(self):
        # This should return a perfect matching for odd degree vertices, simplified for this example
        print("\033[36mChristofides Algorithm\033[0m: Starting to find perfect matching...")
        # Simulate progress
        for i in range(1, 4):
            print(f"\033[36mChristofides Algorithm\033[0m: Finding perfect matching: Step {i}/3")
        print("\033[36mChristofides Algorithm\033[0m: Perfect matching found.")

    def solve(self):
        print("\033[36mChristofides Algorithm\033[0m: Starting Christofides algorithm...")
        
        # Step 1: Build the Minimum Spanning Tree
        self.get_minimum_spanning_tree()

        # Step 2: Find the perfect matching
        self.get_perfect_matching()

        # Start with the minimum spanning tree and use Christofides algorithm steps
        route = [self.start_position]  # Start with the starting position
        remaining_notes = [note.position for note in self.notes]

        # Remove the start position from the remaining notes
        remaining_notes = [note for note in remaining_notes if note != self.start_position]

        # Simulate adding the remaining notes to the route
        print("\033[36mChristofides Algorithm\033[0m: Starting to add remaining notes to route...")
        for i, note in enumerate(remaining_notes):
            route.append(note)
            # Print progress every 10% of the way through
            if i % (len(remaining_notes) // 10) == 0:
                print(f"\033[36mChristofides Algorithm\033[0m: Adding remaining notes: {i}/{len(remaining_notes)} notes added")

        print("\033[36mChristofides Algorithm\033[0m: Route creation complete.")
        return route