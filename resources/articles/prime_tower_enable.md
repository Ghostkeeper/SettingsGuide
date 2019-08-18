This prints a tower on your build plate with a mix of materials. The tower is meant to be thrown away, but it serves to prime the material after each extruder switch.

![How a prime tower looks, and the dimensions of it](images/prime_tower.svg)

While other extruders are printing, a nozzle will sometimes ooze some material, leaving the nozzle chamber void of material. Priming the material afterwards is essential, or the material won't flow properly yet at the beginning.

The prime tower consists of an outer shell which is completely printed with one extruder, every layer. This is necessary in order to guarantee stability of the tower, but will sometimes require extra extruder switches for some prints. All other extruders will print loops inside this shell, dumping their material inside the tower, preferably along the walls on the inside. These extruders don't need to prime if they happen to start on the layer, because they will not go in stand-by then.

In addition to priming, the nozzle will also make a movement inside the tower to wipe off any material from the nozzle that accumulated during stand-by. This prevents the ooze from sticking to the print. This is why the prime tower is also sometimes called a *wipe tower*.

The disadvantages of the prime tower are that it takes some extra time to print and takes away some space on the build plate.