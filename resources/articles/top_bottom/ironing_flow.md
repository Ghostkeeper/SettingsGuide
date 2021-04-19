Ironing Flow
====
Ironing places additional lines into the surface, technically overextruding. This setting controls how much gets extruded in this extra pass. The flow is necessary to fill gaps in the surface.

<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true
},
"colours": 64
}-->
<!--screenshot {
"image_path": "ironing_flow.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true,
    "ironing_flow": 20
},
"colours": 64
}-->
![10% flow](../images/ironing_enabled_enabled.png)
![20% flow](../images/ironing_flow.png)

You should put this setting high enough to keep the pressure on the nozzle. This pressure needs to fill the gaps on the top surface. If you have a very rough top surface (due to pillowing or printing fast) you may need to increase this setting.