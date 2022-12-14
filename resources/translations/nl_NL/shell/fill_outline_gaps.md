Dunne wanden printen
====
Normaal gesproken laat Cura wanden weg die dunner zijn dan de [Lijnbreedte Buitenwand](../resolution/wall_line_width_0.md) en negeert ze ze als te klein om printen.

Als deze instelling is ingeschakeld, zal Cura nog steeds proberen deze onderdelen af ​​te printen. De resulterende print zal onnauwkeurig en rommelig zijn, maar zou de gewenste vorm met enige mate van betrouwbaarheid moeten produceren.

<!--screenshot {
"image_path": "fill_outline_gaps_disabled.png",
"modellen": [{"script": "label.scad"}],
"camerapositie": [0, 30, 80],
"settings": {"fill_outline_gaps": false},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "fill_outline_gaps_enabled.png",
"modellen": [{"script": "label.scad"}],
"camerapositie": [0, 30, 80],
"settings": {"fill_outline_gaps": true},
"kleuren": 64
}-->
![Sommige delen zijn te dun om printen](../../../articles/images/fill_outline_gaps_disabled.png)
![Als deze instelling is ingeschakeld, worden ook dunne delen geprint.](../../../articles/images/fill_outline_gaps_enabled.png)

De kleine stukjes zijn gevuld met extreem dunne lijnen. Deze lijnen worden dan gecombineerd als ze naast elkaar en niet te lang zijn. Dit werkt in veel gevallen, maar in sommige gevallen zal er een kleine zigzag zijn, waardoor de printtijd aanzienlijk toeneemt.

Probeer, voordat u naar deze instelling gaat, de breedte van de buitenwandlijnen een beetje aan te passen. Als uw onderdeel iets dunner is dan een lijnbreedte, verkleint u de lijnbreedte van de buitenwand van de hele print zodat de dunne delen normaal een beter resultaat kunnen geven. Als u de lijnbreedte echter te veel verkleint, zal het materiaal onbetrouwbaar vloeien, wat resulteert in onder-extrusie.

**Hiermee wordt alleen geprobeerd delen af ​​te printen die dun zijn in het horizontale vlak. Voor dunne delen in z-richting zie de instelling [Slicetolerantie](../experimental/slicing_tolerance.md) of verhoog de slice-hoogte.**