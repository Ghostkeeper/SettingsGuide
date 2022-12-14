Laag Hoogte
====
De 3D-printer brengt het plastic in lagen aan. De laaghoogte is de hoogte van deze lagen in millimeters. Het is de belangrijkste factor in zowel de visuele kwaliteit van de uiteindelijke print als de printtijd.

<!--screenshot {
"image_path": "layer_height_0.1.png",
"modellen": [{"script": "plunger_stop.scad"}],
"camerapositie": [25, 100, 50],
"instellingen": {"layer_height": 0.1},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "layer_height_0.3.png",
"modellen": [{"script": "plunger_stop.scad"}],
"camerapositie": [25, 100, 50],
"instellingen": {"layer_height": 0.3},
"kleuren": 32
}-->
![0,1 mm laaghoogte](../../../articles/images/layer_height_0.1.png)
![0.3mm laaghoogte](../../../articles/images/layer_height_0.3.png)

laaghoogte is de belangrijkste instelling die van invloed is op de algehele kwaliteit en, omgekeerd, op de printtijd. Dit zijn slechts enkele van de effecten:
* Dunnere lagen verhogen de visuele kwaliteit van de print. Omdat de lagen dunner zijn, wordt de rafeling aan de randen van de lagen verminderd. Ook liggen de lagen dichter bij elkaar, waardoor de groeven tussen de lagen kleiner zijn, wat resulteert in een globaal gladder resultaat.
* Dunnere lagen zorgen ervoor dat de printer meer details kan creëren aan de boven- en onderkant van de print.
* Dikkere lagen maken de print tot op zekere hoogte stabieler. Er zijn minder randen tussen lagen, wat meestal een zwak punt is. De dikkere lagen schuiven niet zo veel af.
* Dikkere lagen verkorten de printtijd omdat de nozzle minder horizontale bewegingen hoeft te maken.

laaghoogte vs. profielen
----
Veel instellingen zijn afhankelijk van de laaghoogte. Omdat de laaghoogte de doorvoer van het materiaal door de nozzle aanzienlijk beïnvloedt, veranderen veel parameters van het printproces. Dit is erg ingewikkeld. Als je bijvoorbeeld de laaghoogte vergroot, moet je waarschijnlijk ook de printtemperatuur iets verhogen om het extra warmteverlies te compenseren. De temperatuur heeft dan invloed op de vloeibaarheid van het materiaal, wat weer van invloed is op hoe scherp de hoeken zullen zijn en welke koeling nodig is etc. Het is altijd aan te raden om te beginnen met een vooraf ontworpen kwaliteitsprofiel dat beschikbaar is voor uw printer en een laaghoogte die aan uw eisen voldoet.

Met de aangepaste modus kunt u de gewenste laaghoogte kiezen, maar er zijn ook vooraf ontworpen profielen met verschillende laaghoogtes beschikbaar. U kunt kiezen uit profielen voor verschillende laaghoogtes in de aanbevolen modus met een schuifregelaar of in de aangepaste modus met behulp van de vervolgkeuzewidget. Aangezien deze profielen ook enkele parameters wijzigen die afhankelijk zijn van de laaghoogte, krijgt u op deze manier waarschijnlijk een betere kwaliteit.

Extra informatie
----
Met zeer kleine laaghoogtes zou je de grenzen van de resolutie van je Z-as kunnen bereiken. Zoek de toename van de Z-as van uw printer op en zorg ervoor dat de laaghoogte een veelvoud daarvan is. Als dit niet het geval is, zullen sommige lagen dikker zijn dan andere, waardoor strepen ontstaan.

**Merk op dat de instelling van de laaghoogte niet van toepassing is op de eerste laag van de print of op de raftlagen, aangezien deze hun eigen instellingen hebben om de laaghoogte afzonderlijk aan te passen. Bij gebruik van adaptieve lagen wordt deze instelling voor de laaghoogte als basislijn gebruikt, maar de werkelijke laaghoogte kan enigszins variëren.**