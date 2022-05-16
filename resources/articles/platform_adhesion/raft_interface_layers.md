Raft Middle Layers
====
The raft can have any number of middle layers. This setting controls how many middle layers will be printed.

![Where the middle layers are located in the raft](../images/raft_dimensions_simplified.svg)

Having more middle layers takes more time to print, but greatly increases the stiffness of the raft and protects the model from the heat of the build plate more. The same effect can be achieved by increasing the [Raft Top Layers](raft_surface_layers.md). However the top layers are tuned to produce a nice smooth surface, which can take a lot of time to print if there are many layers. The middle layers don't need to be smooth, and so having many of them doesn't have a great impact on the printing time.