from classes.Satlite import Satellite
from space_network_lib import (
    SpaceNetwork,
    Packet,
)

from errors.errors import BrokenConnectionError
from space_utils.space_utils_fns import attempt_transmission

my_space_network = SpaceNetwork(3)

sat1 = Satellite("Sat1", 100)
sat2 = Satellite("Sat2", 200)

my_space_network.register(sat1)
my_space_network.register(sat2)

packet1 = Packet("hi from packet1", "Sat1", "Sat2")

try:
    attempt_transmission(packet1)
except BrokenConnectionError:
    print("Transmission failed")
