Eerste laag Horiontale uitbreiding
====
Deze instelling breidt alleen de eerste laag uit die op de platform (of op het raft) rust. Net als bij [Horizontale uitbreiding](xy_offset.md), breidt een positieve waarde de eerste laag uit, terwijl een negatieve waarde de eerste laag verkleint.

<!--screenshot {
"image_path": "xy_offset_layer_0_original.png",
"modellen": [
    {
        "script": "d1.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"instellingen": {"xy_offset_layer_0": 0},
"kleuren": 16
}-->
<!--screenshot {
"image_path": "xy_offset_layer_0_enabled.png",
"modellen": [
    {
        "script": "d1.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"instellingen": {"xy_offset_layer_0": -0.6},
"kleuren": 16
}-->
![Het originele model](../../../articles/images/xy_offset_layer_0_original.png)
![De eerste laag wordt verkleind.](../../../articles/images/xy_offset_layer_0_enabled.png)

De eerste laag wordt vaak geprint op een verwarmt platform, waardoor deze in een enigszins vloeibare toestand blijft om de hechting aan de platform te verbeteren. De eerste laag is meestal ook veel dikker dan de overige lagen. Hierdoor blijft er genoeg tijd en materiaal over om de laag zijwaarts te laten zakken, waardoor het fenomeen "olifantvoet" ontstaat, waarbij de onderkant van de print een iets bredere rand heeft. Met deze instelling kan de olifantvoet worden gecompenseerd door de eerste laag in de eerste plaats dunner te maken. Geef deze instelling een kleine negatieve waarde om de olifantvoet te compenseren.

U kunt deze instelling ook op een hoge waarde zetten om een pseudo-brim rond uw print te maken die kan worden gecombineerd met andere hechttechnieken zoals het raft. Bedenk dat hierdoor ook de skin wordt uitgerekt, zodat er skin onder de wanden van de tweede laag zit.

**Het combineren van deze instelling met een rand is niet effectief omdat de rand sowieso een grote rand rond de eerste laag vormt.**