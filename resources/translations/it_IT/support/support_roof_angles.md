Support Roof Line Directions
====
The support roof is normally oriented to be as perpendicular as possible to the model above it and the support body below. If the orientation of the bottom lines or the support lines has been customised, it is a good idea to customise the orientation of the support roof lines as well. This setting allows you to customise the orientation of the support roof lines.

<!--screenshot {
"image_path": "support_interface_angles_0.png",
"models": [
    {
        "script": "plug.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 36, 92],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_interface_pattern": "lines",
    "support_interface_angles": [0, 90]
},
"layer": 118,
"colours": 128
}-->
<!--screenshot {
"image_path": "support_interface_angles_45.png",
"models": [
    {
        "script": "plug.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 36, 92],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_interface_pattern": "lines",
    "support_interface_angles": [45, 135]
},
"layer": 118,
"colours": 128
}-->
![Both the roof and floor angled at 0° and 90°](../images/support_interface_angles_0.png)
![Both the roof and floor angled at 45° and 135°](../images/support_interface_angles_45.png)

Multiple angles can be filled in for this setting, separated by commas. Cura will alternate these angles across the layers.

The support roof lines will ideally be oriented to be perpendicular to the support lines that they rest on as well as to the model lines that rest on them. Orienting them perpendicularly reduces the distance that these lines have to bridge and thus reduces sagging and improves the quality of overhangs. This is especially important when working with support that isn't completely dense.