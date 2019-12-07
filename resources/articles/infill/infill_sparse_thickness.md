Since the layer height of the infill is not important for visual quality, you can use thicker layers for the infill to reduce the printing time. This setting causes layers of infill to be combined together, as long as there are multiple layers of infill directly above each other. It will then not print any infill on some of the layers, but in the highest of the combined layers it will extrude more material to make up for it.

In layer view, it will look as if the infill lines have become much wider. When actually printed, the infill lines will drop down further instead of spreading out horizontally.

![Infill Layer Thickness is set to three times the layer height](images/infill_sparse_thickness.png)

The infill layer thickness must be a multiple of the ordinary layer height. If it is not, it will be rounded to the closest layer height.

* Be careful with increasing this too much. When switching to and from infill, the flow rate through the nozzle needs to accelerate and decelerate significantly. There is some delay on this, so it'll extrude too little at the beginning of the infill and too much after the end of the infill.
* In the in-between layers, it will still print infill with a lower layer thickness where there is no infill in the layers around it. This can cause small lines of infill to be printed alongside sloping walls.