Uitgebreid Hechten
====
Cura moet weten waar het interieur van het model is om het met materiaal te kunnen vullen. Als het oppervlak van uw model niet volledig gesloten is of binnenwanden heeft, kan het onduidelijk zijn waar de binnenkant van het model zich bevindt.

Een veelvoorkomend geval waarin het model incompleet is, is wanneer een extra stuk van het model is bevestigd aan een anders gesloten onderdeel. Dit gebeurt vaak bij het bewerken van meshes met CAD-software die niet is ontworpen voor productie (alleen voor digitale weergave), zoals: Blender of SketchUp. Een voorbeeld hiervan ziet u in de volgende afbeeldingen.

<!--screenshot {
"image_path": "meshfix_extensive_stitching_xray.png",
"modellen": [{"script": "external_attachment.py"}],
"camerapositie": [62, 87, 68],
"laag": -1
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_disabled.png",
"modellen": [{"script": "external_attachment.py"}],
"camerapositie": [62, 87, 68],
"instellingen": {
    "meshfix_extensive_stitching": false
},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_enabled.png",
"modellen": [{"script": "external_attachment.py"}],
"camerapositie": [62, 87, 68],
"instellingen": {
    "meshfix_extensive_stitching": true
},
"kleuren": 32
}-->
![De röntgenfoto toont een extra oppervlak aan de binnenkant](../../../articles/images/meshfix_extensive_stitching_xray.png)
![Als deze instelling uit staat, wordt alleen het volledig gesloten object geprint.](../../../articles/images/meshfix_extensive_stitching_disabled.png)
![Als deze instelling is ingeschakeld, wordt het extra stuk dienovereenkomstig toegevoegd.](../../../articles/images/meshfix_extensive_stitching_enabled.png)

Deze instelling zorgt ervoor dat Cura de gaten in de mesh beter probeert te dichten wanneer deze niet volledig is gesloten. Dit vergroot de kans op een goede print, maar verlengt de snijtijd en kan soms verkeerde oppervlakken aan elkaar hechten