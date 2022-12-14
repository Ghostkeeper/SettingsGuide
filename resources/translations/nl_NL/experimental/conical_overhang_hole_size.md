Maximale overhang oppervlak gat
====
Aangezien de instelling [Overhang Printbaar Maken](conical_overhang_enabled.md) elk type overhang elimineert, worden alle bruggen automatisch neergelaten en wordt de onderliggende overhang gesloten. Als de overstek echter aan alle kanten is ingesloten, wordt deze verlaagd totdat de ingesloten overhang volledig is gevuld. Dit heeft het effect dat alle neerwaartse gaten volledig worden gevuld, zelfs als de overhang die moet worden verwijderd slechts een klein stipje helemaal bovenaan is.

Om dit effect te voorkomen, zorgt deze instelling ervoor dat de overhang open blijft als deze aan alle kanten gesloten is en kleiner is dan een bepaald gebied. Dit geldt alleen voor gaten. Regelmatige overhang aan de buitenkant van het model blijft zich naar beneden uitstrekken om een ​​redelijk printbare hoek te behouden.

<!--screenshot {
"image_path": "conical_overhang_hole_size.png",
"modellen": [{"script": "plopper.scad"}],
"camerapositie": [-86, 29, -85],
"instellingen": {
    "conical_overhang_enabled": waar,
    "conical_overhang_hole_size": 20
},
"kleuren": 64
}-->
![Een klein gebied aan de punt kan overhangen zodat dit gat niet wordt opgevuld.](../../../articles/images/conical_overhang_hole_size.png)

Voor de meeste modellen is het redelijk veilig om deze waarde in te stellen op enkele tientallen vierkante millimeters. Als u deze te laag instelt, wordt het model meer aangepast om uitsteeksels te ondersupporten die eigenlijk te klein zijn om support te vereisen. Als u de waarde echter te hoog instelt, ontstaan ​​er aanzienlijke overhangende gebieden die moeilijk te overbruggen zijn.

Als er vanwege deze instelling grote overhanggebieden zijn, is het een goed idee om eerst de [Bruginstellingen inschakelen](bridge_settings_enabled.md) te controleren voordat u probeert het model aan te passen om de overhang te verwijderen.