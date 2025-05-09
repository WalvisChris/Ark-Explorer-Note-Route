import math
from utils import get_distance

class GoverwelleAlgorithm:
    def __init__(self, notes, start_position):
        self.notes = notes
        self.start_position = start_position
    
    def get_closest_index(self, position: tuple, s: list) -> int:
        index = 0
        lowest = float('inf')

        for i, note in enumerate(self.notes):
            
            if note.position == position or note.position in s:
                continue

            distance = get_distance(position, note.position)
            
            if distance < lowest:
                lowest = distance
                index = i

        return index

    def solve(self):
        route = []
        currentNode = self.get_closest_index(self.start_position, route)

        print(f"\033[92mGoverwelle Algorithm:\033[0m {len(self.notes)} notes to check...")
        print(f"\033[92mGoverwelle Algorithm:\033[0m Starting at {self.notes[currentNode].position} {self.notes[currentNode]}\n")

        for i in range(len(self.notes) + 1):
            nextNote = self.get_closest_index(self.notes[currentNode].position, route)
            
            # debug
            name = str(self.notes[nextNote]).rjust(20)
            location = str(self.notes[nextNote].position).rjust(15)
            remaining = str(f"{len(self.notes) - len(route)} remaining").rjust(15)
            print(f"\033[92mGoverwelle Algorithm:\033[0m {name} {location} {remaining}")
            
            route.append(self.notes[nextNote].position)
            currentNode = nextNote

        return route