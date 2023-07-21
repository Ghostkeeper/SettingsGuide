Minimaal Afstandsgebied voor Intrekken
====
Om ervoor te zorgen dat het filament correct wordt verplaatst, moet het feederwiel het filament vastgrijpen. Door het materiaal in te trekken, verslijt het feederwiel vaak het filament tot het punt dat het het filament niet meer goed kan vasthouden. Deze instelling beperkt het aantal feeds binnen een bepaalde lengte van het filament om deze slijtage te voorkomen.

Intrekkingen worden beperkt door de combinatie van [Maximaal Aantal Intrekbewegingen](retraction_count_max.md) en deze instelling. Het materiaal mag niet verder worden teruggetrokken dan de Maximum intrekkingen binnen een filamentlengte die is gespecificeerd door deze instelling van het Minimaal Afstandsgebied voor Intrekken

![Een specifieke filamentlengte waarbij het aantal intrekkingen beperkt is](../../../articles/images/retraction_count_max.svg)

De lengte van het filament waarbij het aantal intrekkingen beperkt is, is een zogenaamd intrek lengte. Bijvoorbeeld bij een filament lengte van 3 mm en een maximaal aantal intrekkingen van 10 betekent dit dat een nieuwe intrekking is toegestaan zodra de 10e vorige intrekking meer dan 3 mm terug op het filament zit.

Door het afstandsgebied te vergroten, wordt het aantal intrekkingen effectief verminderd. Dit maakt de print betrouwbaarder, maar verhoogt de hoeveelheid stringing en klodders op het oppervlak. Dit is vooral handig voor zachtere materialen die gevoeliger zijn voor slijtage.