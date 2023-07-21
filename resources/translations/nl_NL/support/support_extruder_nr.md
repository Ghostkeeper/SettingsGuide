Extruder Supportstructuur
====
Als uw printer meerdere extruders heeft, kunt u deze instelling gebruiken om te kiezen welke van deze extruders moet worden gebruikt om de supportstructuur te printen.

<!--screenshot {
"image_path": "support_extruder_nr.png",
"modellen": [
    {
        "script": "question_stick_clip.scad",
        "transformatie": ["roterenY(90)"],
        "object_settings": {"extruder_nr": 1}
    }
],
"camerapositie": [134, 134, 113],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_use_towers": false,
    "support_extruder_nr": 3
},
"color_scheme": "materiaal_kleur",
"kleuren": 64
}-->
![De support is geprint in wit materiaal, het model in blauw.](../../../articles/images/support_extruder_nr.png)

Door een ander materiaal te gebruiken, is de support gemakkelijker te verwijderen zonder de sterkte van de support op te offeren. Verschillende soorten materialen hechten niet zo goed aan elkaar, vooral als ze verschillende krimpfactoren hebben.

Sommige materialen zijn ook ontworpen om support printen. Sommige zijn b.v. opzettelijk extreem bros gemaakt, zodat ze gemakkelijker breken. Sommige materialen lossen op in water of ethanol, waardoor support kan worden verwijderd, zelfs als ze heel dicht bij het model worden geprint.

Als u de drager echter print met een andere extruder dan de rest van het model, moet de printer het materiaal bij elke laag veranderen, wat de printtijd kan verlengen. Als het supportmateriaal een andere kleur heeft dan het bouwmateriaal, kan het residu van het supportrmateriaal duidelijk zichtbaar zijn op de print.