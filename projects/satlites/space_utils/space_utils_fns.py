from space_network_lib import (
    Packet,
    TemporalInterferenceError,
    DataCorruptedError,
    LinkTerminatedError,
    OutOfRangeError,
    SpaceNetwork,
)

from errors.errors import BrokenConnectionError

from time import sleep


def attempt_transmission(p: Packet):
    sent_flag = False

    while not sent_flag:
        try:
            print("sending msg...")
            sn.send(p)
            sent_flag = True
        except TemporalInterferenceError:
            print("Interference, waiting...")
            sleep(2)
        except DataCorruptedError:
            print("Data corrupted, retrying")
        except (LinkTerminatedError, OutOfRangeError) as e:
            msg = ""
            if isinstance(e, DataCorruptedError):
                msg = "Link lost"
            elif isinstance(e, OutOfRangeError):
                msg = "Target out of range"
            print(msg)
            raise BrokenConnectionError(msg)

    print("message sent successfully")
