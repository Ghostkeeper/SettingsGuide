Nozzle ID
====
This is a setting, intended to be specialised by nozzle profiles, that indicates what type of nozzle this is.

The value of this setting is written in the g-code header when using the [Griffin flavour of g-code](machine_gcode_flavor.md). This way the printer knows which nozzle the g-code was meant for, and can warn the user that he might want to switch the nozzle before starting this print.

*Since this is a machine setting, this setting is not normally visible in the settings list.*