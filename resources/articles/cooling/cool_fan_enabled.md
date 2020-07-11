Enable Print Cooling
====
This setting will enable or disable the fans on the print head during printing. The fans are meant to cool down the material while it is printing, so that it solidifies faster.

Materials with a low glass transition temperature range, such as PLA, will need to be cooled down while printing. The fans help to do this by blowing cooler air from the environment onto the hot material that just exited the nozzle. Otherwise it will start to [sag](../troubleshooting/sagging.md) from the heat, which causes deformities and may even fail the print completely. In places where the material is hanging in mid-air, such as where there is an overhang, there is nothing to stop the sagging so there it is critical that the material is cooled immediately.

For materials with a higher glass transition temperature range, such as ABS, it is still recommended to turn on the fans, but they may spin at a lower rate for certain parts of the print. Most printers allow precise control over the fan speed, so it's not just an on/off toggle. You can usually control the precise [fan speed](cool_fan_speed.md).

Only for materials with a very high glass transition temperature should you completely disable the fans. If the fans are enabled then, it could give extrusion problems and make the final print brittle.