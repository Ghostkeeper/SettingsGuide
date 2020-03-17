Enable Acceleration Control
====
This setting causes Cura to take over control over how fast the print head should accelerate. Just like a car, the print head needs to accelerate in order to change its speed. Normally the printer decides by itself how fast the print head should change direction and speed, but if this is enabled, Cura can decide this instead, which allows you to have different acceleration rates for each feature of a print.

![A graph of the speed (V) over time when moving a nozzle back and forth. Acceleration is the slope of the line when it is starting, stopping or changing direction.](../images/velocity_acceleration_jerk.svg)

* Increasing acceleration causes the print head to reach the desired speed sooner. This will make the print faster, especially when printing small parts, but will also cause more vibrations. These vibrations reduce dimensional accuracy and cause ringing.