Always Write Active Tool
====
This setting indicates how certain g-code commands with a tool parameter get interpreted by the printer. Some g-code commands can include a parameter to indicate which extruder it applies to. Some firmware interprets this parameter as a command to switch to that tool and then execute the g-code, while some firmware interprets this parameter as a command to make the g-code apply to a different extruder than the currently active one.

The only commands this applies to that are relevant to 3D printing are the nozzle heating commands, `M104` and `M109`. Take the following example of a heating command, executed while the first extruder (`T0`) is printing:

`M104 S210 T1`

There are two possible interpretations of this command:
* While continuing to print on the first extruder, start heating the second extruder to 210°C. This is the interpretation held by Marlin, Reprap, Sailfish and their derived firmware packages.
* First switch to the second extruder, then heat the second extruder to 210°C. This is the interpretation held by Smoothieware and its derived firmware.

Due to the temperature regulation strategy of Cura, it never needs to execute the second interpretation. If the printer interprets the g-code command in the second way, Cura will write the following g-code instead:

`M104 S210 T1`

`T0`

Essentially, it knows that the printer will switch to the second extruder due to that command, and so it must switch back to the first extruder to continue printing there.

**Since this is a machine setting, it will not normally be listed in the normal list of settings.**