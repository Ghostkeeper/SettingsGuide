Machinekop en ventilatorpolygoon
====
Deze instelling vertelt Cura hoe de vorm van uw printkop eruitziet van bovenaf gezien. Dit is nodig om botsingen te voorkomen bij het printen in [Printvolgorde](../blackmagic/print_sequence.md).

![printkopafmetingen](../../../articles/images/head_dimensions.svg)
![Van bovenaf gezien is de vorm van de printkop relatief ten opzichte van de nozzlepositie](../../../articles/images/machine_head_with_fans_polygon.png)

Deze instelling bevat een lijst met coördinaten die een veelhoek vormen. De coördinaten zijn relatief ten opzichte van de "positie" van de kop, waar de nozzles ook relatief ten opzichte van zijn gepositioneerd.

Cura gebruikt dit om een ​​botsingsgebied te creëren rond de objecten die u printt in "Een-voor-een"-modus. Dit botsingsgebied voorkomt dat de objecten te dicht bij elkaar komen te staan, zodat ze niet kunnen worden geprint zonder dat de printkop botst met het eerder geprinte model. Het botsingsgebied heeft echter niet dezelfde vorm als de printkop zelf: het is een bolle schil rond de printkop om botsingen te voorkomen, zelfs wanneer deze beweegt. Ook wordt het gereduceerd om symmetrisch te zijn. Als de nozzle zich bijvoorbeeld meer links van de printkop bevindt (zoals in de afbeelding hierboven), wordt het botsingsgebied verkleind zodat een ander object rechts van de reeds geprinte objecten kan worden geplaatst. De volgorde waarin deze objecten worden geprint

**Omdat dit een apparaatinstelling is, wordt deze normaal gesproken niet vermeld in de normale lijst met instellingen. De grootte van de printkop kan echter ruwweg worden aangegeven in het dialoogvenster met printerinstellingen, dat zich in de lijst met toegevoegde printers in het instellingenvenster bevindt. U kunt alleen de positie links, rechts, boven en onder aan de printkop specificeren.**