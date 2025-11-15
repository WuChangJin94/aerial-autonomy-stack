"""
docker exec simulation-container bash -c " \
  gz topic -t /world/\$WORLD/wind/ -m gz.msgs.Wind \
  -p 'linear_velocity: {x: 0.0 y: 3.0}, enable_wind: true'"                                   
  
# Positive X blows from the West, positive Y blows from the South

docker exec simulation-container bash -c " \
  gz topic -t /world/\$WORLD/wind/ -m gz.msgs.Wind \
  -p 'enable_wind: false'"  
"""

import gz.transport13
