Supportstructuurlijnen verbinden
====
Bij sommige supportpatronen kan de support erg onstabiel worden wanneer dunne stroken support nodig zijn. Deze instelling zorgt ervoor dat de eindpunten van de supportlijnen worden verbonden. Hierdoor heb je meer stabiliteit. Het drukt ook de drager af met een continue doorvoer. Er zijn minder verplaatsingen nodig.

<!--screenshot {
"image_path": "zig_zaggify_support_disabled.png",
"modellen": [{"script": "plug.scad"}],
"camerapositie": [71, 71, 147],
"instellingen": {
    "support_enable": waar,
    "support_pattern": "driehoeken",
    "support_wall_count": 0,
    "support_offset": 0.2,
    "zig_zaggify_support": false
},
"laag": 236,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "zig_zaggify_support_enabled.png",
"modellen": [{"script": "plug.scad"}],
"camerapositie": [71, 71, 147],
"instellingen": {
    "support_enable": waar,
    "support_pattern": "driehoeken",
    "support_wall_count": 0,
    "support_offset": 0.2,
    "zig_zaggify_support": true
},
"laag": 236,
"kleuren": 64
}-->
![Verbroken supportlijnen](../../../articles/images/zig_zaggify_support_disabled.png)
![Verbonden supportlijnen](../../../articles/images/zig_zaggify_support_enabled.png)

Wanneer een supportlijn wordt geprint, wordt er een lijn getrokken langs de rand van het supportgebied naar de volgende lijn in plaats van naar de volgende lijn te gaan. Dit zet het volledige supportpatroon om in een enkele of zeer weinig lijnen. Conversie naar een enkele lijn is niet altijd mogelijk. Het startpunt van deze lijn is willekeurig, dus heel vaak hangen er lijnen in de lucht omdat in de ene laag twee lijnen aan het ene eindpunt kunnen worden verbonden, terwijl ze in de volgende laag aan de andere kant zijn verbonden. Dit maakt de support iets zwakker maar nog steeds stabiel en voorkomt onderbrekingen in de doorvoer. Het gedrag van deze instelling is hetzelfde als voor [Vullijnen verbinden](../infill/zig_zaggify_infill.md).

Het aansluiten van de supportlijnen heeft een aantal voordelen, maar ook enkele nadelen:
* De support is stabieler en kantelt niet gemakkelijk tijdens het printen.
* De doorvoersnelheid wordt constanter gehouden, zodat u de support op hogere snelheid kunt printen zonder doorvoerproblemen. Dit is vooral belangrijk voor moeilijk te extruderen dragermaterialen.
* Wanneer doorvoerintrekkingen worden gemaakt tijdens support, zijn er aanzienlijk minder  doorvoerintrekkingen nodig terwijl de support wordt geprint, waardoor materiaalslijtage wordt voorkomen.
* Er is meer materiaal nodig om de drager printen.
* Het printen van de support duurt meestal langer omdat de verplaatsbewegingen meestal sneller zijn dan het printen van supportlijnen.

Het zigzagpatroon is altijd verbonden (met een iets andere techniek). Deze instelling is niet beschikbaar voor het zigzagpatroon.