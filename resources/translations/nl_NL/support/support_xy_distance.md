X/Y-afstand van de Supportstructuur
====
Het geeft aan hoe groot de horizontale afstand tussen de drager en het model moet zijn.

<!--screenshot {
"image_path": "support_xy_distance.png",
"modellen": [{"script": "clamp.scad"}],
"camerapositie": [-8, 185, 42],
"instellingen": {
    "support_enable": waar,
    "support_xy_overrides_z": waar,
    "support_xy_distance": 2
},
"kleuren": 64
}-->
![Een horizontale opening tussen de support en het model](../../../articles/images/support_xy_distance.png)

De horizontale speling is om te voorkomen dat de support het model raakt en een litteken op het oppervlak achterlaat. Hierdoor ontstaat echter ook een grotere afstand tussen het model en de supportconstructie ter plaatse van de overhang, waardoor kleinere overhang niet worden ondersteund.

X/Y versus Z-afstand
----
Zowel de X/Y-afstand als de Z-afstand moeten exact worden aangehouden, niet meer en niet minder. Dit is een beperking, dus er moet een voorkeur zijn tussen de twee. Dit wordt aangegeven door de instelling [Support Clearance Priority](support_xy_overrides_z.md). Deze instelling verandert het gedrag van de instelling support X/Y-afstand.

![X/Y heeft voorrang op Z](../../../articles/images/support_xy_overrides_z.svg)

Als X/Y voorrang heeft op Z, blijft de X/Y-afstand behouden, zelfs als dit betekent dat de Z-afstand te groot is. De Z-afstand wordt nog steeds minimaal gehouden.

![Z heeft voorrang op X/Y](../../../articles/images/support_z_overrides_xy.svg)

Als Z voorrang heeft op X/Y, wordt de Z-afstand gerespecteerd, zelfs als dit betekent dat de X/Y-afstand te klein is. De X/Y-afstand heeft alleen een effect vanaf de bovenkant van de support, waar ook de Z-afstand geen effect heeft.