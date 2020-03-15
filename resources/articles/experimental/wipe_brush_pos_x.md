Wipe Brush X Position
====
This setting configures where the nozzle moves to when wiping.

The wipe procedure only supports wiping in the X direction. This means that the wiping brush must span the entire Y axis. The wipe will be made directly to the left or right from the point where the nozzle ends up on the layer. The wiping movement itself will also be made solely in the X direction.

Your wiping brush may either be in the negative X direction or in the positive X direction. If the positive X direction is used, you'll most likely need the nozzle to move some ways beyond the edge of the build volume. If the brush is in the negative X direction, this coordinate will most likely need to be negative.

The nozzle will never move beyond this point for the wipe procedure. The wipe itself is made from this point on towards the model. It will not wipe beyond this point.