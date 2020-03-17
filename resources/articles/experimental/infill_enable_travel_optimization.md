Infill Travel Optimization
====
Enabling this setting may slightly reduce the travel time in your print. By shortening the length of the travel moves the print will go slightly faster and the nozzle will also ooze slightly less. However, it will also take more time to slice the model.

Normally Cura optimises the order in which infill lines are drawn rather naively. After each line, Cura will look for the next closest line to draw and draw that. However for some unusual, intricate shapes, the path to that next infill line may be fairly long because the nozzle has to make a detour due to [combing](../travel/retraction_combing.md). Naively, Cura underestimates the distance then and may choose a longer travel move over a shorter one. When this setting is enabled, the distance is calculated precisely so that a better choice may be made.

This setting will usually have little impact on slicing time. However for intricate prints with many small parts (where it is most useful) it may increase the slicing time by orders of magnitude.