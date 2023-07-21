Alternerende wandrichtingen
====
Als deze instelling is geactiveerd, worden de wanden afwisselend met de klok mee en tegen de klok in geprint.

De eerste binnenwand is geprint in de tegenovergestelde richting van de buitenwand, en de tweede binnenwand is geprint in de tegenovergestelde richting. Daarnaast begint de volgende laag ook in de tegenovergestelde richting, dus de op elkaar gestapelde wanden worden ook afwisselend geprint.

Het veranderen van de compressierichting vermindert het effect van interne spanningen in het model, waardoor het effect van [Kromtrekken](../troubleshooting/warping.md) wordt verminderd. Tijdens het printen van een lijn trekt nozzle behoorlijk hard aan het filament van gesmolten materiaal, waardoor het plastic uitrekt. Tijdens het uitharden kan deze spanning het model vervormen. Als de aangrenzende lijnen in de tegenovergestelde richting worden geprint, wordt deze spanning gecompenseerd door de aangrenzende lijnen in de tegenovergestelde richting te trekken. De kracht van de spanning wordt gecompenseerd door een spanning in de tegenovergestelde richting.

Het nadeel van het veranderen van de wandrichtingen komt voort uit de hysterese van het printerportaal. Als de assen of rollen van de printer speling hebben, worden de diagonale lijnen op een iets andere plaats geplaatst wanneer in de tegenovergestelde richting wordt geprint. Hierdoor wordt de wand minder glad en zijn de printafmetingen minder nauwkeurig. Dit effect treedt niet op bij een goed afgestelde printer. Dus als de printer de riemen, katrollen en precieze onderdelen heeft aangespannen, zal het wisselen van wandrichting waarschijnlijk alleen maar voordelen opleveren.

Bij [Wandvolgorde](../shell/inset_direction.md) maakt deze instelling de naad van de wand beter zichtbaar en veroorzaakt het wat rimpellen omdat nozzle een volledige 180° draai maakt net voor het begin van de buitenwand, waardoor trillingen. Bij het printen van buiten naar binnen is dit effect minder merkbaar.