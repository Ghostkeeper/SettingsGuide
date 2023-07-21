Onder-extrusie
====
Een van de meest voorkomende problemen met 3D-printen is dat de printer niet genoeg materiaal extrudeert om een mooi, stevig object te produceren. Wanneer dit gebeurt, wordt dit "onder-extrusie" genoemd: nozzle extrudeert minder materiaal dan zou moeten.

![Een extreem geval van onder-extrusie waarbij je zelfs de binnenkant van het object kunt zien](../../../articles/images/underextrusion.jpg)

Onder-extrusie kan zich ook op verschillende manieren manifesteren. In het meest extreme geval is het object erg broos en is het interieur door het oppervlak heen te zien. Soms zijn de lijnbreedtes te klein zodat ze niet aansluiten op de aangrenzende lijnen. Soms zijn het slechts kleine gaatjes in het oppervlak of kleine scheurtjes in de wanden die zichtbaar worden.

Er zijn talloze mogelijke oorzaken van onder-extrusie, waardoor het erg moeilijk is om problemen op te lossen. In de rest van dit artikel worden enkele van de meest waarschijnlijke oorzaken beschreven en hoe u deze kunt verhelpen.

Verstopte nozzle
----
Als uw printer voorheen prima printte en plotseling onderextrudeert zonder veel verandering in het geprinte object of de instellingen, zit het probleem waarschijnlijk ergens in de extrudertrein. In de regel is de zwakste schakel hier de nozzle.

Verstopte nozzles komen bij alle 3D-printers regelmatig voor. Dit kan gebeuren wanneer het filament vervuild is met dingen die niet goed smelten en in nozzle worden geduwd. Het kan ook gebeuren als het filament zelf in nozzle verbrandt. Dit kan gebeuren als het plastic te veel wordt verwarmd of te lang op een hoge temperatuur wordt bewaard. Het materiaal wordt afgebroken, de polymeren kristalliseren, waardoor een stuk hard plastic overblijft dat niet uit nozzle kan worden gesmolten. Om dit te verhelpen, moet u de aanslag uit de nozzle verwijderen.

Er zijn verschillende technieken om de aanslag uit de nozzle te verwijderen. Als u een acupunctuurnaald of een andere dunne metalen naald heeft, kunt u deze van onderaf naar buiten duwen. De meest gebruikelijke techniek is echter wat bekend staat als de "Atomic Pull". Om deze techniek uit te voeren, neem je een stuk filament van minimaal 50 cm lang, bij voorkeur gemaakt van een materiaal met een hoog smeltpunt. Verwarm nozzle tot het smeltpunt van het filament (bijv. 190°C voor PLA) en gebruik een tang om het filament naar binnen te duwen totdat er materiaal uit nozzle komt. Laat nozzle vervolgens afkoelen tot de glasovergangstemperatuur (bijv. 60°C voor PLA) terwijl u het filament in nozzle duwt. Net voordat de glasovergangstemperatuur is bereikt, trek je het filament er snel uit. Als de punt van het filament vuil is met zwartgeblakerd plastic, knipt u de punt af en probeert u het opnieuw totdat deze schoon is. Probeer iets opnieuw printen en hoop dat het nu beter extrudeert.

Doorslippende feeder
----
Soms kan de feeder het filament niet stevig genoeg vastpakken om het hard genoeg door de nozzle te duwen. Tijdens het printen hoor je het filament dan periodiek met een zwakke klik om de paar seconden doorschuiven. Dit is de feeder die het filament naar binnen probeert te duwen, maar de feeder glijdt af en toe door.

De meeste feeders hebben afstelpunten om de kracht te regelen die ze op het filament uitoefenen. Probeer de feeder iets strakker op het filament te laten drukken. Als de feeder te hard op het filament drukt, kan het filament breken of te veel wrijving veroorzaken en gaan slepen. Te weinig druk resulteert vaak in onder-extrusie.

Ongelijke filamentdiameter
----
Hoewel het meeste filament prima is, wordt er soms een batch geproduceerd waarbij het filament iets te dun is. Dit kan een grote impact hebben op de mate van extrusie in uw print. Goedkopere filamenten zijn vaak gevoeliger voor dit probleem. U kunt nonius schuifmaten gebruiken om de werkelijke diameter van uw filament te meten. Zorg ervoor dat u op verschillende punten langs het filament meet en niet waar de feeder het filament heeft geraakd.

Als de diameter van het filament te veel afwijkt (een verschil van 50μm zal zichtbaar zijn in de print), dan kunt u de diameter van het filament aanpassen in de materiaalmanager. Als u materiaal gebruikt dat al in Cura bestaat, moet u dat materiaal dupliceren voordat u het bewerkt. Cura zal dan de nieuwe diameter compenseren door de voedingssnelheid aan te passen.

Materiaal smelten
----
Naast het in topconditie houden van uw 3D-printer, moeten de instellingen waarmee u print ook overeenkomen met de materiaaleigenschappen van het materiaal dat u gebruikt. De belangrijkste instelling is de printtemperatuur.

Als de [Printtemperatuur](../material/material_print_temperature.md) te laag is, zal er zeer snel onder-extrusie optreden. Als het materiaal te koud is, wordt het erg stroperig, waardoor het moeilijk is om goed uit de nozzle te stromen. In combinatie met een hoge printsnelheid heeft het materiaal niet genoeg tijd om goed te smelten en in de juiste positie te vloeien. Sommige materialen, zoals PVA of Nylon, hebben de neiging om vocht uit de lucht op te nemen. Dit vocht verdampt wanneer het materiaal wordt geprint, waardoor het plastic afkoelt. Om dit effect te compenseren, moeten deze materialen bij een hogere temperatuur worden geprint wanneer ze gedurende een bepaalde periode aan lucht worden blootgesteld.

Als de temperatuur te hoog is, kan het materiaal zeer snel ontleden. Afgebroken filament kan dan niet meer goed smelten, waardoor de nozzle verstopt raakt. De extra warmte kan er ook voor zorgen dat het materiaal verderop in de extruderstreng smelt. Dit kan wrijving in de extruderstreng veroorzaken, waardoor het moeilijker wordt om het materiaal naar buiten te duwen. Kijk goed naar de temperatuurclassificatie op uw filamentlabel om te zien in welk temperatuurbereik het kan worden geprint.

In plaats van de temperatuur in te stellen, kun je ook de [Ventilatorsnelheid](../cooling/cool_fan_speed.md) instellen. Als de blower te hoog is ingesteld, kan de nozzle tijdens het extruderen van materiaal sneller afkoelen, waardoor het kouder is dan de temperatuursensor daadwerkelijk aangeeft. Speciaal voor materialen die van nature bij hoge temperaturen worden geprint, zoals: Polycarbonaat, het is vaak nodig om de ventilatorsnelheid te verlagen om onder-extrusie te voorkomen.

Te snel printen leidt ook tot onder-extrusie, omdat er niet genoeg tijd is om het materiaal in de nozzlekamer te laten smelten. Het verlagen van de [Printsnelheid](../speed/speed_print.md) kan ook helpen om onder-extrusie te voorkomen.

Laat het materiaal stromen
----
Er is altijd enige vertraging tussen het materiaal dat door de printer wordt gevoerd en het daadwerkelijk starten van de extrusie. Deze latentie kan leiden tot onder-extrusie als er geen rekening mee wordt gehouden. Terwijl de printer het materiaal voortbeweegt, neemt de druk in de nozzlekamer geleidelijk toe totdat het voldoende is om het gesmolten materiaal aan de andere kant naar buiten te duwen. Het kan tot een seconde duren voordat het materiaal zijn normale doorvoersnelheid heeft bereikt. Als de printer een bowden-buis heeft tussen de invoer en nozzle, kan deze vertraging vele malen groter zijn, bijvoorbeeld 10 seconden of zo.

Als de printer meer materiaal moet extruderen dan voorheen, zal het materiaal sneller worden doorgevoerd, maar het zal even duren voordat het bij de nozzlepunt komt. Ondertussen probeert nozzle een lijn te trekken, maar die lijn is onder-geëxtrudeerd. Vooral wanneer de print zeer gedetailleerd is, kan dit leiden tot aanzienlijke onder-extrusie.

Om dit op te lossen, kunt u twee dingen doen: Voorbereiden en Snelheid aanpassen.

Het materiaal voorbereiden betekent een klein beetje materiaal extruderenn voordat het belangrijke deel van de print begint. Vaak gebeurt dit in een aparte routine aan het begin van de print door een kleine lijn of klodder plastic in een hoek van de platform te printen. Als alternatief kunt u een [Type Hechting aan Platform](../platform_adhesion/adhesion_type.md) gebruiken die een reeks lijnen rond de print zelf printt. Wanneer het materiaal goed stroomt en alle lucht uit de nozzlekamer is ontsnapt, zal het gelijkmatiger extruderen.

Als het materiaal wordt ingetrokken, wordt de materiaaldoorvoer onderbroken. Als het materiaal terug in nozzle wordt geduwd, kan het even duren voordat het weer begint te stromen. Door de [Intreksnelheid(Primen)](../travel/retraction_prime_speed.md) te verlagen, kan het materiaal beter smelten voordat het wordt geëxtrudeerd, wat een beetje helpt. Anders kunt u ook proberen het materiaal iets verder door te voeren dan vóór de intrekking door de [Extra Primehoeveelheid na Intrekken](../travel/retraction_extra_prime_amount.md) aan te passen om de onder-extrusie te compenseren. Deze instelling is echter zeer delicaat.

Balanceren van de filamentdoorvoer
----
Als de onder-extrusie alleen voorkomt in bepaalde structuren van de print, b.v. in de vulling en in de support moet je de nozzle van je print meer aanpassen. Er is altijd een vertraging tussen het toegevoerde materiaal en het daadwerkelijk uitstromen van het materiaal uit de nozzle. Wanneer de printsnelheid voor een deel van de print wordt verhoogd, versnelt de printkop relatief snel, maar blijft de materiaaldoorvoer achter totdat de druk in de nozzlekamer wordt verhoogd om de hogere extrusiesnelheid aan te kunnen. Dit leidt ook tot onder-extrusie. Het vertragen van de extrusiesnelheid resulteert altijd in wat over-extrusie.

Sommige firmwareprogramma's kunnen dit effect compenseren. Marlin heeft een functie genaamd [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) die de druk in de nozzlekamer vooraf verhoogt, waardoor materiaal eerder uit de nozzle kan stromen. Sailfish heeft een [soortgelijke functie](https://www.sailfishfirmware.com/doc/tuning-jkn-advance.html) genaamd JKN Advance. Om de parameters van deze functies in te stellen, moet u de g-code opzoeken in de start-g-code.

Wanneer dergelijke functies niet beschikbaar of niet effectief zijn, moet u ervoor zorgen dat er geen plotselinge, grote doorvoerveranderingen zijn tijdens het printen. Verlaag de [Dikte Vullaag](../infill/infill_sparse_thickness.md) en [Dikte vullaag supportvulling](../support/support_infill_sparse_thickness.md). Met deze instellingen wordt de extrusiesnelheid vermenigvuldigd om een grotere laaghoogte te bereiken.

Wat nog belangrijker is, je zorgt ervoor dat de vulling, binnenwanden, buitenskin en support met een vergelijkbare extrusiesnelheid worden geprint. De extrusiesnelheid van een lijn is het product van lijnbreedte, laaghoogte, stroming en (gemiddelde) snelheid. Vermenigvuldig deze vier factoren met elkaar en zorg ervoor dat het resultaat voor de vulling ongeveer hetzelfde is ([Dikte Vullaag](../infill/infill_sparse_thickness.md), [Lijnbreedte Vulling](../resolution/infill_line_width.md ) , [Doorvoer vulling](../material/infill_material_flow.md) en [Vulsnelheid](../speed/speed_infill.md)), skin ([Lijnbreedte Boven-/Onderkantg](../resolution/skin_line_width.md) , [Doorvoer boven/onder](../material/skin_material_flow.md) en [Snelheid Boven-/Onderkant](../speed/speed_topbottom.md)), Buitenwand ([Lijnbreedte Buitenwand](../resolution/wall_line_width_0.md), [Buitenste wanddoorvoer](../material/wall_0_material_flow.md) en [Snelheid Buitenwand](../speed/speed_wall_0.md)), Binnenwand ([Lijnbreedte Binnenwand(en)](../resolution/wall_line_width_x.md), [Doorvoer binnenwand(en)](../materiaal/wall_x_material_flow.md) en [Snelheid Binnenwand](../speed/speed_wall_x.md)) en Support ([Dikte vullaag supportvulling](../resolution/infill_sparse_thickness.md), [Lijnbreedte Supportstructuur](../resolution/support_line_width.md), [Doorvoer support](../material/support_material_flow.md) en [Snelheid Supportstructuur](../speed/speed_support.md)). Als [Gelijkmatige wandoverlappingen](../shell/travel_compensate_overlapping_walls_enabled.md) is ingeschakeld, zorg er dan voor dat u [Balanceren van de filamentstroom](../speed/speed_equalize_flow_enabled.md)zodat de snelheid wordt aangepast in plaats van de doorvoer.

Limieten voor nozzle
----
Te veel materiaal door een klein nozzle extruderen kan ook leiden tot onder-extrusie. Bij het printen van grote laaghoogtes, lijnbreedtes of snelheden met een kleine nozzle kan het materiaal fysiek niet op tijd uit de nozzle stromen. Door de temperatuur te verhogen kan het materiaal tot op zekere hoogte vloeibaarder worden, maar er zijn nog steeds grenzen waaraan een nozzle kan extruderen. Als deze limiet wordt overschreden, moet u een grotere nozzle kopen.

Anderzijds kan het extruderen van te weinig materiaal ook leiden tot onder-extrusie. Als de druk in de nozzlekamer erg laag is, kan de oppervlaktespanning van de vloeibare kunststof het materiaal in de nozzlekamer vasthouden. Af en toe wordt het er met een grote druppel uitgeperst, waardoor er op andere plaatsen lucht achterblijft. Dit kan resulteren in een effect dat lijkt op onder-extrusie.

Directe instelling van de doorvoer
----
Als al het andere faalt, heeft Cura ook een instelling om de [Doorvoer](../material/material_flow.md) rechtstreeks aan te passen. Deze tijdelijke oplossing kan een onbekende fout ergens in het systeem compenseren.

Het werkt niet als het materiaal fysiek verhindert dat het sneller stroomt (bijvoorbeeld door een verstopte nozzle). In andere gevallen zal het op sommige plaatsen waarschijnlijk leiden tot over-extrusie. Het is echter een gemakkelijke manier om de druk naar behoefte aan te passen.