Richtungen der Verbindungslinien unterstützen
====
Die Support-Schnittstelle ist normalerweise so ausgerichtet, dass sie möglichst senkrecht zum Modell und dem sie umgebenden Support-Körper steht. Wenn die Ausrichtung der oberen/unteren Linien oder der Support-Linien angepasst wurde, ist es ratsam, auch die Ausrichtung der Support-Schnittstellenlinien anzupassen. Mit dieser Einstellung können Sie die Ausrichtung der Support-Schnittstellenlinien anpassen.

<!--screenshot {
"image_path": "support_interface_angles_0.png",
"models": [
    {
        "script": "plug.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 36, 92],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_interface_pattern": "lines",
    "support_interface_angles": [0, 90]
},
"layer": 118,
"colours": 128
}-->
<!--screenshot {
"image_path": "support_interface_angles_45.png",
"models": [
    {
        "script": "plug.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 36, 92],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_interface_pattern": "lines",
    "support_interface_angles": [45, 135]
},
"layer": 118,
"colours": 128
}-->
![Abgewinkelt bei 0° und 90°](../../../articles/images/support_interface_angles_0.png)
![Abgewinkelt bei 45° und 135°](../../../articles/images/support_interface_angles_45.png)

Für diese Einstellung können mehrere Winkel eingegeben werden, die durch Kommas getrennt sind. Cura wird diese Winkel abwechselnd auf die Schichten verteilen.

Die Support-Schnittstellenlinien werden idealerweise so ausgerichtet, dass sie senkrecht zu den Linien stehen, auf denen sie ruhen, sowie zu den Linien, die auf ihnen ruhen. Wenn Sie sie senkrecht ausrichten, verringert sich der Abstand, den diese Linien überbrücken müssen, wodurch die Durchbiegung verringert und die Qualität der Überhänge verbessert wird. Dies ist besonders wichtig, wenn der Support nicht ganz geschlossen ist.