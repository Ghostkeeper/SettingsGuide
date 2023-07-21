Vullijnen verbinden
====
Deze instelling verbindt de eindpunten van het opvulpatroon, waar de opvulling de binnenwand of skin raakt, met een lijn die de rand van het opvulgebied volgt.

![Geen verbonden vulling](../../../articles/images/infill_pattern_grid.png)
![Aaneengesloten opvullijnen](../../../articles/images/zig_zaggify_infill_enabled.png)

Hiermee wordt het volledige vulpatroon omgezet in een enkele of zeer weinig lijnen. Conversie naar een enkele lijn is niet altijd mogelijk. Het beginpunt van deze lijn is willekeurig, dus het kan zijn dat het niet voor elke laag hetzelfde is, vooral als de vorm waarin de vulling zich bevindt van laag tot laag verschilt.

Het samenvoegen van de vulling heeft een aantal voordelen, maar ook enkele nadelen:
*Uw onderdeel wordt sterker omdat het praktisch een halve omtrek meer heeft.
* Door het grotere oppervlak hecht de vulling beter aan de wanden, waardoor het onderdeel ook stabieler is.
* De doorvoer wordt constanter gehouden, zodat u de vulling op hogere snelheid kunt printen zonder stroomproblemen. Dit is vooral belangrijk voor materialen die moeilijk te extruderen zijn.
* Tijdens het printen van de vulling vindt er beduidend minder toevoer plaats, waardoor het materiaal niet wordt weggeslepen.
* Het effect van de instelling [Overlappingspercentage vullingl](infill_overlap.md) wordt vergroot, aangezien meer van de infill-lijnen de wanden zullen overlappen.
* Er is meer materiaal nodig om de vulling printen.
* Het printen van de vulling kost doorgaans meer tijd, aangezien de routes doorgaans sneller zijn dan het printen van de vullingslijnen.
* De vulling heeft de neiging om meer door de wanden te schijnen omdat het in een groter deel van de wanden wordt geduwd.