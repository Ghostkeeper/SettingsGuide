Raft Middle Print Acceleration
====
<!--if cura_version<5.0:This setting configures the acceleration rate of the print head while the middle layer of the raft is printed. The acceleration for the base, middle and top layers of the raft can be configured independently.-->
<!--if cura_version>=5.0-->This setting configures the acceleration rate of the print head while the middle layers of the raft are printed. The acceleration for the base, middle and top layers of the raft can be configured independently.<!--endif-->

![Where the middle layer is located in the raft](../images/raft_dimensions_simplified.svg)

Since the raft generally consists of long line segments, increasing acceleration normally has very little impact on printing time. Increasing the acceleration will save a bit of time when going through corners at the end of the lines though.

Increasing the acceleration rate will cause the printer to vibrate more while printing the middle <!--if cura_version<5.0:layer--><!--if cura_version>=5.0-->layers<!--endif--> of the raft. This slightly increases the risk of pulling the raft off of the build plate.