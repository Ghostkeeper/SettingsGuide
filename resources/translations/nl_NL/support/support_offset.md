Horizontale Uitzetting Supportstructuur
====
Deze instelling zorgt ervoor dat de support iets breder is en zich horizontaal in alle richtingen uitstrekt.

<!--screenshot {
"image_path": "support_offset.png",
"modellen": [{"script": "duct.scad"}],
"camerapositie": [47, 72, 128],
"instellingen": {
    "support_enable": waar,
    "support_offset": 1.8
},
"kleuren": 64
}-->
![De support is breder dan nodig is om het model te ondersteunen](../../../articles/images/support_offset.png)

Deze instelling heeft meerdere toepassingen, afhankelijk van het materiaal dat wordt gebruikt voor support en het type model dat moet worden ondersupportd:
* Als u deze instelling verhoogt, wordt de support breder en dus stabieler. Dit is handig voor hoge modellen met kleine overhangen, anders zou de overhang worden ondersteund door een zeer hoge, dunne pijler. Met enige horizontale verlenging wordt het een zeer hoge maar iets bredere supportpijler.
* Het verhogen van deze instelling dient ook als veiligheidsmaatregel om ervoor te zorgen dat supportgebieden een bepaald minimumoppervlak hebben. Dit is nodig bij materialen die moeilijk te extruderen zijn, zoals PVA.
* Als u deze instelling verlaagt, vermindert u het gebruik van supportmateriaal en de printtijd. Natuurlijk verhoogt het verhogen van de instelling de materiaalvereisten en de printtijd. Zie ook de functie [Conische supportstructuur inschakelen](../experimental/support_conical_enabled.md), die de breedte van de support verkleint zonder het gebied dat de support ondersteuning aan te tasten.
* Als u deze instelling op een negatieve waarde zet, kunt u ook dunne supportpijlers volledig verwijderen. Als de support toch niet zou worden geprint, is het misschien beter om deze helemaal weg te laten. Een methode om support te verwijderen zonder de overhangkwaliteit van de rest van het model te beïnvloeden, is de Support Blocker-tool.