This setting expresses the difference in the length of the filament when it's being compressed between the feeder and the nozzle chamber.

If the filament is being pushed out the nozzle, there is a counter-pressure applied by the nozzle itself (due to the smaller nozzle opening) and by the material underneath the nozzle, be it the printed part or the bed. Meanwhile, the feeder is pushing from the other end. This compresses the filament in the length of the path between the feeder and the nozzle, making the filament effectively shorter. As a result, bringing the filament from the feeder to the nozzle tip requires less movement than bringing the filament into a proper printing position.

This setting tells the printer how far the filament needs to be moved to bring the filament to the nozzle, given that it knows how long the track is from the feeder to the nozzle. This may also help to determine how much material needs to be primed in order to bring the nozzle up to a proper pressure for printing.

Materials that compress more easily, such as TPU or Polypropylene, will have a lower factor than stiff materials such as PLA.

**This setting is currently never visible in Cura's interface. It can only be set by the profiles. It is also not used by Cura during slicing. However, printers that understand Cura's material file format may use it to determine how to move the filament around between the feeder and the nozzle.**