Support Interface Resolution
====
Cura needs to determine where the support interface is printed by looking above and below the support where it comes into contact with the model. This setting determines the resolution at which it checks.

Increasing this setting causes Cura to sample at a lower resolution, which speeds up slicing. However increasing it too much can cause Cura to skip placing support interface if the model above or below the support is very thin. If the model is very thin, Cura's sampling could skip over the model, not noticing that it should place support interface there. Instead, it will place ordinary support.

It's normally fine to leave this at a couple of layer heights. If you are using sacrificial layers or other single-layer parts, it might result in some inconsistencies in the support interface, but nothing that will seriously affect the print.