Minimum Feedrate
====
The Marlin firmware for 3D printers, from which most printer firmware is derived, has a minimum speed for all of its movements. This setting indicates what that minimum speed is for your printer's firmware.

The minimum speed is an adjustment to prevent errors in the firmware due to divisions by zero. The firmware needs to calculate the time intervals between steps in order to send a signal to the motors with the correct timing. If the motor needs to move with a speed of 0 (i.e. stand still) this would be an infinite time interval, which the firmware can't handle well. This only applies if none of the motors of the printer actually turn though. For example, when moving in the X direction the motor controlling the Y axis still doesn't rotate, but due to the intricacies of stepper motors the minimum feedrate doesn't apply here.

Cura uses this minimum feedrate in order to produce correct time estimates. It is applied when accelerating at the beginning of the print or after a pause, and when decelerating to a standstill at the end of a print or before a pause.

**Since this is a machine setting, this setting is not normally visible in the settings list.**