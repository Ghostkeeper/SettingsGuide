Rijbrug hoogte
====
Deze instelling meet de afstand tussen de platform en het portaalsysteem waaraan de printkop is opgehangen. Deze hoogte is een bovengrens wanneer u [Print Volgorde](../blackmagic/print_sequence.md) print, aangezien het eerder geprinte object de portal zou kunnen raken.

![printkopafmetingen](../../../articles/images/head_dimensions.svg)

De meeste 3D-printers hebben hun printkoppen aan een of twee dwarsbalken hangen. De vorm van dit portaal is niet door Cura gemodelleerd: of het nu gaat om twee kruisende staven, een enkele arm die uit één richting komt of een enkele dwarsbalk waarlangs de printkop in één richting kan bewegen. Cura ziet dit portaal als een hard plafond bij het één voor één printen, ongeacht in welke volgorde de modellen worden geprint. Bij het één voor één printen wordt de hoogte van het bouwvolume verlaagd tot deze portaalhoogte, om aan te geven dat er geen modellen hoger dan de portaalhoogte zijn toegestaan.

Een uitzondering is wanneer er slechts één object op de platform wordt geladen. Dit object mag hoger zijn dan de portaalhoogte omdat er dan niets anders op de platform zal zijn dat tegen het portaal kan botsen.

**Aangezien dit een machine-instelling is, wordt deze normaal gesproken niet vermeld in de normale lijst met instellingen. De portaalhoogte kan worden gewijzigd in het dialoogvenster met printerinstellingen, dat u kunt vinden in de lijst met toegevoegde printers in het voorkeurendialoogvenster.**