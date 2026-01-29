from space_network_lib import Packet, SpaceEntity


class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(packet_to_relay, sender, proxy)

    def __repr__(self):
        return (
            f"RelayPacket(Relaying [{self.data}] to {self.receiver} from {self.sender})"
        )
