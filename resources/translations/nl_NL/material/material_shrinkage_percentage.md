Schaalfactor krimpcompensatie
====
<!--if cura_version >= 4.8-->Met deze instelling wordt het model automatisch geschaald voor het slicen. Het doel is om de krimp te compenseren die optreedt als de print afkoelt tot kamertemperatuur. Door de print iets groter te maken dan gewenst, kan het eindresultaat beter aansluiten bij de oorspronkelijke afmetingen van het invoermodel. Deze schaalfactor wordt gelijkelijk toegepast op alle dimensies (X, Y en Z).

De hele modelgroep wordt geschaald vanuit het midden. Wanneer u meerdere modellen print, worden ze allemaal geschaald vanaf hetzelfde startpunt. Hierdoor kunt u de modellen zeer dicht bij elkaar plaatsen zonder ze in de uiteindelijke print te overlappen. Ook zijn de botsingsgebieden van de modellen geschaald, zodat je precies kunt zien waar je print terecht komt. Dit voorkomt ook dat u modellen op plaatsen plaatst waar ze functies van de print of printer zouden verstoren, b.v. B. met de primepijler of de clips van de platvorm.

Een factor 100% veroorzaakt geen schaling. Een schaalfactor van iets meer dan 100% is redelijk voor veel technische materialen zoals ABS of polypropyleen. Een schaalfactor van minder dan 100% zou erop wijzen dat het materiaal groeit als het afkoelt, een beetje zoals schuim.

Zuivere chemische gegevens over hoeveel een materiaal krimpt tussen printtemperatuur en kamertemperatuur zijn niet voldoende om een ​​goede waarde voor deze instelling te voorspellen, aangezien het printproces ook krimp beïnvloedt. Wanneer het plastic in een lijn wordt geëxtrudeerd, strekt het zich uit in de richting van de lengte van de lijn en krimpt het meer in die as. De krimp is niet uniform, maar deze instelling past alleen een uniforme schaalfactor toe in alle richtingen. Om nauwkeurige resultaten te krijgen, moet u de schaalfactor toepassen op de as die het meest relevant is voor uw toepassing. Als er veel lange, rechte lijnen langs de belangrijkste dimensie zijn, moet de schaalfactor groter zijn.

Als de schaalfactor groter is dan 100,5% en u drukt iets groots af, dan zal Cura een waarschuwing tonen dat er mogelijk problemen zijn [Kromtrekken](../troubleshooting/warping.md).<!--endif-->

<!--if cura_version < 4.8:Dit is een beschrijvende instelling die Cura vertelt hoeveel het materiaal krimpt als het afkoelt van printtemperatuur naar kamertemperatuur.

Deze instelling wordt momenteel niet gebruikt voor slicen. Het wordt momenteel alleen gebruikt om de gebruiker te waarschuwen bij het printen van grote objecten als de krimpverhouding groter is dan 0,5%.
-->
**Deze instelling is niet zichtbaar in de instellingenlijst. Het is slechts een interne instelling die wordt overschreven door het materiaalprofiel.**