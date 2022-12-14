Maximaal Aantal intrekbewegingen
====
Het feederwiel moet het filament aangrijpen om het goed te verplaatsen. Door het materiaal in te trekken, verslijt het feederwiel vaak het filament tot het punt dat het het filament niet meer goed kan vasthouden. Deze instelling beperkt het aantal intrekkingen binnen een bepaalde lengte van het filament om dit te voorkomen.

De instelling specificeert het aantal keren dat het filament mag worden ingetrokken tijdens de filamentlengte die is opgegeven in de instelling [Retraction_extrusion_window.md]. Eventuele volgende intrekkingen in deze periode worden niet gedaan, maar gaan gewoon door zonder intrekken.

![Visualisatie van het terugtrekken van het filament over een bepaalde lengte](../../../articles/images/retraction_count_max.svg)

De lengte van het filament waar het aantal intrekkingen beperkt is, is een rekbaar venster. Met een lengte van 3 mm en een maximaal aantal intekkingen van 10 betekent dit dat een nieuwe intrekking is toegestaan ​​zodra de 10e vorige intrekking meer dan 3 mm terug op de filament is.

Door het maximale aantal feeds te verminderen, wordt de slijtage van de filamenten verminderd. Dit is handig voor zachtere materialen zoals PVA. Dit verhoogt echter ook het stringing, omdat het filament niet meer kan worden ingetrokken op een punt waar dit duidelijk gewenst was.