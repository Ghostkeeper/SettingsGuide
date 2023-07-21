Lijnrichting Vulling Supportstructuur
====
Het supportpatroon is meestal zo georiënteerd dat de lijnen loodrecht staan op de meeste dingen die het ondersteund. Dit minimaliseert de afstand die het ondersteunde materiaal moet overbruggen. Met deze instelling kan de oriëntatie van de supportlijnen individueel worden aangepast.

<!--screenshot {
"image_path": "support_infill_angle_0.png",
"modellen": [{"script": "umbrella_square_rounded.scad"}],
"camera_positie": [0, 0, 180],
"instellingen": {
    "support_enable": waar,
    "support_infill_angles": [0]
},
"laag": 160,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_infill_angle_30.png",
"modellen": [{"script": "umbrella_square_rounded.scad"}],
"camera_positie": [0, 0, 180],
"instellingen": {
    "support_enable": waar,
    "support_infill_angles": [30]
},
"laag": 160,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_infill_angles.png",
"modellen": [{"script": "umbrella_square_rounded.scad"}],
"camera_positie": [0, 0, 180],
"instellingen": {
    "support_enable": waar,
    "support_infill_angles": [30, 60]
},
"laag": 160,
"kleuren": 64
}-->
![Een hoek van 0°](../../../articles/images/support_infill_angle_0.png)
![Afwisselend tussen 30° en 60°](../../../articles/images/support_infill_angles.png)

Met deze instelling kunnen meerdere hoeken, gescheiden door komma's, worden ingevoerd. Als er meerdere hoeken worden ingevoerd, wisselt Cura tussen die hoeken in de slices.

Als de [Lijnrichtingen boven-/onderkant](../top_bottom/skin_angles.md) zijn aangepast, is het raadzaam om ook de hoek van de support dienovereenkomstig aan te passen, zodat deze loodrecht blijft op de lijnen van de onderkant van de print . Hierdoor kunnen de onderste lijnen goed op de support rusten en niet tussen de supportlijnen vallen. Dit is vooral belangrijk voor lijnen en zigzag [Patroon Supportstructuur](support_pattern.md) waar er lange rechte lijnen zijn tussen de supportlijnen die geen support bieden.