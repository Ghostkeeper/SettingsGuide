Final Printing Temperature
====
Just before switching to a different extruder, the nozzle will be allowed to cool down slightly to the Final Printing Temperature. In effect, this causes the nozzle to cool down slightly earlier before the extruder has completed printing. It will start cooling down at such a moment that the nozzle is expected to reach the Final Printing Temperature is reached exactly when the extruder switch happens. After that, it will continue cooling down towards the stand-by temperature.

![The moment to start cooling down (precool) is calculated such that the nozzle can cool down to the Final Printing Temperature when the nozzle switch happens](../images/temperature_regulation.svg)

If the Final Print Temperature temperature is slightly lower than the normal printing temperature, the nozzle won't ooze as much while waiting in stand-by while the other extruder is printing.