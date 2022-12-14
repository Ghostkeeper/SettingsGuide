Topografie
====
Het "topografie"-effect wordt gecreëerd wanneer een schuine boven- of onderkant wordt geprint met een klein aantal lagen, zodat de grenzen tussen de lagen ver uit elkaar liggen en gemakkelijk te zien zijn. Het is genoemd naar [topografische kaarten](https://en.wikipedia.org/wiki/Topographic_maps), waar hoogteverschillen meestal worden aangegeven door hoogtelijnen.

![Je kunt de randen van de lagen duidelijk zien](../../../articles/images/topography.jpg)

Dit effect is alomtegenwoordig bij 3D-printen en is een van de gemakkelijkste manieren om te zien dat een object in 3D is geprint. Hoewel het kan worden voorkomen, vermindert het meestal de productiviteit aanzienlijk.

Laaghoogte
----
Aangezien het topografische effect optreedt wanneer de grenzen tussen lagen erg ver uit elkaar liggen, kan het verminderen van de [Laaghoogte](../resolution/layer_height.md) het effect voorkomen. Naarmate de laaghoogte wordt verminderd, resulteren de kleinere verticale afstanden tussen lagen ook in kleinere horizontale stappen, waardoor het topografische effect wordt verminderd. Het verminderen van de laaghoogte verhoogt echter de printtijd aanzienlijk.

In plaats van de laaghoogte voor de hele print te verlagen, kunt u ook de laaghoogte voor alleen de platte randen van de print verminderen met [Adaptive lagen gebruiken](../experimental/adaptive_layer_height_enabled.md). Dit vermindert het topografische effect aanzienlijk, terwijl de printtijd slechts minimaal wordt beïnvloed. Het is dan echter moeilijker om de druk af te stemmen op andere kwaliteiten, omdat de afstemming meestal afhangt van de laaghoogte.

Modelaanpassingen
----
U kunt ook overwegen het model te draaien, zodat er geen platte schuinte in de print zit. Dit betekent echter meestal dat u veel meer support voor uw model moet printen, wat ook de productiviteit vermindert, en de overhangen zien er misschien niet zo goed uit.