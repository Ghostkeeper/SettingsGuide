Verzakking
====
Met FFF-printers wordt een lijn van gesmolten plastic getrokken. Deze lijn is zacht en als hij nergens raakt, zakt hij naar beneden. Dit wordt verzakking genoemd.

![Doorhangen in de overhangende delen](../../../articles/images/sagging.jpg)

Doorhangen zorgt ervoor dat overhangende delen er vezelig uitzien. In plaats van het beoogde oppervlak van het model vloeiend te volgen, zal het te laag zijn. In extreme gevallen wordt de onderkant van een model zo gerafeld dat de holle binnenkant van de print te zien is.

Oorzaken
----
Verzakking wordt eigenlijk niet of nauwelijks veroorzaakt door de zwaartekracht. Het wordt voornamelijk veroorzaakt door de kracht van het materiaal dat uit nozzle wordt geduwd. Daarom doet dit fenomeen zich ook voor bij printers die ondersteboven worden geplaatst of in gewichtloosheid printen. De druk die wordt gebruikt om het materiaal te extruderen, duwt het materiaal naar beneden omdat nozzle (meestal) naar beneden wijst.

Normaal gesproken is de druk in de nozzlekamer nodig om het (stroperig) materiaal naar buiten te duwen en het plat te maken tot een brede en vlakke lijn materiaal door tussen nozzle en de vorige laag of platform te knijpen. Als er echter geen materiaal in de vorige laag zat, is er geen tegendruk om de strook plat te maken. In plaats daarvan wordt het te ver naar beneden geduwd.

Overbrugging
----
Een techniek om de kwaliteit van overhangen te verbeteren, is het optimaliseren van de manier waarop de overhangende opening wordt overbrugd. Dit omvat het verminderen van de druk die wordt gebruikt om het materiaal uit nozzle te persen, evenals het proberen de viscositeit van het materiaal te verhogen of het sneller te laten harden. Ook kunnen de geprinte lijnen opnieuw worden uitgelijnd om de afstand waarover de lijnen niet worden ondersteund te verkleinen. Deze technieken samen worden bridging genoemd.

Cura biedt een aantal manieren om de overbrugging te verbeteren. Het biedt zelfs nog meer wanneer [Brug instellingen inschakelen](../experimental/bridge_settings_enabled.md) is ingeschakeld. Als u deze optie activeert, worden er meer instellingen weergegeven en worden de printparameters voor de overbruggingsgebieden standaard aangepast.

Houd bij het configureren van overbrugging om doorzakken te verminderen rekening met de volgende aanpassingen:
* Het verlagen van de [Printtemperatuur](../material/material_print_temperature.md) maakt de thermoplast viskeuzer, waardoor deze minder uitzakt.
* Door de [Laaghoogte](../resolution/layer_height.md) of [Lijnbreedte](../resolution/line_width.md) te verlagen, wordt de druk waarmee het materiaal uit de nozzle wordt geduwd, verlaagd. Dit vermindert niet alleen doorhangen, maar deze lijnen hebben ook een lagere thermische capaciteit, waardoor de ventilatoren op de printkop effectiever kunnen koelen.
* Als u de [Printsnelheid](../speed/speed_print.md) verlaagt, neemt ook de druk af waarmee het materiaal uit de nozzle wordt geduwd. In dit geval wordt de thermische capaciteit niet verminderd, maar blazen de ventilatoren langer op het materiaal, wat ook hun effectiviteit verhoogt en doorzakken vermindert. Als de bridge-instellingen zijn ingeschakeld, kan de printsnelheid van bridges afzonderlijk worden aangepast. Het verlagen van [Snelheid brugwand](../experimental/bridge_wall_speed.md) is effectief om hellende overhangen te verbeteren. Het verlagen van [Snelheid brugskin](../experimental/bridge_skin_speed.md) vermindert doorzakken in volledig horizontale overhanggebieden. Er is ook een variant hiervan die gebruik maakt van de [Snelheid Overhangende Wand](../experimenteel/wall_overhang_speed_factor.md). Deze instelling is ook van kracht wanneer het oppervlak niet perfect horizontaal is, dus een bepaalde overhangende printsnelheid is alleen mogelijk voor schuine wanden.
* [Doorvoer](../material/material_flow.md) reductie is vergelijkbaar met lijnbreedte reductie. Dit vermindert de druk die wordt gebruikt om het materiaal naar buiten te duwen en vermindert de warmtecapaciteit, waardoor het materiaal sneller stolt. Deze instelling kan ook alleen voor de overbruggingsgebieden worden aangepast, afzonderlijk voor de [Doorvoer brugwand](../experimental/bridge_wall_material_flow.md) of de [Doorvoer brugskin](../experimental/bridge_skin_material_flow.md). Het verminderen van de stroming voor grote oppervlakken resulteert echter ook in gaten in het oppervlak en een schokkerig uiterlijk, dus de overhang kan er visueel nog steeds slecht uitzien als dit wordt aangepast. De maatnauwkeurigheid moet echter worden verbeterd.
* Verhoog de [Vventilatorsnelheid](../cooling/cool_fan_speed.md) om de beelden sneller af te koelen. Hierdoor wordt het materiaal sneller hard en gaat het niet doorhangen.
* Print de wanden [Wandvolgorde](../shell/outer_inset_first.md). Hierdoor kan de buitenwand op de aangrenzende binnenwand leunen, waardoor deze niet valt. Dit is het meest effectief met een kleine [Lijnbreedte Buitenwand](../resolution/wall_line_width_0.md).

<!--screenshot {
"image_path": "support_enable.png",
"modellen": [{"script": "pipe_corner.scad"}],
"camerapositie": [77, 197, 40],
"settings": {"support_enable": true},
"kleuren": 64
}-->
Spport
----
![Een draagconstructie ondersupportt het model](../../../articles/images/support_enable.png)

De meest gebruikelijke en betrouwbare manier om overhangende onderdelen te verbeteren, is door ze tijdens het printen te ondersteunen met een draagstructuur. Deze draagstructuur wordt later verwijderd nadat het materiaal is gestold. Printsupport, ongeacht de grootte van het overhangende gebied, is zeer effectief in het voorkomen van doorzakken, maar het vereist extra tijd en materiaal en laat een litteken achter op de plaats waar de support werd geplaatst.

<!--if cura_version >= 4.7-->Cura heeft twee technieken voor het genereren van support gespecificeerd met de instelling [Supportstructuur](../support/support_structure.md). Er is een "normale" methode en een "boom" methode. De normale methode is over het algemeen effectiever in het verminderen van doorzakken, maar resulteert soms in een ongelijke onderkant. De "boomsupport" betekent dat de strengen iets verder maar ook gelijkmatiger doorhangen.<!--endif-->
<!--if cura_version < 4.7:Cura heeft twee technieken om draagvlak te creëren. Er is een standaardmethode die wordt voortgebracht wanneer [Generate Support](../support/support_enable.md) is ingeschakeld. Als alternatief wordt een boomsupportstructuur gegenereerd als [boomsupportstructuur](../experimental/support_tree_enable.md) is geselecteerd. De normale methode is over het algemeen effectiever in het verminderen van doorzakken, maar resulteert soms in een ongelijke onderkant. De "boomsupport" betekent dat de strengen iets verder maar ook gelijkmatiger doorhangen.-->

Cura's supportgeneratie bepaalt automatisch waar support worden geplaatst. In de meeste gevallen werkt dit goed, maar op sommige modellen kan er te weinig of te veel support zijn. Gelukkig biedt Cura ook veel methodes om de plaatsing van de support aan te passen.
* Het aanpassen van de [Overhanghoek supportstructuur](../support/support_angle.md) is de gemakkelijkste manier om te bepalen hoeveel supportmateriaal wordt geplaatst. U moet deze parameter instellen om al uw overhangende gebieden te ondersupporten. Deze instelling bepaalt ook welke gebieden in de voorbereidingsfase rood worden getekend. Door de overhanghoek te verkleinen, wordt er meer support geprint, wat doorhangen in meer delen van de print vermindert, maar ook meer tijd en materiaal kost en meer littekens veroorzaakt.
* U kunt overhangende delen bovenop andere delen verwijderen door de instelling [Plaatsing Supportstructuur](../support/support_type.md) in te stellen op "Bed Touch". Als u in plaats daarvan "Overal" instelt, kunt u slechte overhangen voorkomen.
* Zorg ervoor dat de instelling [Minimumgebied supportstructuur](../support/minimum_support_area.md) geen dunne delen van de support wist.
* Met de tool Support Blocker kun je kubussen in je scene plaatsen om te voorkomen dat daar support wordt gecreëerd. Je kunt deze blokken ook markeren en Cura vertellen om ze printen als support in de instellingen per model. Ze worden vervolgens geprint als een nieuw stuk support. Zo kun je precies aangeven waar je de support moet plaatsen. U kunt zelfs een volledig 3D-model in Cura laden met de exacte vorm van uw support en Cura vertellen om het als support printen via de tool "Per Model Settings".

Zelfs als de overhang wordt ondersteund door een support, kan deze nog een beetje doorzakken. Om de support te verwijderen, wordt een bepaalde [Z-afstand Supportstructuur](../support/support_z_distance.md) gehandhaafd tussen het model en de support. Het model zal tot deze afstand doorzakken voordat de support in werking treedt. Het verkleinen van de Z-afstand vermindert doorzakken (maar maakt de brace moeilijker te verwijderen). Sommige materialen zijn zo ontworpen dat ze gemakkelijker te verwijderen zijn omdat ze niet chemisch kunnen worden gecombineerd met het materiaal of kunnen oplossen. Deze materialen kunnen het zich veroorloven om de z-afstand te verkleinen, waardoor doorhangen verder wordt verminderd, terwijl ze toch in staat zijn om vervolgens de drager te verwijderen. De druk kan ook tussen de supportlijnen doorzakken,

Het model aanpassen
----
De vrijheid hebben om het model dat wordt geprint aan te passen, kan een veel schoner resultaat opleveren dan proberen de uitsteeksels te overbruggen of te ondersupporten. In plaats van het materiaal in de overhangen te laten zakken, ontwerp en oriënteer je je model zodat er geen overhangingen zijn.

<!--screenshot {
"image_path": "support_minimise_overhang.png",
"modellen": [
    {
        "script": "deuvel.scad",
        "transformatie": ["roterenY(127)"]
    }
],
"instellingen": {"support_angle": 55},
"camerapositie": [21, -104, -30],
"laag": -1
}-->
![Deze oriëntatie maakt het mogelijk om het object printen met zeer weinig support](../../../articles/images/support_minimise_overhang.png)

De eenvoudigste truc om dit te bereiken is door het model te draaien. Als uw printer in staat is om hoeken van 45 graden te printen zonder te verzakken, kunt u een model met een verticaal en een horizontaal deel roteren zodat ze twee schuine delen van 45 graden vormen, wat de kwaliteit van de verticale wand iets zal verminderen, maar doorhangen voorkomt in het horizontale deel. Zorg er echter voor dat het contactoppervlak met de platform niet te klein is, anders kan de print loskomen van de platform en beschadigd raken.

Het toevoegen van afschuiningen kan ook helpen het aantal overhangen in het model te verminderen met relatief weinig extra materiaal. Cura biedt een automatische methode om afschuiningen aan uw model toe te voegen via de voorkeur [Overhang Printbaar Maken](../experimental/conical_overhang_enabled.md). Het toevoegen van afschuiningen voegt een supportstructuur toe aan het eigenlijke model. Ze worden dan naadloos in het model geprint, wat er mooier uitziet. Bovendien wordt materiaal bespaard in vergelijking met printsupport, omdat het supportmateriaal de krachten snel overdraagt ​​op de rest van het model. En uiteindelijk zal je object sterker zijn.

Over het algemeen is het bij het ontwerpen van objecten voor 3D-printen het beste om overhangen helemaal te vermijden. Als de geometrie van het object dit niet toelaat, overweeg dan om het model in verschillende delen te verdelen en deze vervolgens samen te stellen.