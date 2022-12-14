Olifant voet
====
Soms is de onderkant van de print iets breder dan de rest van de print, waardoor er een rand ontstaat. Dit wordt "olifantenpoot" genoemd omdat het lijkt op de poten van een olifant, waarbij de tenen iets breder zijn dan de rest van het been.

Er zijn verschillende effecten die olifantenvoet worden genoemd en die totaal verschillende oorzaken hebben. Ook deze vragen om totaal andere oplossingen. Dit artikel helpt je de oorzaak te vinden.

![Olifantenvoeten veroorzaakt door de dikte van de skin](../../../articles/images/elephants_foot.jpg)

Brim
----
Soms is deolifantsvoet eigenlijk gewoon een deel van de brim die niet goed is verwijderd. Als je de brim met de hand hebt verwijderd, kun je zien dat de randlijn volledig grenst aan de normale wandlijn en de normale wandlijn direct onder de rest van de wand. Om de brim helemaal te verwijderen kun je het beste met een scherp mes langs de onderkant van je print snijden.

Als het model geen grote bodem heeft, moet u in plaats daarvan [Type Hechting aan Platform](../platform_adhesion/adhesion_type.md) op Skirt instellen. Als dit te veel problemen met de hechting van het bed veroorzaakt, kunt u alternatieve methoden proberen om de hechting te verbeteren, zoals het instellen van de [Eerste laag patroon onderkant](../top_bottom/top_bottom_pattern_0.md) instelling op "Concentric". .

Kromtrekken
----
Waarschijnlijk de meest voorkomende oorzaak van een echte olifantenpoot is kromtrekken. Als het materiaal afkoelt, krimpt het een beetje. Het materiaal van de onderste laag(en) kan soms niet krimpen. Het behoudt zijn oorspronkelijke grootte, maar de lagen erboven krimpen een beetje. Er zijn verschillende redenen waarom de onderste lagen niet kunnen krimpen:
* Het kleeft aan de platvorm die niet krimpt.
* Hij wordt verwarmd door de platvorm, waardoor hij niet krimpt.
* Er zit een buitenskin naast die krimpen tegengaat. (In hogere lagen kan er in plaats daarvan vulling zijn).

Zie [Kromtrekken](warping.md) om het kromtrekken te voorkomen. Specifiek voor dit type kromtrekken zijn er een paar dingen die je kunt proberen:
* Vergroot de [Wwanddikte](../shell/wall_thickness.md) om te voorkomen dat de wanden naast de vulling krimpen.
* Verlaag de [Platformtemperatuur](../material/material_bed_temperature.md) om de eerste laag net zoveel te laten krimpen als de andere lagen. Als de bedtemperatuur erg hoog was, kan het materiaal ook wat doorzakken, waardoor het aan de onderkant breder wordt. Dit effect is meestal klein, maar kan ook worden voorkomen door de platformtemperatuur te verlagen.
* Verhoog de[Bodemdikte](../top_bottom/bottom_thickness.md) om geleidelijk naar een kleiner formaat te gaan. U kunt zelfs overwegen om het model volledig massief te printen (bij voorkeur door de bodemdikte extreem hoog in te stellen) om het verschil in krimp volledig te elimineren.

Afstelling platform
----
Olifantsvoet kan ook worden veroorzaakt doordat de platvorm te dicht bij nozzle zit bij het printen van de eerste laag. Hierdoor wordt de eerste laag te veel geëxtrudeerd en naar buiten geduwd.

Raadpleeg de handleiding van uw 3D-printer om de platvorm aan te passen. De meeste printers hebben stelschroeven in het platform of portaal om het hoogteverschil van de platvorm tijdens de eerste laag aan te passen. Pas de platvorm tijdens het printen aan (bij voorkeur tijdens de brim, skirt of raft) totdat de eerste laag mooi glad is en niet dunner dan de andere lagen.

U kunt de [Doorvoer eerste laag](../material/material_flow_layer_0.md) in Cura ook direct aanpassen om eventuele over-extrusie te compenseren. Als alternatief kan het verkleinen van de [lijnbreedte eerste laag](../resolution/initial_layer_line_width_factor.md) de extrusie voldoende normaliseren om de voet van de olifant te voorkomen.

Vervorming boven de glasovergang
----

Bij zeer kleine prints bestaat de kans dat de vorige laag niet uithardt wanneer de volgende laag erop wordt aangebracht. Het materiaal wordt met aanzienlijke kracht uit nozzle geduwd. Als de vorige laag nog niet is uitgehard, wordt deze laag samengeprint en horizontaal uitgezet. Dit wordt uitgeprint in de vorm van een olifantenpoot. De oplossing voor dit probleem is ervoor te zorgen dat het materiaal is uitgehard tegen de tijd dat de volgende laag erop wordt aangebracht. Probeer de volgende instellingen te wijzigen:

* Verlaag de [Printtemperatuur van de eerste laag](../material/material_print_temperature_layer_0.md) zodat het materiaal minder hoeft af te koelen.
* Verlaag de [Platformtemperatuur voor de eerste laag](../material/material_bed_temperature_layer_0.md) om de eerste laag sneller af te laten koelen door meer warmte af te geven aan de platvorm. Kunststoffen voor 3D-printen zijn ontworpen om zeer snel te stollen op een bepaald temperatuurpunt, de [glasovergangstemperatuur](https://en.wikipedia.org/wiki/Glass_transition#Transition_temperature_Tg). Om kromtrekken te voorkomen, moet je de glasovergangstemperatuur van je filament opzoeken in het datasheet en ervoor zorgen dat de temperatuur van het printbed niet te veel boven deze overgangstemperatuur stijgt.
* Verhoog de [Startsnelheid ventilator](../cooling/cool_fan_speed_0.md) om het materiaal sneller af te koelen. Overweeg ook om de instelling [Normale ventilatorsnelheid op hoogte](../cooling/cool_fan_full_at_height.md) te verhogen om de eerste paar lagen verder te koelen.
* Verlaag de [Snelheid Eerste Laag](../speed/speed_layer_0.md). Hierdoor heeft de eerste laag meer tijd om af te koelen na het printen.
* Verhoog de [Minimale laagtijd](../cooling/cool_min_layer_time.md). Dit is om ervoor te zorgen dat elke laag een bepaalde tijd heeft om af te koelen voordat de volgende laag erop wordt geplaatst, en gebruikt ook de [Maximale Vventilatorsnelheid](../cooling/cool_fan_speed_max.md). Dit maakt het gemakkelijker om de bovenstaande aanpassingen voor de initiële snelheid van de laag en de ventilatorsnelheid te combineren. Houd er echter rekening mee dat dit geldt voor de hele print, niet alleen voor de eerste laag.

Algemene oplossingen
----
Hier zijn een paar oplossingen die u kunt proberen om van elk type olifantenpoot af te komen, ongeacht de oorzaak:
* Door een [Raft (Type Hechting aan Platform)](../platform_adhesion/adhesion_type.md) te gebruiken, wordt alle druk van de platvorm weggenomen, waardoor de door de platvorm veroorzaakte effecten zoals de temperatuur en te sterke hechting aan de platvorm worden geëlimineerd, en ook de noodzaak voor een brim wordt geëlimineerd. dus vermeden.
* Verminder de [Eerste laag Horizontale uitbreiding](../shell/xy_offset_layer_0.md) (mogelijk tot een negatieve waarde). Dit compenseert de olifantenvoet in de eerste laag.