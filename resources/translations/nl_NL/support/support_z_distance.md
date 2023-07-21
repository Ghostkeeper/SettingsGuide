Z-afstand Supportstructuur
====
Deze instelling specificeert de verticale afstand die moet worden aangehouden tussen de support en het model, zowel aan de bovenkant van de support als aan de onderkant.

<!--screenshot {
"image_path": "support_z_distance.png",
"modellen": [{"script": "rack.scad"}],
"camerapositie": [0, 129, 11],
"instellingen": {
    "support_enable": waar,
    "support_z_distance": 1
},
"kleuren": 32
}-->
![De Z-afstand bepaalt zowel de boven- als onderkant van de support](../../../articles/images/support_top_bottom_distance.svg)
![Een verticale afstand tussen model en support (overdreven)](../../../articles/images/support_z_distance.png)

Deze instelling heeft de grootste invloed op hoe goed de support aansluit op het model.

Door deze instelling te verlagen, kan de support beter aansluiten op het model. Dit zorgt ervoor dat overhangen er beter uitzien, omdat ze niet zo veel kunnen doorhangen. Daarnaast wordt de stabiliteit van de support verbeterd doordat deze stevig op het model zit aan de onderkant van de support.

Als u deze instelling verhoogt, wordt het gemakkelijker om de support te verwijderen. Het laat minder littekens achter op het oppervlak waar de support het model ondersteunde. Aan de andere kant wordt het model ook niet langer ondersteund. Dit vermindert de oppervlaktekwaliteit van de overhang.

In het algemeen geldt dat hoe beter het supportmateriaal hecht aan het bouwmateriaal, hoe groter deze instelling moet zijn. Als u een ander materiaal gebruikt om support printen, kan de z-afstand aanzienlijk worden verkleind, omdat twee verschillende materialen na uitharding gemakkelijker van elkaar scheiden. Als u een materiaal gebruikt met een goede laaghechting, moet de instelling iets worden verhoogd. Heter of met zwaardere lijnen printen verhoogt ook de hechting, dus deze instelling moet ook worden verhoogd.