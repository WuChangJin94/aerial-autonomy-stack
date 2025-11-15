"""
docker exec simulation-container bash -c " \
  gz service -s /world/\$WORLD/control --reqtype gz.msgs.WorldControl --reptype gz.msgs.Boolean \
  --req 'multi_step: 250, pause: true'"                                                       
  
  # Adjust multi_step based on the value of max_step_size in the world's .sdf (defaults: 250 for PX4, 1000 for ArduPilot)
"""

import gz.transport13
from gz.msgs10.world_control_pb2 import WorldControl
from gz.msgs10.boolean_pb2 import Boolean as GzBoolean

# GZ Transport Setup
self.gz_node = gz.transport13.Node()

# Call Gazebo service to step the simulation
req = WorldControl()
req.multi_step = 50
req.pause = True
result, response = self.gz_node.request(
    "/world/default/control",
    req,
    WorldControl,
    GzBoolean,
    1000 # 1 second timeout
)
