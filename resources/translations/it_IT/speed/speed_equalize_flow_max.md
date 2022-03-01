Maximum Speed for Flow Equalization
====
If the [Equalize Filament Flow](speed_equalize_flow_enabled.md) setting is enabled, then the small gap filling technique will adjust its speed such that the flow rate out the nozzle will be equal to the skin, even if the lines are much thinner.

One problem with this is that very thin lines could result in extremely high speeds. Such speeds may not be reachable by the printer, resulting in lost steps and ultimately in a layer shift. This setting puts a maximum on those speeds.

Since small gaps tend to be small by nature, the lines drawn at these high speeds are usually short as well. This means that due to acceleration limits, the nozzle won't be able to reach the high speeds anyway. This setting normally only has an effect on straight mechanical prints where the gap filling technique fills up long straight slits between two walls that are too small for the nozzle to print.