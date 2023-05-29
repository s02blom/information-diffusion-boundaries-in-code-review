import unittest

from simulation.model import CommunicationNetwork, EntityNotFound


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
        with self.assertRaises(EntityNotFound):
            self.empty_cn.vertices("v3")

    def test_invalid_hyperedges(self):
        with self.assertRaises(EntityNotFound):
            self.empty_cn.hyperedges("h2")

    def test_timings(self):
        with self.assertRaises(EntityNotFound):
            self.empty_cn.timings("h2")


class CommunicationNetworkTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.cn = CommunicationNetwork(
            {"h1": ["v1", "v2"], "h2": ["v2", "v3"], "h3": ["v3", "v4"]},
            {"h1": 1, "h2": 2, "h3": 3},
        )
        self.empty_cn = CommunicationNetwork({"h1": ["v1"]}, {"h1": 0})
    
    def setUp(self):
        channels = {"h1": ["v1", "v2"], "h2": ["v2", "v3"], "h3": ["v3", "v4"]}
        channel_timing = {"h1":1, "h2":2, "h3":3}
        self.cn = CommunicationNetwork(channels, channel_timing)

    def test_invalid_vert(self):
        invalid_vert = "v69"
        with self.assertRaises(EntityNotFound) as context:
            self.cn.vertices(invalid_vert)
            self.assertEqual(str(context.exception), f"Unkown vertex {invalid_vert}")
        
    def test_invalid_hyp_edge(self):
        invalid_hyp_edge = "h69"
        with self.assertRaises(EntityNotFound) as context:
            self.cn.hyperedges(invalid_hyp_edge)
            self.assertEqual(str(context.exception), f"Unkown hyperedge {invalid_hyp_edge}")

    def test_timing_for_vert(self):
        vertex = "v3"
        expected_timing = 2
        timings = self.cn.timings(vertex)
        self.assertEqual(timings, expected_timing)
    
    def test_timing_for_hyp_edge(self):
        hyper_edge = "h2"
        expected_timing = 2
        timings = self.cn.timings(hyper_edge)
        self.assertEqual(timings, expected_timing)


    def test_channels(self):
        self.assertEqual(len(self.cn.channels()), 3)
        self.assertEqual(self.cn.channels("v1"), {"h1"})

    def test_participants(self):
        self.assertEqual(len(self.empty_cn.participants()), 1)
        self.assertEqual(self.empty_cn.participants("h1"), {"v1"})

    def test_invalid_file_path(self):
        with self.assertRaises(EntityNotFound):
            self.empty_cn.from_json("", None)


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
