Ángulo de apoyo cónico
====
Este ajuste determina el ángulo de la pendiente en la que se imprime el soporte cónico.

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_10.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 10
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_neg10.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": -10
},
"colours": 64
}-->
Un ángulo de 30 grados](../images/support_conical_enabled.png)
Un ángulo de 10 grados](../images/support_conical_angle_10.png)
![Un ángulo de -10 grados, haciendo que la base sea más ancha](../images/support_conical_angle_neg10.png)

El ángulo de apoyo cónico es el compromiso más importante entre la estabilidad del apoyo y la cantidad de apoyo que se genera.

El uso de un ángulo grande hará que el soporte sea muy delgado durante una gran parte de su altura. Esto ahorra mucho material de soporte y tiempo de impresión. Cuando se necesita mucho material de soporte, esto puede ahorrar mucho tiempo y material, ya que hasta la mitad del soporte queda fuera. Sin embargo, como el soporte se vuelve muy delgado en la parte inferior, el soporte también puede ser menos estable, aumentando la posibilidad de que la impresión falle. Puede aumentar el [ancho mínimo] (support_conical_min_width.md) para evitarlo.

El uso de un ángulo negativo hará que el soporte sea más ancho hacia la parte inferior, en forma de volcán. Si su impresión tiene pequeñas características en lo alto que necesitan apoyo, normalmente producirán [torres] muy altas(../soporte/soporte_uso_torres.md) que son propensas a caerse durante la impresión. Con un ángulo negativo estas estructuras de soporte altas y delgadas se harán más anchas en la parte inferior. Esto les da una mayor estabilidad. Sin embargo, se tardará más en imprimir este soporte ya que requiere más material. Un ángulo de aproximadamente -5° es normalmente suficiente para dar a las estructuras de soporte más altas y delgadas suficiente estabilidad. Si su material tiende a rezumar mucho durante los desplazamientos, se necesitará un ángulo negativo mayor porque la estructura se verá más empujada debido a las manchas en el soporte.