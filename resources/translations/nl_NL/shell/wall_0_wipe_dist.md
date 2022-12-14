Veegafstand buitenwand
====
Bij deze instelling zal het de nozzle aan het einde van elke buitenwand iets verder gaan zonder te extruderen, waardoor de contour wordt afgesloten.
<!--screenshot {
"image_path": "wall_0_wipe_dist.png",
"modellen": [
    {
        "script": "thin_cylinder.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 0, 50],
"instellingen": {
    "wall_0_wipe_dist": 4
},
"structuren": ["reizen", "helpers", "shell", "infill", "starts"],
"minimum_laag": 2,
"laag": 2,
"kleuren": 16
}-->
![De nozzle een kleine stukje verder na voltooiing van de buitenwand.](../../../articles/images/wall_0_wipe_dist.png)

Het doel van deze functie is om de zichtbaarheid van de naad te verminderen. Als de wand klaar is, zal er meestal nog een druppel onder de nozzle zijn. Dit kleine spoor verbindt deze druppel met het begin van de contour zodat de naad wordt gesloten.

De naad is nog steeds zichtbaar, maar het resultaat zou iets beter moeten zijn met een kleine veegafstand. Als u deze instelling te veel verhoogt, heeft dit geen effect meer, omdat nozzle over de naad heen schiet, wat later kan leiden tot onder-extrusie als de nozzlekamer leeg raakt door te sijpelen op de buitenwand.

Dit effect is in feite het tegenovergestelde van [Coasting inschakelen](../experimental/coasting_enable.md), dat stopt met extruderen net voor het einde van de contour.