Versie G-code
====
Hoewel G-code een gestandaardiseerd formaat is voor het verzenden van instructies naar CNC-machines zoals 3D-printers, zijn er nog steeds enkele verschillen in welke G-codes door elke printer worden ondersupportd, wat hun oorspronkelijke status is en soms hoe de opdrachten moeten worden geïnterpreteerd. Met de G-code-smaak kunt u grotendeels specificeren welke reeks opdrachten uw printer accepteert.

Het verschil tussen de verschillende G-code varianten is over het algemeen vrij klein. De hoofdcommando's, zoals het verplaatsen en verwarmen van nozzle, zijn over het algemeen hetzelfde.

Lees de documentatie bij de firmware van uw printer om de juiste G-code-variant te selecteren. Daar moet u leren welke functies worden ondersupportd en welke niet. Dit zijn de beschikbare varianten in Cura en hun verschillen.

Marlijn
----
Marlin wordt beschouwd als de standaard G-codevariant. Het is bedoeld voor de belangrijkste release van [Marlin Firmware](https://marlinfw.org/), de meest populaire 3D-printfirmware en vormt de basis van de meeste alternatieve firmwares die er zijn.

Marlijn (volumetrisch)
----
Dit is een variant van Marlin waarbij de extrusie-opdrachten de extrusiehoeveelheid specificeren in kubieke millimeters in plaats van filamentlengtes. Dit zijn de opvallende wijzigingen:
* De parameter `E` van het `G1`-commando wordt berekend in kubieke millimeters, het volume plastic dat wordt toegevoerd, in plaats van de lengte van het filament dat tijdens die beweging wordt ingevoerd.
* De statistieken aan het begin van de G-code tonen ook het gebruikte filament in kubieke millimeters.

RepRap
----
Dit is een variant gericht op het ondersupporten van printers en is voortgekomen uit het [RepRap-project](https://reprap.org/wiki/RepRap). Ze heeft een aantal opmerkelijke uitzonderingen:
* Vermeld altijd de extruder bij het instellen van de begintemperatuur van de laag, ook als er maar één extruder is.
* Keer terug naar relatieve extrusie na het printen.
* Verander de acceleratie met behulp van de `P` en `T` parameters van de `M204` opdracht, voor respectievelijk druk en verplaatsversnelling, in plaats van de `S` parameter.
* Verander jerk met commando `M566` in plaats van commando `M205`.

Ultimaker 2
----
Deze G-code variant is bedoeld voor de Ultimaker 2 familie. De firmware van deze familie had het vreemde idee dat de printer de materiaalgerelateerde instellingen moest regelen en niet de slicer. Dit zijn de uitzonderingen:
* Er zullen geen printtemperatuurcommando's zijn in de G-code.
* Er zijn geen g-code temperatuuropdrachten voor de platform.
* Er zullen geen commando's voor de temperatuur van het bouwvolume zijn in de G-code.
* Aangenomen wordt dat de eerste nozzle de [printtemperatuur voor de eerste laag](../material/material_print_temperature_layer_0.md) heeft wanneer het printen begint.
* Er wordt aangenomen dat het bouwvel op [Temperatuur eerste laag](../material/material_bed_temperature_layer_0.md) is wanneer het printen begint.
* De parameter 'E' van het commando 'G1' wordt berekend in kubieke millimeters, het volume plastic dat wordt toegevoerd en niet de lengte van het filament dat tijdens die beweging wordt ingevoerd.
* In de statistieken aan het begin van de G-code wordt het gebruikte filament weergegeven in kubieke millimeters.


Griffioenen
----
Dit is de G-code variant voor moderne Ultimaker printers, de Ultimaker 3 en nieuwere modellen. Deze printers hebben een set metadata nodig in een bepaald formaat aan het begin van de G-code. De verschillen in deze G-code variant zijn:
* Aan het begin van de G-code staat een grote header die metadata bevat zoals de duur van de print, de naam van de printopdracht en wat praktische informatie zoals de starttemperatuur en de begrenzingsbox van de print.
* Er zijn geen commando's voor het bouwen van een temperatuur in de G-code.
* Aangenomen wordt dat het eerste nozzle zich bij het begin van het printen op [Eerste laag printtemperatuur](../materiaal/materiaal_print_temperatuur_laag_0.md) bevindt.
* Er wordt aangenomen dat het bouwvel de [temperatuur van de eerste laag van het bouwvel] (../material/material_bed_temperature_layer_0.md) heeft wanneer het printen begint.
* Er wordt niet aangenomen dat de printer start met de eerste extruder, dus aan het begin van het printen met een `T`-commando zal hij altijd overschakelen naar de startende extruder.
* Voor elke extruder wordt bij de eerste printstart een druppel geprint met `G280` in plaats van een streepje.

Mmakerbot
----
Dit is een G-code-smaak die bedoeld is voor op [Sailfish](https://www.sailfishfirmware.com/) gebaseerde firmware. Deze firmware wordt gebruikt in opvolgers van de originele Makerbot-printers. Enkele opvallende verschillen zijn:
* Bij het wijzigen van de printtemperatuur wordt `M109` (temperatuur instellen en onderhouden) niet ondersupportd. In plaats daarvan wordt `M104` uitgevoerd, die niet wacht tot de temperatuur is bereikt. Vervolgens gebruikt het 'M116' om de printer te vertellen dat hij moet wachten tot die temperatuur is bereikt.
* De `E`-afmeting van het `G1`-extrudeercommando wordt niet gereset tijdens het printen. Bij andere varianten wordt deze parameter na elke 10 meter filament gereset met een `G92 E0`-opdracht om afrondingsfouten met drijvende komma in de firmware te voorkomen, maar niet bij deze variant.
* Het wisselen van extruder gebeurt met het `M135`"-commando en niet met het `T`-commando.
* De ventilatorsnelheid wordt niet gerapporteerd. De ventilator is volledig aan of uit. Cura geeft de printer de opdracht om de ventilator aan te zetten wanneer hij anders wil dat de ventilatorsnelheid 50% of meer is.

Bits from bytes
----
Dit is een G-code variant voor de Bits from Bytes printers, die hun eigen firmware hebben. Hun G-code variant verschilt aanzienlijk van andere. De volgende wijzigingen worden door Cura doorgevoerd:
* Extrusiehoeveelheden worden geschreven met de snelheid van de feeder en niet met de parameter `E`.
* Inspringingen worden geschreven met `M101` of `M201`", afhankelijk van de actieve extruder.
* De invoersnelheid wordt gegeven met een apart commando `M108`.
* Rijbewegingen worden gespecificeerd met een `M103`-commando in plaats van `G1` uit te schakelen voor `G0`. Er worden geen `G0`-commando's gegeven.
* De printer is ingesteld om automatisch intrekken te gebruiken met de opdracht `M227`.
* Cura zal nieuwe regels in Windows-stijl uitvoeren, voorafgegaan door een regelterugloop in plaats van alleen een nieuwregelsymbool.
* De `E`-afmeting van het `G1`-extrudeercommando wordt niet gereset tijdens het printen. Bij andere smaken wordt deze parameter na elke 10 meter filament gereset met een `G92 E0`-opdracht om afrondingsfouten met drijvende komma in de firmware te voorkomen, maar niet bij deze.

Mach3
----
Dit is een G-code-smaak die dichter bij de manier blijft waarop CNC-freesmachines G-code verwachten. Er is slechts één opmerkelijk verschil:
* De extrusiehoeveelheden worden geschreven met de parameter `A` van het commando `G1` en niet met de parameter `E`.

Repetier
----
Dit is een G-code variant voor de 3D-printers van Repetier. Het bootst de output van de Repetier-slicer na. Dit zijn de opvallende verschillen in deze g-code variant:
* Wanneer firmware-inspringingen zijn ingeschakeld, gebruiken de inspringingen voor een extruderschakelaar `G10 S1` om aan te geven dat het een inspringing is voor een extruderschakelaar.
* acceleratiewijzigingen worden gemaakt met de commando's 'M201' en 'M202' (om respectievelijk acceleratie en rijversnelling printen) en niet met 'M204'.
* Jerk-wijzigingen worden gemaakt met het commando `M207` en niet met het commando `M205`.

**Omdat dit een apparaatinstelling is, wordt deze normaal gesproken niet vermeld in de normale lijst met instellingen. Er is echter een vervolgkeuzemenu voor deze instelling in het dialoogvenster Printerinstellingen, dat u kunt vinden in de lijst met toegevoegde printers in het dialoogvenster Instellingen.**