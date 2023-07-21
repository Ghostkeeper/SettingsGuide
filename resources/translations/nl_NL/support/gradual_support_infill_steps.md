Geleidelijke supportvulling traptreden
====
Geleidelijke support vermindert de hoeveelheid gebruikt supportmateriaal door de supportdichtheid in de onderste lagen te verlagen. Dit bespaart printtijd en materiaal zonder dat dit ten koste gaat van de kwaliteit van de overhang. Het hoofddoel van de support is het ondersupporten van overhangende gebieden. Deze functie stemt de support alleen voor dat doel af.

Deze instelling specificeert in hoeveel stappen de supportdichtheid wordt verminderd. Bij elke stap wordt de dichtheid van de support gehalveerd. Met bijvoorbeeld een dichtheid van 20% en twee niveaus, is de supportdichtheid in de lagere gebieden respectievelijk 10% en 5%.

<!--screenshot {
"image_path": "gradual_support_infill_step_height_1mm.png",
"modellen": [
    {
        "script": "trap.scad",
        "transformatie": ["roterenY(-90)", "scaleZ(0.5)"]
    }
],
"camerapositie": [49, 91, -38],
"instellingen": {
    "support_enable": waar,
    "support_pattern": "raster",
    "support_wall_count": 0,
    "support_infill_rate": 50,
    "gradual_support_infill_steps": 3,
    "gradual_support_infill_step_height": 1
},
"kleuren": 64
}-->
![De support wordt in 3 stappen teruggebracht naar een lagere dichtheid](../../../articles/images/gradual_support_infill_step_height_1mm.png)

Naarmate u het aantal stappen verhoogt, wordt de dichtheid steeds meer gehalveerd, wat resulteert in een lagere dichtheid. Dit bespaart veel materiaal en printtijd, maar maakt de support zwakker.

Een deel van de support zal in de lucht zweven. In de praktijk lost dit zich echter snel op voor de meeste supportpatronen, aangezien de lagen goed kunnen bouwen, zelfs op verzwakte onderlagen. Het doel van de [Geleidelijke supportvulling hoogte traptreden](gradual_support_infill_step_height.md) is om de lagen voldoende tijd te geven om zichzelf te herstellen voordat de volgende geleidelijke supportvulling wordt aangebracht.

Deze instelling kan het beste worden gecombineerd met ten minste één [Aantal wandlijnen supportstructuur](support_wall_count.md). Dit geeft de supportlijnen iets om aan vast te klampen in plaats van in de lucht te zweven.