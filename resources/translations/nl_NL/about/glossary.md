Glossary
====
Op deze pagina worden enkele branchetermen uitgelegd die door Cura worden gebruikt. Cura is niet altijd de meest consistente als het gaat om het gebruik van terminologie, dus sommige termen zijn synoniemen.

* **Adaptive layers:** Een techniek die de laaghoogte over de print varieert om de zichtbaarheid van de topologie te verminderen en toch redelijk snel te printen.
* **Aliasing:** Een printdefect waarbij de resolutielimiet van de stappenmotoren zichtbaar is aan de buitenkant van de print.
* **Anti-overhang mesh:** Een model dat voorkomt dat er ondersteuning wordt gegenereerd om een overhang te ondersteunen waarmee het model overlapt. Synoniem van "support blocker". 
* **Bead:** Een streng materiaal nadat het is neergezet door de extrudertrein. De term "bead(kraal)" wordt gebruikt in de wetenschap waar het belangrijk is om rekening te houden met de daadwerkelijke vorm van de streng nadat deze is gestold. Vergelijkbaar met "lijn". 
* **Blob:** Een klodder overtollig materiaal aan de buitenkant van de print.
* **Bowden tube:**Een holle, flexibele buis die wordt gebruikt om het filament door de extrudertrein te leiden.
* **Bridging:** Een techniek om overhangende lijnen in de lucht te printen, door rechte lijnen tussen twee rustpunten te spannen. Cura kan de parameters van overbruggingslijnen aanpassen en zal de richting van sommige lijnen aanpassen om bruggen te creëren.
* **Brim:** Een rand van materiaal, bevestigd aan de print, die werkt als een skirt, maar die de print ook beter aan de bouwplaat hecht door meer oppervlakte te bieden waar het materiaal aan kan kleven.
* **Build plate:** Het platform waarop de print wordt geplaatst terwijl deze wordt gemaakt. Sommige platform's worden verwarmd om het materiaal tijdens het printen beter te laten plakken.
* **Build volume:** De 3D-ruimte waar de printer bij kan om materiaal te extruderen.
* **Coasting:** Een techniek waarbij het laatste deel van een extrusiebaan wordt geprint met 0% filament doorvoer, waardoor de nozzle van zijn overdruk wordt ontdaan.
* **Combing:** Een beweging die probeert te voorkomen dat je tijdens het verplaatsen van de nozzle, wanden oversteekt, om te voorkomen dat er een zichtbaar litteken aan de buitenkant van de print ontstaat.
* **Coordinate origin:** De locatie op het platform waar een nozzle zou bewegen als hij de instructie krijgt om naar de coördinaten [0, 0, 0] te gaan.
* **CuraEngine:** Een programma dat Cura gebruikt om het zware werk van het slicen te doen. Converteert 3D-modellen naar g-code.
* **Cutting mesh:** Een model op het platform dat instellingen kan wijzigen voor het deel van het volume dat overlapt met daadwerkelijk afgedrukte modellen. Het model zelf wordt niet geprint, maar knipt stukken uit van andere modellen en kan dan de instellingen of extruder wijzigen waarmee die onderdelen geprint worden.
* **Disallowed area:** Een locatie op het platform waar je geen model mag plaatsen om te printen. Bijvoorbeeld omdat het clips zou raken die het bed naar beneden houden, de primepijler, of omdat uw afdruk hulponderdelen zou hebben die groter dan het bouwvolume zouden zijn.
* **Draft shield (tochtscherm):** Een omhulsel van materiaal dat rond het object wordt geprint en dat de temperatuur rond de print constant houdt.
* **Elephant's foot:** Een print fout waarbij de onderkant van de print is breder is dan gewenst.
* **Extruder:** De feeder, optionele Bowden-buis, warmtezone, hot-end en nozzle samen. Sommige printers hebben meerdere extruders of hebben meer dan één van sommige delen van de extrudertrein. Afkorting van "extrudertrein".
* **Extruder switch:** Gewoonlijk is slechts één van de extruders tegelijkertijd actief. Een extruderschakelaar is wanneer het de actieve extruder van de ene extruder naar de andere verandert.
* **Extruder train:** De feeder, optionele Bowden-buis, warmtezone, hot-end en nozzle samen. Sommige printers hebben meerdere extrudertreinen of hebben meer dan één van sommige delen van de extrudertrein.
* **Extrusion:** De handeling van het doorvoeren van filament door de extrudertrein, zodat er materiaal uit het nozzle komt, dat hopelijk op de juiste plaats wordt afgezet om de print te vormen.
* **Face:** Een plat oppervlak van een 3D-mesh. Met driehoekige mazen (de enige soort die Cura kan verwerken), zijn alle vlakken driehoeken in 3D-ruimte.
* **Fan:** Niet zomaar een ventilator van de printer, maar specifiek de ventilator(en) die aan de printkop zijn bevestigd die de print afkoelen net nadat het materiaal is geëxtrudeerd.
* **FDM printing:** Gefuseerde afzettingsmodellering. Een vorm van 3D-printen waarbij lijnen van plastic in een bepaalde vorm worden geëxtrudeerd. Dit is de enige techniek van 3D-printen die Cura ondersteunt. Synoniem van "FFF-afdrukken".
* **Feeder:** Een motor en tandwielkast die het filament door de extrusietrein duwt of trekt.
* **Feedrate:** De snelheid waarmee filament in de extrudertrein wordt doorgevoerd.
* **FFF printing:** Fabricage van gefuseerde filamenten. Een vorm van 3D-printen waarbij lijnen van plastic in een bepaalde vorm worden geëxtrudeerd. Dit is de enige techniek van 3D-printen die Cura ondersteunt. Synoniem van "FDM-afdrukken".
* **Filament:** Een touw van plastic wordt in de 3D-printer gevoerd. Het komt op spoelen. Als het eenmaal geëxtrudeerd is, is het geen filament meer maar gewoon materiaal.
* **Flow:** De snelheid van extrusie materiaal als verhouding van zijn normale snelheid. Meer dan 100% stroom extrudeert theoretisch meer materiaal dan in het toegewezen volume past. Minder dan 100% stroom extrudeert theoretisch te weinig materiaal.
* **Gantry:** Het mechanische frame dat de printkop rond het bouwvolume beweegt.
* **Gap filling:** Een techniek die door Cura wordt gebruikt om kleine openingen in de afdruk op te vullen met materiaal met behulp van zeer kleine lijnsegmenten.
* **Gradual infill:** Een techniek waarbij de hoeveelheid materiaal wordt verminderd in lagere delen van een volume, maar nog steeds hoog in hogere delen om het materiaal erboven goed te ondersteunen. Deze wordt niet alleen gebruikt voor materiaal maar ook voor ondersteuning.
* **Hardness:** Een maatstaf voor de mate waarin een print bestand is tegen elastische vervorming of perforatie.
* **Heater:** Een verwarmingselement dat het filament op de temperatuur brengt die nodig is voor 3D-printen.
* **Heat zone:** De zone waar het filament opwarmt terwijl het naar de nozzle gaat. Aan het begin van de warmtezone is het filament op kamertemperatuur. Aan het einde is het op printemperatuur.
* **Hop:** Een techniek waarbij de nozzle omhoog wordt bewogen (+Z) om met een beetje speling over de print te bewegen. Synoniem van "Z-hop".
* **Hot end:** Het hete metalen of keramische bit met daarin de nozzle, het verwarmingselement en de temperatuursensor.
* **Infill:** Een structuur aan de binnenkant van een print die de bovenskin omhoog houdt en de print extra stevigheid geeft.
* **Infill mesh:** Vergelijkbaar met "Cutting mesh", maar is alleen van toepassing waar het overlapt met het vul volume van een ander model. Dit is een model dat instellingen aanpast voor vulling van een ander model.
* **Inner walls:** Alle wanden behalve de buitenste wand. Hoewel een onderdeel op een laag slechts één buitenwand heeft, kan het een willekeurig aantal binnenwanden hebben.
* **Inset:** Een bewerking op polygonen die een kleinere/dunnere polygoon produceert, waarvan de contour op een bepaalde afstand blijft van de contour van de originele polygoon. Een inzet met een negatieve afstand wordt een "offset" genoemd.
* **Ironing:** Een techniek waarbij de nozzle nog een keer over het bovenoppervlak gaat om het extra glad te maken.
* **Jerk:** Een limiet op de hoeveelheid onmiddellijke snelheidsverandering die wordt toegepast aan het begin van elke beweging. Dit is niet hetzelfde als de gebruikelijke definitie van "schok" in de natuurkunde!
* **Layer:** 3D-printen gebeurt in dunne laagjes materiaal. Deze lagen zijn 2D-vormen met een bepaalde dikte, die verticaal gestapeld een 3D-print vormen.
* **Layer shift:** Een print fout waarbij de horizontale positie van een laag onbedoeld wordt gewisseld, waardoor meestal ook de rest van de print is verwisseld.
* **Layer split:** Een printfout waarbij de lagen niet goed genoeg aan elkaar plakken en openbarsten.
* **Line:** Een stuk materiaal nadat het door de extrudertrein is neergezet. In Cura worden lijnen gemodelleerd als rechthoekige blokken met een bepaalde breedte, dikte (laaghoogte) en lengte. Vergelijkbaar met "lijn".
* **Line segment:** Om de 3D-printterm "lijn" ondubbelzinnig te maken, zal Cura bij het verwijzen naar een lijnsegment in wiskundige zin altijd de volledige term "lijnsegment" gebruiken om een rechte geometrische lijn van beperkte lengte aan te duiden.
* **Material:** Het materiaal waar je 3D print uit bestaat. Typisch een thermoplast in FFF-afdrukken.
* **Mesh:** Een verzameling driehoeken die samen een model vormen. Hoewel het soms wordt gebruikt als synoniem van "object" en "model", wordt dit meestal gebruikt in de context van een stuk gegevens in plaats van iets dat u zou willen printen.
* **Model:** Een 3D-model geladen in de 3D-scène van Cura (vóór het slicen). Synoniem van "voorwerp".
* **Nozzle:** De opening waar het printmateriaal de extrudertrein verlaat.
* **Object:** Een 3D-model geladen in de 3D-scène van Cura (vóór het slicen). Synoniem van "model".
* **Offset:** Een bewerking op polygonen die een grotere/dikkere polygoon produceert, waarvan de contour op een bepaalde afstand blijft van de contour van de originele polygoon. Een offset met een negatieve afstand wordt een "inzet" genoemd.
* **One-at-a-time mode:** Een manier om meerdere objecten af te drukken waarbij elk object volledig wordt voltooid voordat het doorgaat met het volgende object, terwijl normaal gesproken een laag voor elk object wordt afgedrukt voordat verder wordt gegaan met de volgende laag.
* **Ooze shield:** Een omhulsel van materiaal dat rond de print wordt geprint en dat eventueel uitgesijpeld materiaal opvangt wanneer een beweging de nozzle naar de print beweegt.
* **Oozing:** Materiaal uit de nozzle lekken terwijl dat niet de bedoeling is. Meestal laat dit een sliert materiaal achter langs het verplaats pad.
* **Outer wall:** De buitenste wand. Er is slechts één buitenwand per onderdeel per laag.
* **Overextrusion:** Te veel materiaal in een beperkt volume extruderen, waardoor het materiaal overloopt naar waar het niet hoort te gaan.
* **Overhang:** Een deel van de print dat niet (of niet volledig) wordt ondersteund door materiaal in de onderliggende lagen. Als de overhang te extreem is om goed te printen, is ondersteuning of overbrugging noodzakelijk.
* **Overpressure:** Tijdens het printen wordt de nozzlekamer onder hoge druk gehouden om ervoor te zorgen dat het materiaal consistent wordt geëxtrudeerd.
* **Parking:** De handeling waarbij de print even wordt onderbroken terwijl de nozzle niet in de buurt van de print is, zodat het materiaal kan afkoelen.
* **Part:** Een doorlopende vorm (polygoon) op een enkele laag. Een enkel model kan bij het slicen in meerdere delen op bepaalde lagen worden opgesplitst.
* **Pattern:** Een techniek om een volume te vullen met materiaal, hoewel niet noodzakelijkerwijs met 100% dichtheid. Cura biedt keuze tussen verschillende patronen zoals lijnen, raster, concentrisch, tetraëdrisch, enz.
* **Pillowing:** Een afdrukfout waarbij de bovenskin uitpuilt of uiteenvalt tussen de plekken waar deze op de vullingsijnen eronder rust.
* **Polygon:** Een 2D-vorm of gesloten lus die bestaat uit een reeks punten met daartussen rechte lijnsegmenten.
* **Prime blob:** Een klodder materiaal die aan het begin van een print wordt gemaakt om een extruder te primen.
* **Prime tower:** Een structuur die naast de print wordt gecreëerd en waarmee de printer zijn nozzles op hogere lagen kan primen zonder dat het overtollige materiaal op de zijkant van de daadwerkelijke print terechtkomt. Gebruikt voor prints waarbij meerdere extruders betrokken zijn om een extruder te primen na een tijdje stand-by te hebben gestaan.
* **Priming:** De handeling van het doorvoeren van wat materiaal om ervoor te zorgen dat het filament is uitgelijnd met de punt van het nozzle en dat de nozzlekamer correct is gevuld en onder druk staat. Meestal gedaan aan het begin van een print of na een extruderwissel.
* **Purging:** De handeling van het extruderen van materiaal als afval. Een veelvoorkomende reden voor zuiveren is "primen".
* **Raft:** Een techniek om de hechting van het platform te verbeteren door een stevige plaat onder je print te printen die later wordt weggegooid. De plaat heeft veel oppervlak en is geprint met dikke lijnen die goed plakken en eventuele onregelmatigheden in de vlakheid van de bouwplaat opvangen.
* **Retraction:** De handeling van het gebruik van de feeder om het materiaal in te trekken in de nozzlekamer. Meestal gedaan om tijdelijk te voorkomen dat het materiaal uit het nozzle stroomt om een schone verplaatsbeweging te maken.
* **Ringing:** Een printfout waarbij het oppervlak wiebelt als gevolg van inconsistente extrusie of wiebelen van de nozzle. Gebeurt meestal na het te snel maken van scherpe bochten.
* **Scar:** Een beschadiging aan de buitenkant van de print waar de nozzle het materiaal in het voorbijgaan smolt.
* **Seam:** De locatie waar een gesloten lus begint en stopt. Deze plek is meestal zichtbaar op de uiteindelijke afdruk, dus je wilt hem op een plek plaatsen waar hij niet erg zichtbaar is.
* **Shell:** Zowel de wanden als de skin.
* **Skin:** De boven- en onderkant van de print. Deze worden altijd afgedrukt met een dichtheid van 100%, meestal met het lijnenpatroon. Synoniem van "boven/onder".
* **Skirt:** Een contour die rond de print op de eerste laag is geprint om zowel het materiaal te primen als om de gebruiker te laten zien of de bouwplaat volledig geleveld is.
* **Slicing:** Het proces waarbij een 3D-model wordt omgezet in instructies voor een 3D-printer om het te printen. Binnen de context van CuraEngine wordt dit soms ook gebruikt voor het proces van het maken van doorsneden van het model, wat een van de fasen is van het volledige slicingproces.
* **Spiralise mode:** Een modus om alleen de omtrek van de modellen af te drukken, meestal terwijl de Z-coördinaat geleidelijk door de laag wordt vergroot om de Z-naad te elimineren door het model in één grote spiraal af te drukken. Buiten Cura wordt dit ook wel "vaasmodus" genoemd.
* **Stand-by:** Bij het printen met meerdere extruders is meestal slechts één van de extruders tegelijk actief. De andere extruders staan stand-by.
* **Stitching:** Een onderdeel van het slicen. Het maken van doorsneden van een groep driehoeken resulteert in een aantal lijnsegmenten op elke laag. Stitching combineert die lijnsegmenten tot polygonen en bepaalt wat de binnenkant van de laag is.
* **Strength:** Overkoepelende term die verschillende maten van weerstand tegen beweging aangeeft, waaronder hardheid, stijfheid en taaiheid wanneer verschillende soorten kracht worden uitgeoefend.
* **Stringing:** Wanneerbij verplaats bewegingen er materiaal lekt, ontstaan er dunne strengen materiaal die "stringing" worden genoemd. De strengen strekken zich niet noodzakelijkerwijs helemaal uit over de lengte van een verplaatsing. Een minder extreme vorm hiervan resulteert in "blobs".
* **Support:** Een deel van de print dat na het printen wordt verwijderd, maar nodig was om delen van de print op hun plaats te houden terwijl de print nog bezig was, om te voorkomen dat materiaal naar beneden viel of te veel wiebelde.
* **Support blocker:** Een model dat voorkomt dat er ondersteuning wordt gegenereerd om een overhang te ondersteunen waarmee het model overlapt. Synoniem van "anti-overhang mesh".
* **Support floor:** De onderkant van de steun, gebruikt waar de steun op het model rust. Dit deel van de steun kan optioneel geprint worden met verschillende instellingen. Er is geen ondersteuningsvloer waar de ondersteuning op het platform rust.
* **Support infill:** Het belangrijkste onderdeel van ondersteuning. Als er geen ondersteuningsstructuur is, bestaat de ondersteuning alleen uit ondersteuningsvulling.
* **Support interface:** Het steundak en de vloer, waar het model op de steun rust en waar de steun op het model rust. De onderkant van de ondersteuning waar de ondersteuning op de bouwplaat rust, krijgt geen ondersteuningsstructuur.
* **Support mesh:** Een model dat gevuld wordt met ondersteunende structuur, in plaats van bedrukking zoals een normale bedrukking. Kan worden gebruikt om de vorm van uw steun aan te passen.
* **Support roof:** De bovenzijde van de steun, gebruikt waar het model op de steun rust. Dit deel van de steun kan optioneel geprint worden met verschillende instellingen.
* **Support towers:** Een techniek om zeer dunne of kleine delen van de print te ondersteunen. Het onderdeel wordt ondersteund door de punt van een toren die verder naar beneden breder wordt zodat de steun niet omvalt tijdens het printen.
* **Thermoplastic:** Een soort plastic die zacht wordt bij het smelten. Alleen thermoplasten kunnen worden gebruikt voor FFF-afdrukken.
* **Thickness:** De grootte van een structuur in verticale richting (Z). Vergelijk met "breedte".
* **Top/bottom:** De boven- en onderkant van de print. Deze worden altijd afgedrukt met een dichtheid van 100%, meestal met het lijnenpatroon. Synoniem van "skin".
* **Top surface:** Het hoogste deel van de bovenskin. Zelden meer dan 1 laag, dit bovenoppervlak kan met afzonderlijke instellingen worden bedrukt om een hogere kwaliteit te bereiken zonder veel extra printtijd te kosten.
* **Topography:** Het effect waarbij de beperkte laaghoogte een bijna vlak oppervlak verandert in iets dat lijkt op een geografische hoogtekaart met ringen waar de lagen eindigen.
* **Toughness:** Een maatstaf voor een afdruk in hoeverre deze bestand is tegen plastische vervorming.
* **Transition (of walls):** De plaats waar een verschillend aantal wanden samenkomt om het onderdeel dunner of dikker te maken door in sommige delen een ander aantal wanden te gebruiken dan in andere.
* **Travel (move):** De nozzle van de ene plaats naar de andere verplaatsen zonder materiaal te extruderen.
* **Underextrusion:** Te weinig materiaal extruderen om een volume goed te vullen of om sterke en doorlopende lijnen goed te maken.
* **Underpressure:** In ingetrokken toestand wordt de nozzlekamer op een negatieve druk gehouden om het materiaal naar binnen te zuigen en sijpelen te voorkomen.
* **Vase mode:** Een modus om alleen de omtrek van de modellen af te drukken, meestal terwijl de Z-coördinaat geleidelijk door de laag wordt verhoogd om de Z-naad te elimineren. Cura noemt dit altijd "spiraalvormige modus".
* **Walls:** De zijkanten van de print. Ze staan horizontaal rond het model.
* **Warping:** Kromtrekken van de print na het printen, doordat het materiaal krimpt of door interne spanningen die aan het materiaal trekken terwijl het nog niet gestold is.
* **Width:** De grootte van een structuur in de horizontale richting (X/Y). Vergelijk met "dikte".
* **Winding order:** De volgorde van punten die een polygoon vormen. Met de klok mee of tegen de klok in. In Cura geeft een opwindvolgorde tegen de klok in een positieve vorm aan, terwijl een opwindvolgorde met de klok mee een gat aangeeft. De ingevoerde 3D-modellen moeten driehoeken hebben met een tegen de klok in draaiende volgorde van buitenaf gezien.sp
* **Wiping:** Een techniek om de nozzle met opzet een eerder geprinte structuur te laten kruisen om loshangend sijpelend materiaal van de punt van de nozzle af te vegen, om te voorkomen dat materiaal aan de buitenkant van de print wordt geplaatst.
* **Wire printing:** Een techniek om een model af te drukken door alleen een draadframe rond het model af te drukken. Zeer experimenteel.
* **Z seam:** Een zichtbare plek op de buitenwand waar de nozzle van de ene laag naar de andere ging. Vaak verkeerd gebruikt in plaats van alleen "naad".
* **Z hop:** Een techniek waarbij de nozzle omhoog wordt bewogen (+Z) om met een beetje speling over de print te bewegen. Synoniem van "hop".