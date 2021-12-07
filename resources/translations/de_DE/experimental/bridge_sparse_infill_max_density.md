Maximale Dichte der Materialsparfüllung der Brücke
====
Wenn Sie mit einer sehr geringen Füllungsdichte drucken, neigt die Außenhaut zum Durchhängen, was zu [Pillowing](../troubleshooting/pillowing.md) und allgemein zu unregelmäßigen Oberflächen auf der Oberseite des Drucks führt. Optional können die Überbrückungstechniken auch auf die Außenhaut angewendet werden. Mit dieser Einstellung wird festgelegt, ab welcher Füllung die Überbrückungstechnik angewendet werden soll.

<!--screenshot {
"image_path": "bridge_sparse_infill_max_density.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"layer": 108,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_sparse_infill_max_density": 100
},
"camera_position": [58, 27, 104],
"colours": 64
}-->
![Die Außenhaut überbrückt die Füllung](../../../articles/images/bridge_sparse_infill_max_density.png)

Diese Einstellung ist als Schwellenwert konfiguriert, damit die Profile einen einzigen Wert enthalten. Während der Benutzer die Füllungsdichte ständig anpasst, wird die Überbrückung für die Außenhaut automatisch aktiviert oder deaktiviert.

Die Überbrückung der Außenhaut führt im Allgemeinen zu einer glatteren Oberfläche bei sehr niedrigen Füllungsraten. Achten Sie jedoch darauf, dass genügend [obere Schichten](../top_bottom/top_layers.md) vorhanden sind, um die Oberfläche richtig zu schließen, ohne die Überbrückungstechnik auf die obersten Schichten anzuwenden. Die Überbrückungstechnik, insbesondere bei reduzierter [Linienbreite](bridge_skin_material_flow_3.md), wird die Oberfläche nicht vollständig schließen. Wenn die oberste Außenhaut nicht genügend Schichten hat, entstehen Löcher im Druck und die Festigkeit wird beeinträchtigt.