Scarring
====
When a print has a big flat top side, there is a danger of scars. This is when there is a clearly visible line on the top side of the print, that doesn't belong to the normal pattern. This line mars the otherwise smooth top surface of the print.

![A diagonal scar across the surface](../images/scarring.jpg)

The scars are created by travel moves that cross the top surface. The hot nozzle scrapes over the surface, cutting away some plastic, slightly melting other plastic, and possibly oozing some extra material in the crevices. The scar is purely visual. There is no significant difference in the strength or accuracy of the print. However if a scar is created on the first layer, the scraping could pull your layer loose from the build plate.

Prevention
----
To prevent scars, you need to prevent the nozzle from scraping over the top surface. You can either avoid the top surface horizontally (combing), vertically (hop) or prevent the need for a travel move at all.
* If you set the [Combing Mode](../travel/retraction_combing.md) to "Not in Skin", the nozzle will avoid hitting the skin when making a travel move. When travelling through a model, it is only allowed to travel through the infill and the walls. Since it's not travelling through the skin, you should not get any scars. However if the travel move starts or ends in the skin or when there is no available path without hitting any skin, the travel move will be straight without hitting anything, and preferably retract as well.
* Enable [Z hop](../travel/retraction_hop_enabled.md) to make the nozzle lift up slightly before cruising over the surface. It will keep some distance between the nozzle and the surface, so that the nozzle doesn't scrape. This will prevent the scar as well. If using combing, the nozzle will first attempt avoiding the skin horizontally. If there is no route available, it will retract and then hop.
* Sometimes it is possible to prevent the need for a travel move, or to have a travel move go only through part of the skin that was not yet printed, simply by adjusting the [skin angles](../top_bottom/skin_angles.md). Cura will order the lines to minimise the travel time, but doesn't give a lot of control over this ordering. By rotating the skin lines, or rotating the model, all of the lines fit differently, the printing order will be different and this makes the travel moves different. Now there might not be the need for any travel move any more. This is very much a process of trial-and-error to achieve, though.