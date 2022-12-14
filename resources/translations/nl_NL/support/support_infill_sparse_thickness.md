Dikte vullaag supportvulling
====
Omdat de optische kwaliteit en resolutie van de support niet belangrijk is, kun je voor de support dikkere lagen gebruiken om de printtijd te verkorten. Met deze instelling bepaal je hoe dik de lagen moeten zijn waarmee de support wordt geprint.

In de laagweergave lijkt het alsof de supportlijnen veel breder zijn geworden. Wanneer ze daadwerkelijk worden geprint, vallen de supportlijnen verder naar beneden in plaats van horizontaal uit te spreiden.

<!--screenshot {
"image_path": "support_infill_sparse_thickness.png",
"modellen": [
    {
        "script": "calendar_holder.scad",
        "transformatie": ["schaal(0.5)", "rotateX(90)"]
    }
],
"camerapositie": [18, 43, 19],
"instellingen": {
    "support_enable": waar,
    "support_infill_sparse_thickness": 0.24
},
"laag": 148,
"kleuren": 64
}-->
![Support vullaag dikte is ingesteld op 3 keer laaghoogte.](../../../articles/images/support_infill_sparse_thickness.png)

De dikte van de supportvulling moet een veelvoud zijn van de hoogte van de normale laag. Indien dit niet het geval is, wordt naar boven afgerond op de eerstvolgende hogere laag.

Deze instelling is niet van toepassing op het dak of de vloer van de support, alleen op de hoofdconstructie.

Deze instelling is vooral handig wanneer de support wordt geprint met een ander materiaal dan de rest van de print, en nog meer wanneer dat materiaal moeilijk te extruderen is, zoals plastic. BPVA. Doordat de drager niet in elke laag wordt geëxtrudeerd, hoeft de printer niet zo vaak van extruder te wisselen, wat veel tijd bespaart. Naarmate er meer materiaal op de geprinte lagen wordt geëxtrudeerd, worden materialen die een bepaalde tijd nodig hebben om te vloeien, betrouwbaarder geprint.

Zorg ervoor dat u deze waarde niet te veel verhoogt. Bij het wisselen van en naar de support moet de doorvoer door de nozzle aanzienlijk worden versneld en vertraagd. Dit gebeurt met enige vertraging, dus er is sprake van onder-extruderen wanneer de support begint en over-extruderen wanneer de support eindigt.