Print Volgorde
====
Als er meerdere modellen op de platform worden geplaatst, bepaalt dit de volgorde waarin de lagen voor die objecten worden geprint. Er zijn twee opties.

Alles in een keer
----
Alle objecten worden gelijktijdig geprint, dwz de lagen worden voor alle objecten gelijktijdig van onder naar boven geprint. Van elk object wordt één laag geprint voordat de volgende laag wordt geprint.

Dit heeft twee grote voordelen:
* De vorige laag krijgt meer tijd om af te koelen, wat resulteert in een betere kwaliteit bij het printen van kleine objecten.
* Het volledige bouwvolume kan worden gebruikt om te printen.

De een na de ander
----
De objecten worden opeenvolgend geprint, wat betekent dat alle lagen van een object worden geprint, en vervolgens gaat het terug naar de platform om het volgende object te printen.

De belangrijkste voordelen van deze modus zijn:
* Als de print om welke reden dan ook mislukt, zijn alle objecten die vóór de fout zijn voltooid, perfect in orde.
* Er zijn minder traverse bewegingen nodig om heen en weer te gaan tussen modellen. Dit bespaart wat printtijd en vermindert het aantal littekens op het oppervlak waar de nozzle het object verlaat en binnengaat.

Deze modus heeft echter enkele beperkingen om kop- en portaalbotsingen met het model te voorkomen.
* U kunt geen objecten printen die hoger zijn dan de portaalhoogte van uw printer. De portaalhoogte kan worden ingesteld in het dialoogvenster Machine-instellingen van de printer. Deze portaalhoogte geeft de verticale afstand aan tussen de nozzlepunt en de printkopwagen. De reden voor deze beperking is dat de printkop naar beneden moet bewegen naar de plaat om het tweede object te printen. Dit betekent dat het eerste object door de printkopwagen kan worden geraakt terwijl het tweede object wordt geprint. Theoretisch kan het laatst geprinte object hoger zijn dan de printkopdrager, maar omwille van de eenvoud staat Cura dit niet toe.
* Objecten moeten verder uit elkaar staan om te voorkomen dat de printkop de eerder geprinte modellen aan de zijkant raakt.
* De volgorde waarin de objecten worden geprint is vast en geoptimaliseerd zodat de objecten dichter bij elkaar kunnen worden geprint. Als uw printkop niet symmetrisch is, kan dit veel plaatruimte besparen.

**Een enkel object is alleen beschikbaar in enkele extrusie. Als u een printer met meerdere extruders gebruikt, moet u op één na alle extruders uitschakelen om deze instelling te laten verschijnen.**