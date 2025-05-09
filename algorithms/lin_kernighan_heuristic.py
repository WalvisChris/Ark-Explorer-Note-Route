class LinKernighanHeuristic:
    def __init__(self, notes, starting_position):
        self.notes = notes  # List of notes (or points)
        self.starting_position = starting_position  # Starting position is given as a tuple (x, y)
        self.num_points = len(self.notes)
        self.distance_matrix = self.calculate_distance_matrix()

    def calculate_distance_matrix(self):
        """Calculate the distance matrix between all pairs of points."""
        distance_matrix = {}
        for i in range(self.num_points):
            distance_matrix[i] = {}
            for j in range(self.num_points):
                if i != j:
                    distance = ((self.notes[i].position[0] - self.notes[j].position[0]) ** 2 + 
                                (self.notes[i].position[1] - self.notes[j].position[1]) ** 2) ** 0.5
                    distance_matrix[i][j] = distance
                else:
                    distance_matrix[i][j] = float('inf')  # Distance to self is inf
        return distance_matrix

    def get_route_length(self, route):
        """Calculate the total length of the route."""
        length = 0
        for i in range(len(route) - 1):
            length += self.distance_matrix[route[i]][route[i + 1]]
        # Add distance from last point to the starting position to complete the loop
        length += self.distance_matrix[route[-1]][route[0]]
        return length

    def two_opt_swap(self, route, i, j):
        """Perform a 2-opt swap between two points in the route."""
        new_route = route[:i] + list(reversed(route[i:j + 1])) + route[j + 1:]
        return new_route

    def solve(self):
        """Solve the problem using the Lin-Kernighan Heuristic."""
        # Initialize the route as a list of point indices (starting with 0, 1, 2,...)
        route = list(range(self.num_points))

        # Add the starting position directly at the beginning of the route
        route = [0] + [i for i in range(self.num_points) if i != 0]

        # Try to improve the route using the Lin-Kernighan heuristic
        best_route = route
        best_length = self.get_route_length(best_route)

        # Perform multiple iterations of 2-opt swaps to improve the route
        max_iterations = 10  # Number of iterations for heuristic optimization
        for iteration in range(max_iterations):
            for i in range(self.num_points):
                for j in range(i + 1, self.num_points):
                    new_route = self.two_opt_swap(best_route, i, j)
                    new_length = self.get_route_length(new_route)

                    if new_length < best_length:
                        best_route = new_route
                        best_length = new_length

            # Print the progress
            print(f"\033[31mLin-Kernighan Heuristic Algorithm:\033[0m Iteration {iteration + 1}/{max_iterations}, Best Route Length: {best_length}")

        # Return the final best route with coordinates (from the 'position' attribute of the Note objects)
        route_with_coordinates = [self.notes[i].position for i in best_route]
        return route_with_coordinates