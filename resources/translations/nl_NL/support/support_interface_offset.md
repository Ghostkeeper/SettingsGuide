Supportstructuur horizontale uitbreiding
====
Deze instelling zorgt ervoor dat de supportstructuur zich in alle richtingen horizontaal in de rest van de support uitstrekt.

<!--screenshot {
"image_path": "support_interface_offset.png",
"modellen": [{"script": "f.scad"}],
"camerapositie": [45, 45, 133],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_offset": 2,
    "support_interface_offset": 1
},
"kleuren": 64
}-->
![De supportstructuur is uitgebreid met support](../../../articles/images/support_interface_offset.png)

Er zijn twee manieren voor dit mechanisme.
* Als de supportstructuur direct eindigt bij de rand van de overhang die support nodig heeft, kan het materiaal over de rand hangen. Door de structuur iets verder uit te rekken, wordt dit voorkomen.
* Sommige materialen die doorgaans worden gebruikt om support te printen, extruderen slecht bij lage stroomsnelheden of hebben enige tijd nodig om op gang te komen. Kleine delen van de supportstructuur passen niet goed bij deze materialen. Met deze instelling kunnen de gebieden letterlijk worden vergroot, waardoor er meer ruimte is om deze materialen te extruderen.

Vanwege technische beperkingen kan de supportstructuur niet verder worden uitgebreid dan de support zelf.