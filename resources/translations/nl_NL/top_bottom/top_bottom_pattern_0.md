Eerste laag patroon onderkant 
====
Deze instelling configureert welk patroon wordt gebruikt voor de onderkant van het model waar het direct op de platformof het raft rust. Het patroon voor deze laag wordt afzonderlijk van de rest van de onderstaande lagen geconfigureerd.

<!--screenshot {
"image_path": "top_bottom_pattern_0.gif",
"modellen": [
    {
        "script": "gear_hollow.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [40, -40, 110],
"settings": {"top_bottom_pattern_0": "concentrisch"},
"laag": [1, 2, 3],
"kleuren": 64
}-->

![De eerste laag is geprint met een concentrisch patroon, de rest is een lijnenpatroon.](../../../articles/images/top_bottom_pattern_0.gif)

Het concentrische patroon hecht veel beter aan de platformdan andere patronen, omdat de spanning in de lijnen in alle richtingen wordt verdeeld als ze krimpen. Dit voorkomt kromtrekken en verbetert de printbetrouwbaarheid. Andere patronen trekken slechts in één richting samen.

Bij het printen met een raft heeft het gebruik van het lijnpatroon de neiging om een iets dikker deel te krijgen. De lijnen worden dan ook uitgelijnd om de openingen tussen de raftlijnen goed te overbruggen, waardoor een gladdere onderkant ontstaat.