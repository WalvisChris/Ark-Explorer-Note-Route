import math
from utils import get_distance

class NearestNeighbor:
    def __init__(self, notes):
        self.notes = notes
    
    def get_closest_index(self, position, route):
        index = 0
        lowest = float('inf')

        # Find the closest note to the current position, which is not already in the route
        for i, note in enumerate(self.notes):
            if note.position in route:
                continue
            distance = get_distance(position, note.position)
            if distance < lowest:
                lowest = distance
                index = i

        return index

    def find_route(self, start):
        route = [start]  # Start the route with the given start point
        current_position = start

        total_notes = len(self.notes)
        notes_visited = 1  # We start with the first note in the route

        print("\033[34mNearest Neighbor:\033[0m Starting the nearest neighbor search...")

        # Keep adding the closest note until we visit all the notes
        while len(route) < len(self.notes) + 1:
            next_note_index = self.get_closest_index(current_position, route)
            next_note = self.notes[next_note_index]
            route.append(next_note.position)
            current_position = next_note.position
            notes_visited += 1

            # Print progress every time we add a note to the route
            print(f"\033[34mNearest Neighbor:\033[0m Added {notes_visited}/{total_notes + 1} notes to the route.")

        print("\033[34mNearest Neighbor:\033[0m Route completed.")

        return route
