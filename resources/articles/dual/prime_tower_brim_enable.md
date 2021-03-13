Prime Tower Brim
====
The prime tower brim is an additional brim, similar to the brim option in the [Build Plate Adhesion Type](../platform_adhesion/adhesion_type.md). This brim can be enabled and disabled separately from the ordinary adhesion. When activated, an additional brim will be printed around the prime tower. This brim is a flat disc around the prime tower of just one layer that improves the adhesion of the prime tower to the build plate.

<!--screenshot {
"image_path": "prime_tower_brim_enable.png",
"models": [
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 0
        }
    },
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 1
        },
        "transformation": ["translateX(40)"]
    }
],
"camera_position": [50, -32, 133],
"camera_lookat": [93, -122, 5],
"settings": {
    "prime_tower_enable": true,
    "prime_tower_brim_enable": true,
    "prime_tower_position_x": 600,
    "prime_tower_position_y": 600,
    "adhesion_type": "skirt"
},
"colour_scheme": "material_colour",
"colours": 32
}-->
![The adhesion is set to skirt, but there is still a brim around the prime tower](../images/prime_tower_brim_enable.png)

Enabling the prime tower brim will give the prime tower more surface area to connect to the build plate. Because the prime tower can get pretty tall and slim, it may topple over for very tall prints. This prime tower brim is meant to prevent that at a small cost of printing time, material and space on the build plate.

The prime tower brim will get the width defined in the [Brim Width](../platform_adhesion/brim_width.md) setting. If the Build Plate Adhesion Type is set to Brim, this setting effectively doubles the width of the brim around the prime tower.

The prime tower brim cannot be combined with a raft.