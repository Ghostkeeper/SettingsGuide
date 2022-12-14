Nozzlediameter
====
Deze instelling meet de diameter van de nozzleopening waardoor het materiaal stroomt.

![printkopafmetingen](../../../articles/images/head_dimensions.svg)

Dit is een belangrijke maatregel waar andere instellingen naar kunnen verwijzen. Allereerst wordt de [Lijnbreedte](../resolution/line_width.md) meestal aangepast op basis van de grootte van de nozzle. Sommige printerprofielen beperken ook de laaghoogte op basis van de grootte van de nozzle, aangezien de grootte van de nozzle de belangrijkste factor is in hoe snel materiaal kan worden geëxtrudeerd.

De grootte van de nozzle wordt ook direct voor een detail gebruikt: bij het vullen van [Vul gaten tussen wanden](../shell/fill_perimeter_gaps.md) worden lijnstukken die meer dan twee nozzlematen uit elkaar liggen niet samengevoegd.

Pas de grootte van nozzle niet aan, tenzij u het fysieke nozzle daadwerkelijk verandert. Sommige slicers (waaronder Cura 15.04 en eerder) gebruiken de term "tipgrootte" voor de breedte van de printen lijnen. Cura gebruikt hiervoor de [Lijnbreedte](../resolution/line_width.md) instelling.

**Omdat dit een apparaatinstelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst. Als uw printer specifieke profielen heeft voor de beschikbare jets, kunt u deze selecteren in het menu Printerinstelling bovenaan in het midden van het scherm. Anders kunt u de diameter van de nozzle instellen in het dialoogvenster Printerinstellingen, te vinden in de lijst met toegevoegde printers in het dialoogvenster Instellingen.**