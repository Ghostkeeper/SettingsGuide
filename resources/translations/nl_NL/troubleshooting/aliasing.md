Aliasing
====
Stappenmotoren draaien in vaste stappen. Uw vermogen om te rusten in een positie tussen deze stappen is beperkt. De stapgrootte van de motoren stelt een limiet aan de resolutie die de printer kan bereiken. Bij het printen van wanden die bijna, maar niet helemaal, zijn uitgelijnd met de X- of Y-as, wordt deze resolutie soms weergegeven als een patroon van lijnen.

![Het aliaspatroon op de zijkanten van dit object](../../../articles/images/aliasing.jpg)

De resolutie van een stappenmotor in een typische 3D-printer voor consumenten ligt in het bereik van 50 tot 200 stappen per millimeter. Dit betekent dat de grootte van elke stap in de orde van 10 micron is. Als een lijn bijna evenwijdig aan de andere as wordt getrokken, zeg 0,5° van orthogonaal, dan zal zo'n stap elke 1,15 mm langs de lijn plaatsvinden. Deze stap zelf is te klein om zichtbaar te zijn, maar de trillingen zijn zichtbaar, vooral wanneer ze resoneren met de natuurlijke frequentie van het frame.

Preventie
----
Stappenmotoren kunnen kiezen tussen verschillende strategieën om hun as te draaien, maar er is een afweging tussen resolutie, koppel en ruis. Sommige firmware past dit automatisch aan op basis van verplaatsingssnelheid. Bij sommige firmware kun je dit ook via G-code instellen. Zo kan het g-code commando `M350` in de start g-code worden geplaatst om dit handmatig te configureren. Cura heeft (momenteel) geen manier om dit automatisch te configureren op basis van snelheid of structuur.

De meest betrouwbare manier om dit fenomeen te voorkomen is echter om het model zo aan te passen dat de aliasing niet zichtbaar is. Draai uw model zodat het aliasing-effect niet verschijnt. Als uw model een (bijna) rechte wand heeft, zorg er dan voor dat deze volledig is uitgelijnd met de assen of een hoek van enkele graden ten opzichte van de assen maakt.