Extruder für Füllung Stützstruktur
====
Wenn Ihr Drucker mit mehreren Extrudern ausgestattet ist, kann der Hauptkörper des Supports mit einem anderen Extruder als die Support-Schnittstelle gedruckt werden. Mit dieser Einstellung können Sie wählen, welcher Extruder für den Hauptkörper des Supports verwendet wird.

<!--screenshot {
"image_path": "support_infill_extruder_nr.png",
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
    "support_extruder_nr": 3,
    "support_infill_extruder_nr": 2
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![Der Körper des Supports wird in Rot gedruckt, die Schnittstelle jedoch in Weiß.](../../../articles/images/support_infill_extruder_nr.png)

Einige Materialien eignen sich besser für den Druck von Supports als andere, aber diese Materialien können auch teurer oder langsamer zu drucken sein. Wenn man nur die Schnittstelle mit dem teuren Material druckt, den Großteil des Körpers aber mit einem günstigeren Material, kann man viel Zeit und Geld sparen. Die Schnittstelle wird immer noch mit dem teuren Material gedruckt, so dass der Teil, der das Modell berührt, gut aussieht oder leichter abzubrechen ist, aber der größte Teil des Supports wird mit dem billigeren Material gedruckt.

Wenn Sie lösliche Materialien zum Drucken der Support-Schnittstelle, aber unlösliche Materialien zum Drucken des Support-Körpers verwenden, bedenken Sie, dass der Körper möglicherweise nicht aus Hohlräumen entfernt werden kann, wenn es physikalisch nicht möglich ist, den Support-Körper durch eine kleine Öffnung zu bewegen. Wo ein lösliches Material normalerweise durch einen Hohlraum herausfließen kann, können unlösliche Materialien möglicherweise nicht hindurchgehen.