from abc import ABC, abstractmethod
import random


class CommsError(Exception):
    """Base class for communication errors."""

    pass


class TemporalInterferenceError(CommsError):
    pass


class LinkTerminatedError(CommsError):
    pass


class DataCorruptedError(CommsError):
    pass


class OutOfRangeError(CommsError):
    pass


class Packet:
    def __init__(self, data, sender, receiver):
        self.data = data
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
        return f"Packet(data='{self.data}', sender='{self.sender}', receiver='{self.receiver}')"


class SpaceEntity(ABC):
    def __init__(self, name, distance_from_earth):
        self.name = name
        self.distance_from_earth = distance_from_earth

    @abstractmethod
    def receive_signal(self, packet: Packet):
        pass


class SpaceNetwork:
    def __init__(self, level=1, noise=0.5):
        self._entities = {}
        self._broken_links = set()
        self.level = level
        self.noise = noise if level >= 2 else 0.0

    def register(self, entity: "SpaceEntity"):
        print(f"[Network] Registering {entity.name}...")
        self._entities[entity.name] = entity

    def get_entity(self, name: str):
        return self._entities.get(name)

    def send(self, packet: Packet):
        source_entity = self.get_entity(packet.sender)
        dest_entity = self.get_entity(packet.receiver)

        # Validate entities exist
        if not source_entity or not dest_entity:
            if not source_entity:
                raise ValueError(f"Sender {packet.sender} not registered.")
            if not dest_entity:
                raise ValueError(f"Receiver {packet.receiver} not registered.")

        # Check for broken link
        link_key = (source_entity.name, dest_entity.name)
        if link_key in self._broken_links:
            raise LinkTerminatedError("Link has been permanently terminated")

        # Check Range
        dist = abs(source_entity.distance_from_earth - dest_entity.distance_from_earth)
        if dist > 150 and self.level > 2:
            raise OutOfRangeError(f"Distance {dist} exceeds max range of 150")

        # Simulate Noise/Errors
        if random.random() < self.noise:
            # Weighted probabilities:
            # TemporalInterferenceError: 30%
            # LinkTerminatedError: 10%
            # DataCorruptedError: 60%
            error_type = random.choices(
                [TemporalInterferenceError, LinkTerminatedError, DataCorruptedError],
                weights=[30, 10, 60],
                k=1,
            )[0]

            if error_type is LinkTerminatedError and self.level > 2:
                self._broken_links.add(link_key)
                raise LinkTerminatedError("Link has been permanently terminated")
            elif error_type is TemporalInterferenceError:
                raise TemporalInterferenceError("Temporary interference, please retry")
            else:
                raise DataCorruptedError("Data corrupted during transmission")

        print(
            f"[Network] Transmitting from {source_entity.name} to {dest_entity.name}..."
        )
        dest_entity.receive_signal(packet)
