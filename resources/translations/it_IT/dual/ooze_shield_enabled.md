Enable Ooze Shield
====
When printing with multiple extruders, the inactive extruders sometimes still have some material in them. If the nozzles are still hot, this material tends to ooze out. That's the problem that the ooze shield is meant to prevent. The ooze shield is a border around the object that catches any ooze beneath the nozzle.

<!--screenshot {
"image_path": "ooze_shield.png",
"models": [
    {
        "script": "rocket_dual.scad",
        "scad_params": ["extruder=0"],
        "object_settings": {
            "extruder_nr": 0
        },
        "transformation": ["scale(0.5)"]
    },
    {
        "script": "rocket_dual.scad",
        "scad_params": ["extruder=1"],
        "object_settings": {
            "extruder_nr": 1
        },
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [-62, 102, 87],
"settings": {
    "ooze_shield_enabled": true,
    "layer_height": 0.2,
    "line_width": 0.6
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![The ooze shield gets printed with the first extruder of a layer, causing an alternating pattern if printing with two extruders](../images/ooze_shield.png)
![Some parameters can be adjusted for the ooze shield](../images/ooze_shield.svg)

The ooze shield will print up to the height of the highest extruder switch. Above that height, no nozzle will be moved into the print after being on stand-by mode, so printing an ooze shield is unnecessary. The ooze shield will get printed with the extruder that starts on a layer. This extruder will alternate every layer, which is a hazard when working with two different materials that don't stick well to each other. However printing it later, when the other extruder activates, destroys the effect of the ooze shield largely.

The ooze shield is thin enough to break or cut easily, and keeps its distance from your model so that it can be removed without scarring the surface.