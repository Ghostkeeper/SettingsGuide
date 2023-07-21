Coasting Inschakelen
====
Als deze instelling is ingeschakeld, stopt de nozzle met het extruderen van materiaal net voordat een muurcontour wordt gesloten. De gedachte hierachter is dat de nozzlekamer dan op het laatste stukje van de lijn kan leeglopen, waardoor de druk op de nozzle wordt verminderd en deze kan worden geblokkeerd door het begin van de contour. Dit leidt dan tot een kleinere naad aan het begin van de contour en vermindert het uitlopen in de volgende verplaats beweging.

<!--screenshot {
"image_path": "coasting_enable.png",
"modellen": [{"script": "phone_holder.scad"}],
"camerapositie": [0, -215, 117],
"minimum_laag": 1,
"structuren": ["reizen", "helpers", "shell", "infill", "starts"],
"instellingen": {
    "coasting_enable": waar,
    "coasting_volume": 0.06
},
"kleuren": 32
}-->
![In de lagenweergave is de naad goed te zien wanneer Coasting is geactiveerd, omdat er dan een verplaats beweging is](../../../articles/images/coasting_enable.png)

Het activeren van Coasting is bedoeld om de zichtbaarheid van de naad in de wanden te verminderen. Als je meestal grote, dikke naden hebt, kan het inschakelen van deze functie dit effect verminderen. Het is in feite het tegenovergestelde van wat de [Veegafstand buitenwand](../shell/wall_0_wipe_dist.md) doet, dus het is een goed idee om eerst te proberen het afvegen te verminderen voordat je probeert te coasten .

In theorie leidt coasting altijd tot onder-extrusie. Of dit bij het printen zichtbaar is, hangt af van de specifieke omstandigheden. Coasting is meestal iets effectiever op direct drive printers. Als uw printer een directe aandrijving heeft, moet u [Coasting-volume](coasting_volume.md) op een lagere waarde instellen dan bij gebruik van kabels of flexibele aandrijfassen, omdat de respons van de doorvoer veel sneller zal zijn. Ook is het met Bowden-transportsystemen veel moeilijker om de hoeveelheid uitloop te regelen op een manier die de zichtbaarheid van de naad effectief vermindert.