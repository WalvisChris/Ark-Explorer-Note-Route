import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from note import Note
from algorithms.nearest_neighbor import NearestNeighbor
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.christofides_algorithm import ChristofidesAlgorithm
from algorithms.minimax_genetic_algorithm import MinimaxGeneticAlgorithm
from algorithms.goverwelle_algorithm import GoverwelleAlgorithm
from algorithms.clustered_routing_algorithm import ClusteredRoutingAlgorithm
from algorithms.hilbert_curve_ordering import HilbertCurveAlgorithm
from algorithms.lin_kernighan_heuristic import LinKernighanHeuristic

from utils import load_notes
from graph_plotter import GraphPlotter

def main():
    ExplorerNotes = load_notes()

    os.system("cls")
    starting_x = float(input("x: "))
    starting_y = float(input("y: "))
    start = (starting_x, starting_y)

    # region Neighbor Algorithm
    nn = NearestNeighbor(ExplorerNotes)
    nn_route = nn.find_route(start)
    # endregion

    # region Simulated Annealing Algorithm
    sa = SimulatedAnnealing(ExplorerNotes, start)
    sa_route = sa.solve()
    # endregion

    # region Christofides Algorithm
    ca = ChristofidesAlgorithm(ExplorerNotes, start)
    ca_route = ca.solve()
    # endregion

    # region Minimax Genetic Algorithm
    mg = MinimaxGeneticAlgorithm(ExplorerNotes, start, generations=50)
    mg_route = mg.solve()
    # endregion

    # region Goverwelle Algorithm
    ga = GoverwelleAlgorithm(ExplorerNotes, start)
    ga_route = ga.solve()
    # endregion

    # region Clustered Routing Algorithm
    cr = ClusteredRoutingAlgorithm(ExplorerNotes, 10, start)
    cr_route = cr.solve()
    # endregion

    # region Hilbert Curve Ordering
    hc = HilbertCurveAlgorithm(ExplorerNotes, start)
    hc_route = hc.solve()
    # endregion

    # region Lin-Kernighan Heuristic
    lk = LinKernighanHeuristic(ExplorerNotes, start)
    lk_route = lk.solve()
    # endregion

    # Show result
    plotter = GraphPlotter()
    plotter.plot_route(mg_route, start, "Minimax Genetic Algorithm")
    plotter.plot_route(sa_route, start, "Simulated Annealing Algorithm")
    plotter.plot_route(ca_route, start, "Christofides Algorithm")
    plotter.plot_route(cr_route, start, "Clustered Routing Algorithm")
    plotter.plot_route(hc_route, start, "Hilbert Curve Ordering")
    plotter.plot_route(nn_route, start, "Nearest Neighbor Algorithm")
    plotter.plot_route(ga_route, start, "Goverwelle Algorithm")
    plotter.plot_route(lk_route, start, "Lin-Kernighan Heuristic")

if __name__ == "__main__":
    main()