Habilitar ajustes del puente
====
Cuando su modelo tiene algún saliente que se apoya en ambos lados, Cura detectará esto y modificará el área de la piel que sobresale para imprimir mejor. Si esta configuración está habilitada, puede ajustar la detección de estas áreas de puente y el comportamiento resultante para que se puentee mejor.

<!--screenshot {
"image_path": "bridge_settings_enabled_default.png",
"models": [
    {
        "script": "rack_straight.scad",
        "scad_params": ["length=40"]
    }
],
"camera_position": [0, 74, -137],
"colours": 32
}-->
<!--screenshot {
"image_path": "bridge_settings_enabled_enabled.png",
"models": [
    {
        "script": "stairwell.scad",
        "scad_params": ["steps=4", "width=10", "height=20"]
    }
],
"layer": 275,
"settings": {
    "bridge_settings_enabled": true
},
"camera_position": [-12, 28, 63],
"colours": 64
}-->
Cuando se detecta un puente, las líneas de piel se orientan para salvar el hueco lo mejor posible](../images/bridge_settings_enabled_default.png)
Con la configuración del puente activada, las líneas de puente se imprimen con una configuración diferente](../images/bridge_settings_enabled_enabled.png)

Normalmente, Cura utilizará una técnica de puentes bastante rudimentaria. Cura detectará las áreas de piel que sobresalen y que se apoyan en varios lados. La [dirección de esas líneas de piel](../top_bottom/skin_angles.md) se ajusta para puentear esas áreas automáticamente. Esto asegura que la mayor parte posible del área que sobresale se apoya en múltiples lados y mejora la calidad de impresión.

Sin embargo, cuando esta configuración está activada, puede ajustar ese comportamiento de forma más precisa según sus necesidades. Esto le permite ajustar:
* la velocidad de impresión
* la velocidad de flujo
* la densidad (como la densidad de relleno, pero con las líneas de piel)
* la velocidad del ventilador
* para las paredes, también el arrastre

Estas configuraciones pueden ser ajustadas por separado para la piel que salva un hueco así como para las paredes. Si [El puente tiene varias capas](bridge_enable_more_layers.md) está activado, también se pueden ajustar por separado para la segunda y tercera capa por encima del hueco puenteado. También permite ajustar qué partes de la impresión se ven como áreas de puente, ajustando [qué fracción de un área debe estar sobre el aire](bridge_skin_support_threshold.md) y un [ancho mínimo para las paredes](bridge_wall_min_length.md).

Al activar los parámetros de puente, se obtiene un mayor control sobre cómo se manejan los puentes en la impresión. Afinando muy bien los parámetros de los puentes, puedes mejorar la calidad de tus voladizos significativamente y mejorar la precisión en la dirección vertical. El único inconveniente es que si no ajustas la configuración de los puentes a tu impresora, la impresión podría empeorar con la misma probabilidad.