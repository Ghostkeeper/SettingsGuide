Rimpellen
====
Rimpellen (soms "ghosting" genoemd) is een effect waarbij rimpels verschijnen op verder vlakke oppervlakken in de buurt van kleine details op dat oppervlak. De rimpelingen verschijnen kort nadat de kleine details zijn geprint.

![Rimpelingen op het oppervlak](../../../articles/images/ringing.jpg)

Oorzaken
----
Het rimpellen wordt veroorzaakt door trillingen in uw 3D-printer. Het rimpellen proberen te voorkomen is om deze trilling te verminderen. Ze zijn vooral uitgesproken wanneer de printkop beweegt op een van de resonantiefrequenties van het printerframe.

Duurdere 3D-printers proberen dit fenomeen meestal te voorkomen door een stijver frame te gebruiken dat minder trilt. Ze hebben een sterker portaal met gehard stalen staven en staven of een volledig gesloten frame van zeer stijf materiaal. Dit is echter duur, dus goedkope 3D-printers hebben niet de middelen om rimpellen te voorkomen. Het rimpellen is ook niet zo ernstig bij printers die zijn uitgerust met een Bowden-kabel, aangezien de printkop veel lichter is dan een printkop met directe aandrijving (omdat de zware invoermotor bovenop de printkop rust).

Hoewel het rimpellen horizontaal waarneembaar is, zijn de trillingen niet altijd horizontaal. Het oscilleren van de platvorm ten opzichte van nozzle is ook een zeer belangrijk effect, omdat het plastic wordt geplet en breder wordt naarmate de platvorm dichterbij oscilleert, of dunner naarmate het verder oscilleert.

Hardware-oplossingen
----
Voordat je je print in Cura aanpast, moet je eerst kijken of je je hardware kunt verbeteren om rimpellen te voorkomen. Dit kan resulteren in een algehele verbetering van de printresultaten zonder dat dit ten koste gaat van andere kwaliteiten van de print, zoals sterkte of productiviteit. Hier zijn enkele dingen die u kunt overwegen:
* Voeg dempingselementen toe onder uw printer. U kunt rubberen voetjes gebruiken of de printer gewoon op een blok zacht schuim plaatsen. Dit voorkomt trillingen wanneer de tafel trilt en voorkomt dat de printer ook de tafel trilt. Dit vermindert de feedback van de trillende printer naar de tafel, wat op zijn beurt helpt om hoogfrequente trillingen te verminderen.
* Span de aandrijfriemen van het portaal weer aan. Als deze banden niet strak staan, kan de printkop gaan trillen door de elasticiteit van het rubber.
* Als uw printkop flexibele hulpstukken heeft, b.v. B. een bowdenkabel, deze dient u zo vast te maken dat ze niet meer kunnen wiebelen. Kabelbinders werken goed voor bowdenkabels als er iets is om ze aan te bevestigen.
* Voeg meer bulk toe aan het frame van uw 3D-printer. Dit maakt het frame moeilijker te verplaatsen vanwege de grotere traagheid en het zal moeilijker zijn om het te laten oscilleren.
* Verhoog de stijfheid van het frame van uw 3D-printer met extra beugels of kruisbeugels. Je zou deze kunnen maken van duurzame materialen zoals staal, maar als dat geen optie is, vind je misschien iets in een ijzerhandel dat met minimale aanpassingen past. Je kunt ook overwegen om deze beugels en kruisbeugels in 3D te printen, maar houd er rekening mee dat de meeste kunststoffen niet goed bestand zijn tegen aanhoudende kracht.

De Cura-oplossingen
----
Als de hardware-oplossingen uit den boze zijn, kun je het rimpellen ook verminderen door enkele aanpassingen te doen in de Cura-instellingen.

Aangezien de trillingen worden veroorzaakt door de acceleratie van de printkop, zijn de belangrijkste verbeteringen gericht op het verminderen van deze versnellingen.
* Het verlagen van de maximale [Printsnelheid](../speed/speed_print.md) verkort de duur van de versnellingen.
* Het verlagen van [Printacceleratie](../speed/acceleration_print.md) vermindert direct de acceleratie en vermindert de trillingssterkte.
* In 3D-printen is [Printschok](../speed/jerk_print.md) een technische term voor onmiddellijke snelheidsveranderingen in bochten. Kort gezegd betekent dit dat je oneindig probeert te accelereren om niet in elke bocht te hard te moeten remmen. Dit leidt tot zeer hoge acceleraties gedurende korte tijd in elke bocht. Het verminderen van schokken kan dan ook helpen om trillingen te verminderen. In plaats van een korte, scherpe acceleratie, is de acceleratie langzamer en langer, waardoor hoogfrequente trillingen worden verminderd, maar laagfrequente trillingen toenemen.

Door deze aanpassingen duurt het printproces langer. Maar er zijn andere manieren om het rinkelen te voorkomen, door de soorten bewegingen die het veroorzaken te stoppen:
* Schakel de methode [Vul gaten tussen wanden](../shell/fill_perimeter_gaps.md) uit en druk [Dunne wanden printen](../shell/fill_outline_gaps.md) niet af, aangezien deze methoden soms zeer kleine lijnsegmenten en extra verplaatsingsbewegingen gebruiken. Als er vervolgens een wand wordt geprint, trilt de printer nog een beetje.
* Als uw printer de platvorm op en neer beweegt in plaats van de printkop, moet u [Z-sprong wanneer ingetrokken](../travel/retraction_hop_enabled.md) niet gebruiken. Deze zorgen ervoor dat de platvorm lang nadat de sprong is voltooid op en neer blijft oscilleren.

Je kunt ook de [Wandvolgorde](../shell/outer_inset_first.md) printen. Omdat het printen van de wanden meestal niet zoveel trillingen veroorzaakt als andere onderdelen, kan de printer stoppen met trillen voordat de zo belangrijke buitenwand wordt geprint.

Afhankelijk van de geometrie van uw printportaal worden de trillingen soms in verschillende richtingen anders geabsorbeerd. De printer 45 graden draaien kan ook helpen.