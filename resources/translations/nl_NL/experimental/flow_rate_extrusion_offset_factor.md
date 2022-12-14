Doorvoercompensatiefactor
====
Doorvoercompensatiefactor is een experiment dat lijkt op de functie [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) van Marlin. Het doel van doorvoer Balancing is om te compenseren voor onder- en over-extrusie wanneer de doorvoer van materiaal uit de nozzle verandert. Deze instelling configureert de grootte van het effect.

De doorvoerscompensatiefactor beweegt het filament naar voren met elke beweging met de hoeveelheid extra materiaal die nodig is in de volgende seconde. Tussen elke beweging zijn er drie mogelijke scenario's.
* Als de twee aangrenzende verplaatsingscommando's dezelfde doorvoer hebben (omdat hun lijnbreedte, laaghoogte en snelheid hetzelfde zijn), dan zal de voedingssnelheid ook hetzelfde zijn. Het filament wordt in geen enkele richting tussen deze lijnen bewogen.
* Naarmate de doorvoer toeneemt met de volgende regel, blijft het filament naar voren bewegen tijdens de tweede regel. Dit verhoogt de druk in de nozzlekamer, waardoor het materiaal sneller geëxtrudeerd kan worden bij het printen van de lijn en volgende lijnen.
* Als de doorvoer op de volgende regel afneemt, zal het filament tijdens de tweede regel teruggaan. Dit vermindert de druk in de nozzlekamer, waardoor het materiaal vertraagt ​​bij het printen van de tweede lijn en volgende lijnen.

De afstand die het filament aflegt is gelijk aan de hoeveelheid materiaal die per seconde geëxtrudeerd zou worden tijdens de lijn (als de lijn lang genoeg zou zijn om een ​​volle seconde te printen). Met deze instelling kan deze afstand echter worden aangepast. Het verhogen van de factor verhoogt het compensatie-effect. Verlaging ervan zal het compensatie-effect verzwakken. Bij hogere factoren duurt het printen ook langer omdat het filament meer op en neer bewogen moet worden.

Als deze doorvoerompensatie is ingeschakeld, moet de druk in de nozzlekamer beter overeenkomen met de aankomende doorvoer. Dit kan zowel onder- als over-extrusie verminderen en het object nauwkeuriger afmetingen geven.

De compensatie vindt echter plaats tijdens een enkele regel. Dit kan soms een korte lijn zijn waarbij het filament zeer snel moet bewegen. De printkop moet mogelijk vertragen om de feeder bij te kunnen houden, wat resulteert in een klodder. Soms kan het ook een lange lijn zijn, waardoor de kracht van het effect afneemt. Dit maakt de hele extrusiesnelheidscompensatiefunctie onbetrouwbaar en is de reden waarom deze instelling nog steeds experimenteel is.