Patrón de alisado
====
El alisado cubre la superficie superior con un patrón de trayectoria. Este ajuste determina el patrón que se utiliza para planchar la superficie superior.

El objetivo del patrón es crear una superficie suave y continua. Si hay una interrupción en el patrón, se creará un borde visible en la superficie superior. Hay dos patrones disponibles.

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
Zigzag
----
![Patrón de alisado en zigzag](../images/ironing_enabled_enabled.png)

Esto hará que la boquilla vaya de un lado a otro de la superficie. Funciona bien y de forma fiable para la mayoría de las superficies, pero provocará más bordes de los necesarios.

<!--screenshot {
"image_path": "ironing_pattern.png",
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
    "ironing_pattern": "concentric"
},
"colours": 64
}-->
Concéntrico
----
![Patrón de alisado concéntrico](../images/ironing_pattern.png)

Esto hará que la boquilla haga círculos de dentro a fuera. Esto reducirá los bordes al mínimo, pero si los anillos concéntricos se hacen muy pequeños en el centro, el material se degradará debido a que la boquilla permanece demasiado tiempo alrededor del mismo punto. Esto deja una mancha visible en la superficie. En consecuencia, esto funciona mejor para las superficies que son largas y finas que para las que son igual de anchas que de altas.