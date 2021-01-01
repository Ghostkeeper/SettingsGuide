Wipe Inactive Nozzle on Prime Tower
====
If this is activated, the printer will wipe off the previous nozzle after priming the next one in the prime tower.

The order of events will be as follows if this is enabled:
1. The printer switches to the new extruder.
2. The new extruder is primed by printing a prime tower.
3. The nozzle that was active before the extruder switch is wiped on the prime tower.
4. The printer continues printing the part with the new extruder.

Note that this makes the printer wipe off the nozzle that was active before the extruder switch, not the currently active nozzle. If your printer has multiple nozzles with a certain distance between them, you might see a travel move in layer view that seems useless. That is because the movement to that location causes the previous nozzle to move over the prime tower (which is not pictured in layer view).

After a nozzle goes on stand-by, it'll still be quite hot for a while. While it is hot, some material tends to ooze out. While priming the next nozzle in the prime tower, it'll have had the chance to cool down a bit so oozing has slowed down. This setting causes the ooze that dribbled out to be wiped off in the middle of the prime tower, so that it doesn't end up on the side of your printed model.