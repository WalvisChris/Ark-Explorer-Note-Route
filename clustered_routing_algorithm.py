import random
import math
from utils import get_distance

class ClusteredRoutingAlgorithm:
    def __init__(self, notes, k, start_position):
        """
        notes: List of notes with positions
        k: Number of clusters to divide the points into
        start_position: Starting point of the journey
        """
        self.notes = notes
        self.k = k
        self.start_position = start_position

    def initialize_centroids(self):
        """
        Initialize centroids using KMeans++ strategy.
        """
        centroids = [random.choice(self.notes).position]  # Start with a random point

        for _ in range(1, self.k):
            distances = []
            for note in self.notes:
                dist_to_nearest_centroid = min(get_distance(note.position, centroid) for centroid in centroids)
                distances.append(dist_to_nearest_centroid)
            
            # Select a point randomly weighted by the squared distance to the nearest centroid
            total_distance = sum(distances)
            random_choice = random.uniform(0, total_distance)
            cumulative_sum = 0
            for i, dist in enumerate(distances):
                cumulative_sum += dist
                if cumulative_sum >= random_choice:
                    centroids.append(self.notes[i].position)
                    break

        return centroids

    def assign_to_clusters(self, centroids):
        """
        Assign each note to the nearest centroid (cluster).
        """
        clusters = {i: [] for i in range(self.k)}

        for note in self.notes:
            closest_centroid_idx = min(range(self.k), key=lambda i: get_distance(note.position, centroids[i]))
            clusters[closest_centroid_idx].append(note)

        return clusters

    def update_centroids(self, clusters):
        """
        Recompute centroids of each cluster.
        """
        new_centroids = []
        for cluster in clusters.values():
            avg_x = sum(note.position[0] for note in cluster) / len(cluster)
            avg_y = sum(note.position[1] for note in cluster) / len(cluster)
            new_centroids.append((avg_x, avg_y))
        
        return new_centroids

    def solve(self):
        """
        Solve the clustering problem and return the route.
        """
        # Initialize centroids using KMeans++ strategy
        centroids = self.initialize_centroids()

        prev_centroids = None
        iterations = 0
        while prev_centroids != centroids:
            iterations += 1
            print(f"\033[91mClustered Routing Algorithm:\033[0m Iteration {iterations}...")
            prev_centroids = centroids
            clusters = self.assign_to_clusters(centroids)
            centroids = self.update_centroids(clusters)

        # After clusters are formed, apply a greedy approach within each cluster
        route = [self.start_position]
        for cluster_idx in range(self.k):
            cluster_route = self.greedy_within_cluster(clusters[cluster_idx], route[-1])
            route.extend(cluster_route)
        
        return route

    def greedy_within_cluster(self, cluster, start_position):
        """
        Greedily solve the route within a single cluster.
        """
        route = [start_position]
        remaining = cluster[:]
        current_position = start_position

        while remaining:
            next_note = min(remaining, key=lambda note: get_distance(current_position, note.position))
            route.append(next_note.position)
            remaining.remove(next_note)
            current_position = next_note.position
        
        return route