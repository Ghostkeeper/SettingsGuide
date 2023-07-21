Oppervlaktemodus
====
Normaal gesproken maakt Cura doorsneden van alle driehoeken in je mesh. Deze lijnsegmenten worden samengevoegd om lussen te vormen. Alle lussen die niet gesloten zijn, worden weggegooid.

Deze instelling bepaalt wat er moet gebeuren met deze niet-gesloten lussen. Als de instelling "Normaal" is, worden ze verwijderd. Met de instelling "Oppervlak" worden alle doorsneden als contouren geprint. Wanneer ingesteld op "Beide", worden de gesloten contouren normaal geprint, maar de niet-gesloten contouren worden afzonderlijk geprint als extra wanden.

<!--screenshot {
"image_path": "magic_mesh_surface_mode_normal.png",
"modellen": [{"script": "extra_surface.py"}],
"camerapositie": [66, 129, 124],
"instellingen": {
    "magic_mesh_surface_mode": "normaal"
},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "magic_mesh_surface_mode_surface.png",
"modellen": [{"script": "extra_surface.py"}],
"camerapositie": [66, 129, 124],
"instellingen": {
    "magic_mesh_surface_mode": "oppervlak"
},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "magic_mesh_surface_mode_both.png",
"modellen": [{"script": "extra_surface.py"}],
"camerapositie": [66, 129, 124],
"instellingen": {
    "magic_mesh_surface_mode": "beide"
},
"kleuren": 32
}-->
![Normale modus laat het enkele niet-gesloten oppervlak aan de rechterkant weg](../../../articles/images/magic_mesh_surface_mode_normal.png)
![Surface-modus drukt alleen de oppervlakken af zonder ze als gesloten volumes te behandelen](../../../articles/images/magic_mesh_surface_mode_surface.png)
![Print zowel de volumes als het extra niet-gesloten oppervlak aan de rechterkant](../../../articles/images/magic_mesh_surface_mode_both.png)

De extra vlakken die worden geprint, bevatten alleen de verticale vlakken als enkele lijnen. Er is geen opvultechniek voor horizontale vlakken aangezien de vlakken geen gesloten polygonen zijn. Ze kunnen niet worden gevuld omdat er geen innerlijke werking is. Er mogen geen toppen, bodems, vullingen of supporten zijn. Alleen enkele lijnen.

De extra oppervlakken worden afgedrukt alsof het buitenmuren zijn, dus ze worden beïnvloed door de afdruksnelheid van de buitenmuur, de lijndikte, enzovoort. Het zal deze oppervlakken ook afdrukken met een lijn die precies gecentreerd is op het oppervlak, in plaats van de lijn langs de binnenkant van het model uit te lijnen. Dat betekent dat het zich aan weerszijden van het oppervlak met een halve lijnbreedte uitstrekt. Dit gebeurt omdat het onduidelijk is welke zijde van het oppervlak de binnenkant van het model is. Uw afdruk zal niet maatnauwkeurig zijn. Als, zoals in de schermafbeelding hierboven, het extra oppervlak is uitgelijnd met een normaal, vast oppervlak en je gebruikt de optie "Beide" om eventuele ontbrekende muren te voltooien, dan zullen de lagen niet goed uitgelijnd zijn.

**Als u zowel de normale volumes als de extra oppervlakken print, denk er dan aan dat de volumes worden geprint met de buitenwand volledig binnen het volume. De extra gebieden worden zo geprint dat de lijn gecentreerd is op het gebied en de helft van de breedte van de lijn zich aan elke kant bevindt. Wanneer een extra vlak wordt uitgelijnd op het oppervlak van een gesloten volume, zoals in de bovenstaande figuren, wordt het vlak verschoven met een halve lijnbreedte. Het extra oppervlak heeft immers geen interieur om naar toe te bewegen.**