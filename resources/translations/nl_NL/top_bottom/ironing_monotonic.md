Monotone strijkvolgorde
====
Normaal gesproken regelt Cura de vloeiende lijnen zo dat de afstand ertussen klein is. Als deze instelling is geactiveerd, worden de vloeiende lijnen zo gerangschikt dat aangrenzende lijnen altijd overlappend in dezelfde richting worden geprint.

Strijk lijnen zijn standaard veel dunner dan de nozzle waarmee ze worden geprint, dus de lijnen overlappen sterk met de aangrenzende lijnen. Deze overlap geeft de lijnen een lichte schuine stand, waardoor ze licht in verschillende richtingen anders weerkaatsen. Wanneer aangrenzende lijnen elkaar anders overlappen, verandert deze reflectie. Dit zie je terug in het eindresultaat. Het geeft verschillende glans aan verschillende delen van het oppervlak. Door in een monotone volgorde te printen, is de overlap over het oppervlak gelijk, dus er zijn geen verschillen in lichtreflectie. Hierdoor ziet het oppervlak er egaler en gladder uit.

In tegenstelling tot [Monotone volgorde van boven naar beneden](../top_bottom/skin_monotonic.md), wordt dit effect bij het strijken echter met een heel ander effect. Tijdens het strijken is de doorvoersnelheid zo laag dat de verandering in de doorvoer die optreedt bij normaal printen erg groot is. Hierdoor wordt de laag die moet worden gestreken dikker aan het begin van de print, terwijl er nog steeds een merkbare rand overblijft waar de print werd onderbroken. Een vloeiend verloop zal deze randen niet elimineren. Hoewel het oppervlak er in de praktijk misschien wat gladder uitziet, is het in de praktijk niet effectief om de vloeiende lijnen in een monotone volgorde printen, tenzij uw printer zeer nauwkeurige controle heeft over de doorvoersnelheid.

Door de monotone volgorde neemt de nozzle verplaatsingen iets toe, maar dit effect is zeer minimaal.

Om een ​​glad oppervlak te krijgen, moet u dit combineren met de instelling [Combing-modus](../travel/retraction_combing.md) en eventueel [Hoogte Z-sprong](../travel/retraction_hop.md) activeren.