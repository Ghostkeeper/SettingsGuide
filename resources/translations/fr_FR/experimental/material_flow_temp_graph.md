When printing faster, it's best to print at a slightly higher temperature. This makes the thermoplastic more fluid, allowing it to flow more quickly out of the nozzle opening. When [Auto Temperature](material_flow_dependent_temperature.md) is enabled, this setting specifies for each flow rate at which temperature the material should be printed. The flow rate is then averaged for each layer to determine a temperature for that layer.

The flow rate is calculated in cubic millimetres per second, averaged for an entire layer. The temperature is in degrees Celsius. The value of this setting must be a comma-separated list of coordinates. Each coordinate is of the form `[<flow>, <temperature>]`.

The aim of this setting is to achieve a better print quality, reducing overextrusion and underextrusion, if there are big flow changes within a print. A common case for this is the border between skin and infill. Because skin is normally printed much slower than the infill, the layers where there is a lot of infill should be printed at a slightly higher temperature so that the material can properly be extruded during the printing of that infill.

For many printers, the PID regulator that regulates temperatures in the printer's nozzle tends to overreact when there are many temperature changes in a short amount of time. This can cause the printing temperature to be wildly inaccurate when this setting is used.

**This setting is currently not visible in Cura's interface and cannot be activated.**