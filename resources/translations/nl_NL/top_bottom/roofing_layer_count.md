Bovenste skinlagen
====
Een deel van het bovenste deel van de print kan worden gescheiden en geprint met verschillende instellingen. Deze instelling bepaalt de grootte van het gebied dat wordt gescheiden. Voor hoeveel lagen van het bovenste deel van de print worden aparte aanpassingen gemaakt?

<!--screenshot {
"image_path": "roofing_layer_count.png",
"modellen": [
    {
        "script": "question_stick_clip.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, -90, 60],
"instellingen": {
    "wall_line_count": 0,
    "skin_outline_count": 0,
    "roofing_layer_count": 1,
    "speed_roofing": 10,
    "cool_min_layer_time": 1,
    "roofing_extruder_nr": 1
},
"color_scheme": "snelheid",
"kleuren": 32
}-->

![De bovenste laag van de skin wordt langzamer geprint (blauw) dan de rest van de skin (groen)](../../../articles/images/roofing_layer_count.png)

Sommige instellingen kunnen de kwaliteit van de bovenkant van de print aanzienlijk verbeteren, maar ze kunnen ervoor zorgen dat de print veel langer duurt omdat ze op alle skinlagen worden aangebracht. Een soortgelijk effect kan worden bereikt als deze instellingen alleen voor de bovenste laag of twee lagen worden gemaakt, maar de overige lagen van de skin worden sneller geprint. Dit heeft dan niet zo'n grote negatieve invloed op de printtijd.

Voor de bovenkant zijn de volgende instellingen mogelijk:
* [Extruder bovenskin](roofing_extruder_nr.md)
* [Bovenste oppervlak skindoorvoer](../material/roofing_material_flow.md)
* [Snelheid Bovenskin](../speed/speed_roofing.md)
* [Acceleratie bovenskin](../speed/acceleration_roofing.md)
* [Schok bovenskin](../speed/jerk_roofing.md)
* [Lijnbreedte bovenskin](../experimental/roofing_line_width.md)
* [Patroon bovenskin](../experimental/roofing_pattern.md)
* [Lijnrichting bovenskin](../experimental/roofing_angles.md)

Om een ​​mooier oppervlak te krijgen, probeer de snelheid te verminderen en de schok te vergroten.

Bij het printen van de skin in een andere kleur (met behulp van de [Extruder bovenskin](roofing_extruder_nr.md) instelling), is het vaak nodig om meer dan één laag in de andere kleur printen. Anders zou de originele kleur nog doorschijnen.