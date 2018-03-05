#author: Vasileios Kotronis
#place this script under ~/pyretic/pyretic/examples

from pyretic.lib.corelib import *
from pyretic.lib.std import *

def dumb_forwarder(port1,port2):
    from_1_to_2 = match(inport=port1)
    from_2_to_1 = match(inport=port2)
    return (from_1_to_2 >> fwd(port2)) + (from_2_to_1 >> fwd(port1))
