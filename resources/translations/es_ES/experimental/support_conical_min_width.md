Anchura mínima del soporte cónico
====
Si el soporte cónico está activado y configurado para encoger la estructura de soporte, este ajuste determina la anchura mínima a la que el soporte cónico encogerá el soporte. El soporte no se hará más delgado a menos que el área del voladizo que necesita soporte ya sea más delgada.

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
"image_path": "support_conical_min_width_20.png",
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
    "support_conical_angle": 30,
    "support_conical_min_width": 15
},
"colours": 64
}-->
![Una anchura mínima de 5mm](../images/support_conical_enabled.png)
![Una anchura mínima de 15mm](../images/support_conical_min_width_20.png)

Si un gran volumen de soporte se apoya en un pequeño pilar de soporte, este soporte será muy propenso a caerse. Aumentando la anchura mínima se incrementa la anchura del pilar base del soporte sobre el que gravitará el cono. Esto aumenta la fiabilidad de la impresión, pero costará material adicional. En definitiva, el soporte cónico será menos eficaz para reducir el tiempo de impresión.