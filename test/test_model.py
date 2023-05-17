import unittest

from simulation.model import CommunicationNetwork


class test_model(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.cn = CommunicationNetwork(
            {"h1": ["v1", "v2"], "h2": ["v2", "v3"], "h3": ["v3", "v4"]},
            {"h1": 1, "h2": 2, "h3": 3},
        )
        self.empty_cn = CommunicationNetwork({"h1": ["v1"]}, {"h1": 0})

    def test_vertices_cn1(self):
        self.assertEqual(len(self.cn.vertices()), 4)
        self.assertEqual(self.cn.vertices("h1"), {"v1", "v2"})

    def test_hyperedges_cn1(self):
        self.assertEqual(len(self.cn.hyperedges()), 3)
        self.assertEqual(self.cn.hyperedges("v1"), {"h1"})

    def test_vertices_empty_cn(self):
        self.assertEqual(len(self.empty_cn.vertices()), 1)
        self.assertEqual(self.empty_cn.vertices("h1"), {"v1"})

    def test_hyperedges_empty_cn(self):
        self.assertEqual(len(self.empty_cn.hyperedges()), 1)
        self.assertEqual(self.empty_cn.hyperedges("v1"), {"h1"})

    def test_invalid_vertices(self):
        pass

    def test_invalid_hyperedges(self):
        pass


class ModelDataTest(unittest.TestCase):
    def test_model_with_data(self):
        communciation_network = CommunicationNetwork.from_json(
            "./data/networks/microsoft.json.bz2"
        )
        self.assertEqual(len(communciation_network.participants()), 37103)
        self.assertEqual(len(communciation_network.channels()), 309740)

        self.assertEqual(len(communciation_network.vertices()), 37103)
        self.assertEqual(len(communciation_network.hyperedges()), 309740)


if __name__ == "__main__":
    unittest.main()
