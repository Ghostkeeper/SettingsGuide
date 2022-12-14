Aantal Lijnen Supportstuk
====
Als de support [Supportstructuur in Stukken Breken](support_skip_some_zags.md) is, bepaalt deze instelling hoeveel supportlijnen in één blok worden gecombineerd.

<!--screenshot {
"image_path": "support_skip_some_zags.png",
"modellen": [{"script": "rack.scad"}],
"camerapositie": [0, 184, 10],
"instellingen": {
    "support_enable": waar,
    "support_pattern": "zigzag",
    "support_skip_some_zags": waar,
    "support_skip_zag_per_mm": 20
},
"kleuren": 32
}-->
![Elk blok bevat 8 regels.](../../../articles/images/support_skip_some_zags.png)

Kleinere blokken zijn meestal gemakkelijker te verwijderen dan grotere blokken. Er is minder oppervlak om aan het model te plakken, dus er is minder kracht nodig om de support te verwijderen. Dus als het verwijderen van support meestal niet moeilijk is, kan het verwijderen van support meer werk zijn. Elk stuk moet dan afzonderlijk worden verwijderd in plaats van de hele support in één groot stuk te verwijderen.

Als de stukjes erg klein zijn, kan de structurele integriteit van de drager in gevaar komen. Het patroon van de support lijkt dan meer op het lijnenpatroon, waardoor de kans op omvallen groter wordt. Dit zou resulteren in meer draden en een slechtere overhangkwaliteit op de punten waar de support omklapt.