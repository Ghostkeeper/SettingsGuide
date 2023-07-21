Stringing
====
Wanneer de printer klaar is met het printen van een deel van een laag en moet overschakelen naar een ander deel, moet hij tijdelijk stoppen met extruderen. Als het materiaal tijdens het transport blijft vloeien, wordt er een dunne kunststof draad tussen de twee delen getrokken. Dit wordt stringing genoemd.

![Er zijn dunne lijnen plastic zichtbaar waar de nozzle van het ene onderdeel naar het andere is verplaatst.](../../../articles/images/stringing.jpg)

Vaak worden de strengen op elkaar gestapeld omdat de nozzle in elke laag een onderdeel op dezelfde plaats afwerkt. Hierdoor ontstaat een verticale vlecht. Het extra plastic kan ook een back-up maken van het stringing van de vorige lagen, wat resulteert in lelijke klodders die overal verspreid zijn.

Stringing gaat soms hand in hand met onder-extrusie. De slicer gaat er doorgaans van uit dat er geen materiaal verloren gaat tijdens traverse bewegingen, dus instrueert hij de printer om net genoeg materiaal te extruderen om het volgende deel te printen. Als er materiaal uit de nozzle komt tijdens een beweging (met als gevolg een streng), wordt dat materiaal niet gebruikt bij het printen van het volgende deel, waardoor er sprake is van onder-extrusie. stringing is meestal geen probleem als het zich voordoet binnen de vulling, maar als het stringing te extreem is, kan het daar ook een probleem veroorzaken, wat leidt tot onder-extrusie achteraf.

Oorzaken
----
Stringing treedt op omdat materiaal de nozzle verlaat tijdens een bewegingsbeweging. Hoewel de printer tijdens een beweging geen nieuw materiaal doorvoert, stopt de materiaalstroom niet direct. Tijdens het printen is er een bepaalde druk in de nozzlekamer, die wordt veroorzaakt doordat het filament een bepaalde kracht opbouwt als een veer. Terwijl nozzle door de lucht beweegt, kan deze druk wegvloeien, waardoor het materiaal onbedoeld uit nozzle wordt geperst.

Zelfs als het materiaal vóór de verplaatsbeweging wordt teruggetrokken, is er nog wat materiaal in de nozzlekamer. Dit komt omdat het materiaal in de nozzle is gesmolten. Door het van één kant terug te trekken, wordt het filament niet teruggetrokken. Totdat het stolt, blijft er een druppel gesmolten materiaal in de nozzle. Tijdens een verplaatsbeweging komt deze druppel uit de nozzle als deze voldoende vloeibaar is.

Preventie
----
Intrekken is de belangrijkste techniek om stringing te voorkomen. Als u merkt dat uw printen vastlopen, kunt u het volgende proberen:
* Zorg ervoor dat [Intrekken Ingeschakelen](../travel/retraction_enable.md). Dit kost weliswaar extra printtijd, maar vermindert het stringing aanzienlijk.
* Verlaag de [Printtemperatuur](../material/material_print_temperature.md). Hierdoor wordt het materiaal minder vloeibaar en loopt het dus minder uit de nozzle. Bovendien wordt een effectievere toevoer mogelijk gemaakt naarmate er meer materiaal uit de nozzlekamer wordt getrokken.
* In het algemeen geldt dat als uw materiaal stroperig is, het verhogen van [Intreksnelheig](../travel/retraction_speed.md) de stringing bij korte bewegingen vermindert door een negatieve druk uit te oefenen op de nozzlekamer. Deze onderdruk zorgt ervoor dat het materiaal wordt aangezogen en niet uitloopt.
* Voor lange verplaatsingen zorgt het vergroten van de [Intrekafstand](../travel/retraction_amount.md) ervoor dat het materiaal op een koelere locatie blijft terwijl de verplaatsing wordt uitgevoerd, waardoor de snelheid waarmee het materiaal smelt en de nozzle verlaat, wordt verminderd.
* Soms probeert Cura filamentslijtage te voorkomen door het aantal feeds over een bepaalde lengte filament te beperken. Omdat er dan geen intrekkingen zijn, is stringing een noodzakelijk kwaad in plaats van een printfout. Als uw feeder het materiaal niet te veel sleept, kunt u het [Maximum Aantal Intrekbewegingen](../travel/retraction_count_max.md) verhogen of de [Minimaal Afstandsgebied voor Intrekken](../travel/retraction_extrusion_window.md) , waarlangs deze intrekkingen worden geteld.
* Als u [Combing-modus](../travel/retraction_combing.md) op meerdere plaatsen toestaat, gaat de nozzle door de binnenkant van het model, niet door de buitenkant. Dit voorkomt het stringing niet echt, maar maakt het onzichtbaar door het in het model te plaatsen.
* Als u [Printvolgorde van wanden optimaliseren](../shell/optimize_wall_printing_order.md) gebruikt, beweegt de nozzle minder vaak heen en weer tussen onderdelen, wat stringing vermindert.
* In het algemeen, als u de [Bewegingssnelheid](../speed/speed_travel.md) verhoogt, worden de draden dunner voor langere verplaatsingsbewegingen. Voor korte verplaatsingen maakt dit echter niet veel uit, omdat de acceleratiesimieten van de printers ervoor zorgen dat de nozzle deze snelheden toch niet haalt.
* Printen met een kleinere nozzle vermindert meestal ook het stringing. Het plastic kan gemakkelijker ontsnappen uit een grotere nozzle.