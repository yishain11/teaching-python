from space_network_lib import Packet, SpaceEntity
from classes.Relay import RelayPacket
from space_utils.space_utils_fns import attempt_transmission


class Satellite(SpaceEntity):
    def __init__(self, name, distance_from_earth) -> None:
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet: Packet):
        if isinstance(packet, RelayPacket):
            inner_packet = packet.data
            print(f"Unwrapping and forwarding to {inner_packet.receiver}")
            attempt_transmission(inner_packet)
        else:
            print(f"Final destination reached: {packet.data}")
        return
