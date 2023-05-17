from datetime import datetime
from collections import defaultdict
from pathlib import Path
import bz2

try:
    import orjson as json
except ImportError:
    import json


class EntityNotFound(Exception):
    pass


class TimeVaryingHypergraph:
    def __init__(self, hedges: dict, timings: dict):
        self._vertices = defaultdict(list)
        for hedge, _vertices in hedges.items():
            for vertex in _vertices:
                self._vertices[vertex] += [hedge]

        self._hedges = hedges
        self._timings = timings

    def timings(self, entity=None):
        if entity is None:
            return self._timings
        return self._timings[entity]

    def vertices(self, hedge=None):
        if hedge is None:
            return set(self._vertices)
        if hedge in self._hedges:
            return set(self._hedges[hedge])
        raise EntityNotFound(f"Un   known hyperedge {hedge}")

    def hyperedges(self, vertex=None):
        if vertex is None:
            return set(self._hedges)
        if vertex in self._vertices:
            return set(self._vertices[vertex])
        raise EntityNotFound(f"Unknown vertex {vertex}")


class CommunicationNetwork(TimeVaryingHypergraph):
    def __init__(self, channels, channel_timings, name=None):
        super().__init__(channels, channel_timings)
        self.name = name

    def channels(self, participant=None):
        return self.hyperedges(participant)

    def participants(self, channel=None):
        return self.vertices(channel)

    @classmethod
    def from_json(cls, file_path, name=None):
        file_path = Path(file_path)
        with file_path.open("rb") as file:
            if file_path.suffix == ".bz2":
                raw_data = json.loads(bz2.decompress(file.read()))
            else:
                raw_data = json.loads(file.read())
            hedges = {
                str(chan_id): set(channel["participants"])
                for chan_id, channel in raw_data.items()
            }
            timings = {
                str(chan_id): datetime.fromisoformat(channel["end"])
                for chan_id, channel in raw_data.items()
            }

        return cls(hedges, timings, name=name)
