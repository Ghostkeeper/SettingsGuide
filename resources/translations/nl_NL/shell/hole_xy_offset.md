Horizontale uitbreiding gaten
====
Dit is een corrigerende actie voor een printeffect waarbij gaatjes de neiging hebben om kleiner printen dan bedoeld. Met deze instelling kunt u de grootte van de verticale gaten in uw print vergroten. Net als bij de instelling [Horizontale Uitbreiding](xy_offset.md) worden de gaten in de print in alle richtingen vergroot.


Omdat het gat in alle richtingen uitzet, heeft de waarde van deze instelling betrekking op de straal van de gaten, niet op hun diameter.

<!--screenshot {
"image_path": "hole_xy_offset_0.png",
"modellen": [{"script": "rotary_tumbler_motor_lid.scad"}],
"camerapositie": [-30, 30, 111],
"instellingen": {"hole_xy_offset": 0},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "hole_xy_offset.png",
"modellen": [{"script": "rotary_tumbler_motor_lid.scad"}],
"camerapositie": [-30, 30, 111],
"instellingen": {"hole_xy_offset": 0.8},
"kleuren": 64
}-->
![De gaatjes in deze print moeten passen voor schroeven en assen, maar ze zijn te klein geprint](../../../articles/images/hole_xy_offset_0.png)
![De gaten zijn vergroot, de rest van de vorm is niet veranderd.](../../../articles/images/hole_xy_offset.png)

Door de viscositeit van het materiaal heeft het plastic bij het printen van een lijn in een curve de neiging om met de nozzle in de curve mee te slepen. Hierdoor wordt de curve iets kleiner dan bedoeld, omdat het materiaal naar binnen in de curve wordt getrokken. Normaal gesproken is dit niet echt zichtbaar, maar bij het printen van items die heel precies moeten passen, of bij het printen van items met hele kleine verticale gaatjes, wordt dit fataal voor de nauwkeurigheid van je print. De schroeven passen niet meer, de onderdelen schuiven niet meer netjes in elkaar, enzovoort.

Deze instelling compenseert dit door alle gaten iets groter te maken. In tegenstelling tot [Horizontale uitbreiding](xy_offset.md), heeft dit echter alleen invloed op gesloten gaten. Als er zelfs maar een klein gaatje is aan één kant (horizontaal, op dezelfde laag), dan wordt dat deel niet als een gaatje beschouwd en wordt het niet beïnvloed door deze instelling.

Een positieve waarde maakt de gaten groter. Een negatieve waarde maakt de gaten kleiner. In combinatie met de horizontale uitzetting worden de gaten eerst vergroot voordat de normale horizontale uitzetting wordt toegepast. Dit kan ertoe leiden dat dunne delen volledig verdwijnen voordat ze door normale horizontale uitzetting worden vergroot.