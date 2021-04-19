Warping
====
Warping is a problem with the final print where the print curls up after printing, leaving the final object deformed. Typically the corners on the bottom side of the print curl upwards, or thin parts of the print become wavy.

![The tips are curling up](../images/warping.jpg)

Cause
----
Warping is caused by a combination of effects, but primarily by internal stress due to the nozzle pulling on the molten plastic. While it's in the glass transition, plastic behaves a bit like rubber or gum. If you pull on it the material will stretch, but if you stop pulling it will revert to its original shape. The same happens also during printing. When printing a long line, the nozzle pulls on the line of plastic, which stretches in the length of the line. When the nozzle moves away and stops pulling, the plastic line will contract. This contraction causes a pull on everything attached to it. When enough plastic lines pull in unison, they can warp the print. This is especially common when many lines are parallel, such as in the skin.

A second effect that causes warping is shrinkage of the material when it cools down. Most materials tend to shrink when they cool down. If the object cools down non-uniformly, then some parts of the print shrink more than other parts of the print, which warps the object. As the object continues to cool down it solidifies further, locking that deformity in permanently.

Some materials are more susceptible to shrinkage than others. Here are some shrinkage coefficients of common 3D printing materials. This is approximately how much each type of material shrinks when it cools down from its glass transition temperature to room temperature. Some variation will occur between blends. Greater shrinkage will cause more warping.
* PLA: 0.21%
* ABS: 0.70%
* TPU: 0.63%
* HIPS: 0.64%
* PETG and CPE: 0.45%
* Nylon: 0.62%
* PC: 0.70%
* PP: 1.2%

Additionally the warping may be prevented if other material is in the way. If a part of the print is completely dense then the surrounding material may shrink less or not at all. If other parts are not completely dense, you'll end up with a print that is partially shrunk. The shrunk part of the print will pull on the rest, which can also cause warping. This is common at the border between skin and infill, since the skin is completely dense but the infill is not.

Warping is most common at the bottom side of the print. Here the temperature gradient is the biggest, since the bottom side of the print is often heated by a heated bed and the rest of the print is not. The bottom side usually also consists of many long skin lines. If the [bottom pattern](../top_bottom/top_bottom_pattern.md) is set to Lines or Zigzag, these lines are long, straight and parallel, which allows them to pull in unison in the same direction to warp the object.

Prevention
----
* If the warping occurs in the bottom side of the print, set the [bottom pattern for the initial layer](../top_bottom/top_bottom_pattern_0.md) to concentric. This way the contraction of the bottom skin lines will no longer pull in unison. The internal tension will distribute uniformly into the inside of the bottom layer. If this is not enough to prevent warping then you could also set the ordinary [top/bottom pattern](../top_bottom/top_bottom_pattern.md) to Concentric.
* To reduce the temperature gradients inside the print, reduce the [build plate temperature](../material/material_bed_temperature.md). The object should cool down more evenly then.
* Depending on your printer hardware, printing in an enclosed heated chamber can also prevent warping. For one it will reduce the temperature difference between the build volume and the build plate, and the difference between the build volume and the nozzle. It will also allow the plastic to [anneal](https://en.wikipedia.org/wiki/Annealing_%28glass%29) for longer, reducing internal stresses and therefor the pulling of printed lines that causes the warping. If your printer supports it, consider increasing the [build volume temperature](../material/build_volume_temperature.md).
* To prevent the bottom side from warping, good build plate adhesion helps. This increases the force needed for the material to warp. For instance, increase the [brim width](../platform_adhesion/brim_width.md) or [raft width](../platform_adhesion/raft_margin.md).
* Using a [raft instead of a brim](../platform_adhesion/adhesion_type.md) takes the print away from the build plate and places a sturdy piece of plastic in between that is designed to be resistant to warping.
* Try printing with a [draft shield](../experimental/draft_shield_enabled.md). This builds a chamber around your print, which prevents outside drafts from cooling down your print before it's done. However keep in mind that the draft shield itself may also shrink. If the draft shield fails, you could see a lot of stringing or spaghetti in your print.
* Print in a material that shrinks less, such as PLA.
* If you are at liberty to make adjustments to the printed model, try to prevent placing very sharp outer corners on the build plate. You may choose to round off certain outer corners. This prevents all of the force of the internal stress from concentrating in one point, reducing the likelyhood of warping.