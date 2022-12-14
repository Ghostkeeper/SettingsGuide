Lijnrichting vulling
====
De vullijnen worden indien mogelijk meestal onder een hoek van 45 graden uitgelijnd. Onder deze hoek werken zowel de X- als de Y-motor samen om een ​​maximale acceleratie van de printkop te bereiken bij gebruik van een printer met het gebruikelijke Cartesiaanse portaalmechanisme.

Met deze instelling kunt u die hoek aanpassen. U kunt het aanpassen om meer kracht te produceren voor uw specifieke model of om een ​​grotere acceleratie te bereiken voor uw specifieke portaalsysteem (bijvoorbeeld voor Delta-printers).

![Vulling-lijnen met standaard hoeken van 45 en 135 graden](../../../articles/images/infill_pattern_lines.png)
![Vulling-lijnen met aangepaste hoeken van 0 en 30 graden](../../../articles/images/infill_angles_0_30.png)

De waarde van deze instelling moet een door komma's gescheiden lijst van hoeken zijn tussen vierkante haken. Een hoek van 0 graden resulteert in een lijn evenwijdig aan de Y-as. Deze waarden zijn afwisselend verdeeld over de lagen.
* De uiteindelijke print is het sterkst in de richting van de vullijnen. Als u wilt dat de print een specifieke kracht in horizontale richting uitoefent, is het logisch om de vullijnen in die richting uit te lijnen.
* Laat de instelling als een lege lijst om de standaardinstelling te gebruiken.
* De standaard is afhankelijk van het vulpatroon:
  * Voor Cross en Cross 3D-invulpatronen is de standaard [22]. Hiermee worden zoveel mogelijk lijnen in de buurt van de diagonalen uitgelijnd.
  * Voor lijn- en zigzagopvulpatronen is de standaardwaarde [45.135]. Hierdoor wisselt de uitlijning laag voor laag tussen de twee diagonalen.
  * Voor alle andere patronen is de standaard [45]. Dit lijnt zoveel mogelijk lijnen uit in de buurt van de diagonalen.