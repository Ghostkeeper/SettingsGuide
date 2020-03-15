Maximum Travel Resolution
====
If the model has a very high resolution, Cura will reduce the resolution such that the printer's processor is able to keep up with processing the g-code commands as they are being executed. The maximum resolution of the travel moves can be determined separately from the [maximum resolution](meshfix_maximum_resolution.md) while printing.

Since travel moves are executed significantly faster than printing moves, the print head will go through travel's line segments much faster than other line segments. The CPU would have to process those line segments much faster in order to keep up with the nozzle. This is why the resolution of the travel moves should be lower than the resolution of the slower extrusion moves.

The resolution of the motion during travel moves is often not important for print quality either. Since it's not extruding, there is no surface to become fuzzy or angular. For this reason, reducing the resolution of the travel moves has no significant impact on the print quality.

Most of Cura's travel moves are straight lines. Those are the fastest movements and produce the fewest vibrations. However if Cura is to avoid collisions it tends to follow the surface of the surface it's trying to avoid. The travel move around this surface will then have a similar resolution as the surface it's avoiding. As a result, this setting can only really have an effect if [combing](../travel/retraction_combing.md) is enabled.