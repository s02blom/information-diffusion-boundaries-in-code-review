import unittest
from simulation.model import CommunicationNetwork
from simulation.minimal_paths import (
    single_source_dijkstra_hyperedges,
    single_source_dijkstra_vertices,
    DistanceType,
)


class test_minimal_path(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.cn1 = CommunicationNetwork(
            {"h1": ["v1", "v2"], "h2": ["v2", "v3"], "h3": ["v3", "v4"]},
            {"h1": 1, "h2": 2, "h3": 3},
        )
        self.cn2 = CommunicationNetwork({}, {})
        self.cn3 = CommunicationNetwork(
            {"h1": ["v1"], "h2": ["v2"], "h3": ["v3"]}, {"h1": 1, "h2": 1, "h3": 1}
        )
        self.cn5 = CommunicationNetwork({"h1":["v1","v2"],"h2":["v1","v2"],"h3":["v1","v2"]},{"h1":1,"h2":2,"h3":3})
    def test_short_correct(self):
        self.assertEqual(
            single_source_dijkstra_vertices(
                self.cn1, "v1", DistanceType.SHORTEST, min_timing=0
            ),
            {"v2": 1, "v3": 2, "v4": 3},
        )

    def test_hyper_vert_shortest(self):
        result_1 = single_source_dijkstra_vertices(
            self.cn1, "v1", DistanceType.SHORTEST, min_timing=0
        )
        result_2 = single_source_dijkstra_hyperedges(
            self.cn1, "v1", DistanceType.SHORTEST, min_timing=0
        )
        self.assertEqual(
            result_1,
            result_2,
            "Single-source Dijkstra implementations are not equivalent",
        )

    def test_hyper_vert_fastest(self):
        result_1 = single_source_dijkstra_vertices(
            self.cn1, "v1", DistanceType.FASTEST, min_timing=0
        )
        result_2 = single_source_dijkstra_hyperedges(
            self.cn1, "v1", DistanceType.FASTEST, min_timing=0
        )
        self.assertEqual(
            result_1,
            result_2,
            "Single-source Dijkstra implementations are not equivalent",
        )

    def test_hyper_vert_foremost(self):
        result_1 = single_source_dijkstra_vertices(
            self.cn1, "v1", DistanceType.FOREMOST, min_timing=0
        )
        result_2 = single_source_dijkstra_hyperedges(
            self.cn1, "v1", DistanceType.FOREMOST, min_timing=0
        )
        self.assertEqual(
            result_1,
            result_2,
            "Single-source Dijkstra implementations are not equivalent",
        )

    def test_empty_network_vertices(self):
        self.assertEqual(
            single_source_dijkstra_vertices(
                self.cn2, "", DistanceType.FASTEST, min_timing=0
            ),
            0,
            "Empty graph Dijkstra implementations are not equivalent",
        )

    def test_empty_network_hyperedges(self):
        self.assertEqual(
            single_source_dijkstra_hyperedges(
                self.cn2, "", DistanceType.FASTEST, min_timing=0
            ),
            0,
        )

    def test_non_connected_network(self):
        self.assertEqual(single_source_dijkstra_hyperedges(self.cn3,"v1",DistanceType.FASTEST,min_timing=0),single_source_dijkstra_vertices(self.cn3,"v1",DistanceType.FASTEST,min_timing=0))
    
    def test_connected_distance(self):
        self.assertEqual(single_source_dijkstra_vertices(self.cn3,"v1", DistanceType.SHORTEST,min_timing=0),{})
    def test_deep_connection_network(self):
       # print(single_source_dijkstra_hyperedges(self.cn5,"v1",DistanceType.FASTEST,min_timing=0))
        self.assertEqual(single_source_dijkstra_hyperedges(self.cn5,"v1",DistanceType.FOREMOST,min_timing=0),{"v2":1})

if __name__ == "__main__":
    unittest.main()
