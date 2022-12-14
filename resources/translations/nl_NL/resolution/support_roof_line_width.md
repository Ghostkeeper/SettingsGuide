Lijnbreedte Supportdak
====
De breedte van de supprtlijnen van het dak kan afzonderlijk van de breedte van de andere supportlijnen worden geconfigureerd.

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
![De supportdaklijnen zijn breder dan de rest van de supportlines](../../../articles/images/support_roof_line_width.png)

Het printen van het supportdak met iets dunnere lijnen is vaak gunstig voor de kwaliteit van het overhangende oppervlak dat het ondersupportt, omdat het oppervlak gladder is over de structuur van de supportstructuur. Dit verhoogt echter niet noodzakelijkerwijs de hechting tussen het supportoppervlak en het model, dus het supportoppervlak wordt niet noodzakelijk moeilijker te verwijderen.

Het te dun printen van de daklijnen zal echter resulteren in ongelijkmatige extrusie, waardoor de support van het dak afneemt en de kwaliteit van de overhang afneemt. Ook kan er een scherpe verandering zijn in de doorvoer door het nozzle, wat resulteert in over-extrusie bij het beginnen met het printen van het supportdak en onder-extrusie bij het printen van wat na het supportdak komt.