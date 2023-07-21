Alle Gaten Verwijderen
====
Sommige modellen, vooral die gemaakt voor fabricagetechnieken zoals spuitgieten, hebben vaak interne holtes die niet zichtbaar zijn. Wanneer deze instelling is ingeschakeld, verwijdert Cura deze interne holtes.

<!--screenshot {
"image_path": "meshfix_union_all_remove_holes_disabled.png",
"modellen": [{"script": "foothold.scad"}],
"camerapositie": [-68, 40, 46],
"settings": {"meshfix_union_all_remove_holes": false},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "meshfix_union_all_remove_holes_enabled.png",
"modellen": [{"script": "foothold.scad"}],
"camerapositie": [-68, 40, 46],
"settings": {"meshfix_union_all_remove_holes": true},
"kleuren": 64
}-->
![Dit model heeft een gat in het midden](../../../articles/images/meshfix_union_all_remove_holes_disabled.png)
![Als de instelling is ingeschakeld, wordt het gat verwijderd](../../../articles/images/meshfix_union_all_remove_holes_enabled.png)

De holtes aan de binnenkant kunnen er zijn om materiaal te besparen, maar er zijn enkele beperkingen met 3D-printen waardoor deze modellen slecht printen. 3D-printers doen het bijvoorbeeld niet goed met dunne wanden die niet vele malen zo breed zijn als de lijndikte, en de bovenste laag heeft de neiging door te zakken tenzij ondersupportd door vulmateriaal. Over het algemeen is het beter om een solide mesh te maken en de slicer te laten beslissen hoe deze wordt gevuld. Met deze Mesh Fix-instelling kunt u dat doen zonder de mesh te hoeven bewerken.

Cura controleert alleen of een spouw in horizontale richting volledig is omsloten. Er wordt niet gecontroleerd of een spouw van boven of van onder open is. Het verschil kan nog steeds zichtbaar zijn van boven of van onder.