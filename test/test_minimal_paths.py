import unittest
from simulation.model import CommunicationNetwork
from simulation.minimal_paths import (
    single_source_dijkstra_hyperedges,
    single_source_dijkstra_vertices,
    DistanceType,
)


class self(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.cn = CommunicationNetwork(
            {"h1": ["v1", "v2"], "h2": ["v2", "v3"], "h3": ["v3", "v4"]},
            {"h1": 1, "h2": 2, "h3": 3},
        )
        self.cn2 = CommunicationNetwork({"h1": ["v1"]}, {"h1": 0})

    def test_short_correct(self):
        self.assertEqual(
            single_source_dijkstra_vertices(
                self.cn, "v1", DistanceType.SHORTEST, min_timing=0
            ),
            {"v2": 1, "v3": 2, "v4": 3},
        )

    def test_hyper_vert_shortest(self):
        result_1 = single_source_dijkstra_vertices(
            self.cn, "v1", DistanceType.SHORTEST, min_timing=0
        )
        result_2 = single_source_dijkstra_hyperedges(
            self.cn, "v1", DistanceType.SHORTEST, min_timing=0
        )
        self.assertEqual(
            result_1,
            result_2,
            "Single-source Dijkstra implementations are not equivalent",
        )

    def test_hyper_vert_fastest(self):
        result_1 = single_source_dijkstra_vertices(
            self.cn, "v1", DistanceType.FASTEST, min_timing=0
        )
        result_2 = single_source_dijkstra_hyperedges(
            self.cn, "v1", DistanceType.FASTEST, min_timing=0
        )
        self.assertEqual(
            result_1,
            result_2,
            "Single-source Dijkstra implementations are not equivalent",
        )

    def test_hyper_vert_foremost(self):
        result_1 = single_source_dijkstra_vertices(
            self.cn, "v1", DistanceType.FOREMOST, min_timing=0
        )
        result_2 = single_source_dijkstra_hyperedges(
            self.cn, "v1", DistanceType.FOREMOST, min_timing=0
        )
        self.assertEqual(
            result_1,
            result_2,
            "Single-source Dijkstra implementations are not equivalent",
        )

    def test_empty_network(self):
        result1 = single_source_dijkstra_vertices(
            self.cn, "v1", DistanceType.FASTEST, min_timing=0
        )
        result2 = single_source_dijkstra_vertices(
            self.cn2, "v1", DistanceType.FASTEST, min_timing=0
        )
        self.assertNotEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
