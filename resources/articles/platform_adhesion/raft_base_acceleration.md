Raft Base Print Acceleration
====
This setting configures the acceleration rate of the print head while the base layer of the raft is printed. The acceleration for the base, middle and top layers of the raft can be configured independently.

![Where the base layer is located in the raft](../images/raft_dimensions_simplified.svg)

Since the raft generally consists of long line segments, increasing acceleration normally has very little impact on printing time. Increasing the acceleration will save a bit of time when going through corners at the end of the lines though.

Increasing the acceleration rate will cause the printer to vibrate more while printing the base layer of the raft. This slightly increases the risk of pulling the raft off of the build plate.