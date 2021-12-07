Extruder für Stützstruktur
====
Wenn Ihr Drucker über mehrere Extruder verfügt, können Sie mit dieser Einstellung wählen, mit welchem dieser Extruder die Support-Struktur gedruckt werden soll.

<!--screenshot {
"image_path": "support_extruder_nr.png",
"models": [
    {
        "script": "question_stick_clip.scad",
        "transformation": ["rotateY(90)"],
        "object_settings": {"extruder_nr": 1}
    }
],
"camera_position": [134, 134, 113],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_use_towers": false,
    "support_extruder_nr": 3
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![Der Support wird in weißem Material gedruckt, das Modell in blauem.](../../../articles/images/support_extruder_nr.png)

Durch die Verwendung eines anderen Materials lässt sich der Support leichter entfernen, ohne dass die Festigkeit des Supports darunter leidet. Verschiedene Materialtypen haften nicht sehr gut aneinander, insbesondere wenn sie unterschiedliche Schrumpfungsraten aufweisen.

Außerdem sind einige Materialien dafür ausgelegt, Support zu drucken. Sie können z. B. absichtlich extrem spröde gemacht werden, damit sie leichter brechen. Manche Materialien lösen sich in Wasser oder Ethanol auf, so dass sich Support auch dann noch entfernen lässt, wenn er sehr nah am Modell gedruckt wurde.

Wenn man den Support mit einem anderen Extruder druckt als den Rest des Modells, muss der Drucker allerdings bei jeder Schicht das Material wechseln, was die Druckzeit verlängern kann. Wenn das Support-Material eine andere Farbe hat als das Baumaterial, können die Rückstände des Supports auf dem Druck deutlich sichtbar sein.