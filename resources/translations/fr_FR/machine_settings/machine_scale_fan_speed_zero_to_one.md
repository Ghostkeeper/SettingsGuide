Scale Fan Speed To 0-1
====
To control the speed at which the fans of the printer spin, Cura puts commands in the g-code with a parameter that controls the speed. Normally this parameter is a number between 0 and 255. However some printers accept a number between 0 and 1 as well, and interpret it differently then. This setting causes Cura to write fan speeds as a number between 0 and 1, instead of between 0 and 255.

There are 3 types of behaviours of firmware in various printers on the market.
* Most printers accept fan speeds only as a number between 0 and 255. This setting should be disabled then, or otherwise the fan will never really spin.
* Some printers (particularly RepRapFirmware) accept numbers between 0 and 255, but if it's 1 or lower, interpret it as a number between 0 and 1. This setting should be enabled then, or otherwise there could be a rare case where Cura attempts to set the fan speed to like 0.4% (1 out of 255), but the printer sets it to 100% instead.
* Some printers only accept numbers between 0 and 1. This setting should also be enabled then, or the fan will always be either completely off or completely on.