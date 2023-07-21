Afwisselend Extra Wand
====
Met deze instelling wordt om de andere laag een extra wand toegevoegd. Op deze manier wordt de vulling verticaal tussen de wanden geklemd, waardoor er meer druk ontstaat.

Als u bijvoorbeeld het aantal wandlijnen instelt op twee wanden en de extra wand inschakelt, worden twee wanden geprint op even genummerde lagen en drie wanden op oneven genummerde lagen.

<!--screenshot {
"image_path": "alternate_extra_perimeter.gif",
"modellen": [
    {
        "script": "gear.scad",
        "transformatie": ["schaal(0.7)"]
    }
],
"camera_positie": [0, 30, 123],
"instellingen": {
    "zig_zaggify_infill": waar,
    "alternate_extra_perimeter": true
},
"laag": [15, 16, 17, 18],
"minimum_laag": [15, 16, 17, 18],
"kleuren": 32
}-->
![Deze afbeelding toont de wanden die worden beïnvloed door het wijzigen van deze instelling.](../../../articles/images/alternate_extra_perimeter.gif)

Het inschakelen van deze instelling kost extra tijd, ongeveer de helft van de tijd van het toevoegen van een extra wand. In sommige opzichten is deze afwisselende extra wand bijna net zo goed als een volledige extra wand, in sommige opzichten niet:
* Het verhoogt de hechting tussen de vulling en de wanden aanzienlijk, aangezien de vullinglijnen ook loodrecht kunnen hechten aan de extra wand erboven en eronder. In dit opzicht voldot de optie zeer goed. Ze is erg efficiënt.
* Het verhoogt de stijfheid van de print met meer dan een halve extra wand. Door zich aan de aangrenzende wand te binden, verdeelt het de spanning over meer strengen en biedt het een betere bescherming tegen krachten in horizontale richting. De afwisselende extra wand heeft noch een bijzonder voordeel, noch een bijzonder nadeel.
* Een echte extra wand zou ook de sterkte van de gelaagde composiet verhogen. wanden printen langzaam af en zijn daarom een belangrijke bron van gelaagde composietsterkte. De afwisselende extra wand sluit echter niet aan op de aangrenzende lagen, omdat deze alleen in elke andere laag voorkomt.

Bijgevolg is de alternerende extra wand een efficiënte manier om de horizontale stijfheid te vergroten, maar niet een efficiënte manier om de verticale taaiheid te vergroten.