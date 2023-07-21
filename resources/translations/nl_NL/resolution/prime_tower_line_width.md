Lijnbreedte primepijler
====
Deze instelling bepaalt de breedte van de lijnen die worden gebruikt om de primepijler te printen.

<!--screenshot {
"image_path": "prime_tower_line_width.png",
"modellen": [
    {"script": "cube.scad"},
    {
        "script": "cube.scad",
        "object_settings": {"extruder_nr": 1},
        "transformatie": ["translateX(40)"]
    }
],
"camerapositie": [475, -419, 131],
"camera_lookat": [475, -465, 20],
"instellingen": {
    "prime_tower_enable": waar,
    "[1]prime_tower_line_width": 0,8
},
"color_scheme": "materiaal_kleur",
"kleuren": 64
}-->
![Het blauwe materiaal heeft een grotere lijndikte dan het gele materiaal](../../../articles/images/prime_tower_line_width.png)

Het kiezen van een dikkere lijndikte zorgt er soms voor dat de primepijler sneller print. Als het volume dat door een contour wordt geëxtrudeerd groot genoeg is, elimineert het vergroten van de lijnbreedte de noodzaak voor nog een ronde. Als de lijnbreedte echter te veel wordt vergroot, kan de primepijler verzwakken omdat er niet genoeg materiaal snel genoeg kan worden geëxtrudeerd.