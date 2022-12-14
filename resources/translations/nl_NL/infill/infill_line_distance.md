Lijnafstand Vulling
====
In plaats van de [Dichtheid vulling](infill_sparse_density.md) als een percentage op te geven, is het ook mogelijk om de vulling-dichtheid te configureren door de afstand tussen aangrenzende opvullijnen op te geven. Een grotere afstand tussen vullijnen resulteert in een algehele lagere vuldichtheid.

De afstand tussen vullijnen is een andere manier om naar deze eigenschap te kijken dan vuldichtheid. De afstand tussen de vullijnen geeft de afstand aan die de lijnen van het betreffende oppervlak moeten afleggen van de ene vullijn naar de volgende. Het verkleinen van de vullijnafstand verkleint dus de overbrugde afstand en verbetert de kwaliteit van de oppervlakken.

![4mm afstand tussen de lijnen, wat een vulling-dichtheid van 20% geeft](../../../articles/images/infill_pattern_grid.png)
![8mm afstand tussen de lijnen, wat een vulling-dichtheid van 10% geeft](../../../articles/images/infill_sparse_density_low.png)

Normaal gesproken wordt de vullijnafstand berekend op basis van de gewenste vuldichtheid, afhankelijk van het geselecteerde vulpatroon en de lijnbreedte. Vullijnafstand heeft prioriteit.

Het verhogen van de opvuldichtheid (door de regelafstand te verkleinen) heeft grote effecten op uw print, namelijk
* Uw print wordt stabieler.
* De bovenkant wordt beter ondersteund, waardoor deze gladder en waterdichter is.
* De pilowing effecten worden verminderd omdat de warmtezakken kleiner zijn.
* Je print heeft meer materiaal nodig en is dus zwaarder.
* Het duurt langer om het printen te voltooien.