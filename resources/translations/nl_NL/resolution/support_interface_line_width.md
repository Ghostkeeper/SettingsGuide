Lijnbreedte supportstructuur
====
De breedtes van de supportstructuurlijnen kunnen afzonderlijk van de breedtes van de overige supportlijnen worden geconfigureerd.

<!--screenshot {
"image_path": "support_roof_line_width.png",
"modellen": [
    {
        "script": "trash_bin_lid.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [-47, 79, 110],
"instellingen": {
    "support_enable": waar,
    "support_roof_enable": waar,
    "support_roof_line_width": 0,8
},
"laag": 192,
"kleuren": 64
}-->
![De supportstructuurlijnen zijn breder dan de rest van de supportijnen](../../../articles/images/support_roof_line_width.png)

Het printen van de supportstructuur met iets dunnere lijnen is vaak gunstig voor de kwaliteit van het overhangende oppervlak dat deze ondersupportt, omdat het oppervlak boven de supportstructuur gladder is. Dit verhoogt echter niet noodzakelijkerwijs de hechting tussen de supportstructuur en het model, dus de support wordt niet noodzakelijk moeilijker te verwijderen.

Evenzo hecht de supportvloer gelijkmatiger, waardoor de plekken waar de support op het model rust, worden verminderd zonder de support te verzwakken.

Als de structuurlijnen echter te dun worden geprint, zal er ongelijkmatige extrusie optreden, waardoor de support van de structuur wordt verminderd, wat resulteert in een slechtere overhangkwaliteit en een minder stabiele supportstructuur. Ook kan er een grote verandering zijn in de doorvoer door het nozzle, wat resulteert in over-extrusie bij het starten van het printen van de supportstructuur en onder-extrusie bij het printen van wat na de supportstructuur komt.