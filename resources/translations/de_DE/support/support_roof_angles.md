Richtungen der Dachlinien unterstützen
====
Das Stützdach wird normalerweise so ausgerichtet, dass es möglichst senkrecht zum darüber liegenden Modell und zum darunter liegenden Stützkörper steht. Wenn die Ausrichtung der Bodenlinien oder der Support-Linien angepasst wurde, ist es ratsam, auch die Ausrichtung der Support-Dachlinien anzupassen. Mit dieser Einstellung können Sie die Ausrichtung der Support-Dachlinien anpassen.

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
![Sowohl das Dach als auch der Boden sind um 0° und 90° gedreht.](../../../articles/images/support_interface_angles_0.png)
![Sowohl das Dach als auch der Boden sind um 45° und 135° gedreht.](../../../articles/images/support_interface_angles_45.png)

Für diese Einstellung können mehrere Winkel eingegeben werden, die durch Kommas getrennt sind. Cura wird diese Winkel in den Schichten abwechselnd verwenden.

Die Support-Dachlinien werden idealerweise so ausgerichtet, dass sie senkrecht zu den Support-Linien stehen, auf denen sie ruhen, sowie zu den Modelllinien, die auf ihnen ruhen. Wenn sie senkrecht ausgerichtet sind, verringert sich der Abstand, den diese Linien überbrücken müssen, wodurch das Durchhängen verringert und die Qualität der Überhänge verbessert wird. Dies ist besonders wichtig, wenn der Support nicht ganz geschlossen ist.