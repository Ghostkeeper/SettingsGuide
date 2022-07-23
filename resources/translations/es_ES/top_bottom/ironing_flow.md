Flujo de alisado
====
El alisado coloca líneas adicionales en la superficie, técnicamente sobreextruyendo. Este ajuste controla la cantidad que se extruye en esta pasada extra. El flujo es necesario para rellenar huecos en la superficie.

<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true
},
"colours": 64
}-->
<!--screenshot {
"image_path": "ironing_flow.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true,
    "ironing_flow": 20
},
"colours": 64
}-->
![10% de flujo](../images/ironing_enabled_enabled.png)
![20% de flujo](../images/ironing_flow.png)

Debe poner este ajuste lo suficientemente alto para mantener la presión en la boquilla. Esta presión tiene que llenar los huecos de la superficie superior. Si usted tiene una superficie superior muy áspera (debido a la almohadilla o la impresión rápida) es posible que tenga que aumentar esta configuración.