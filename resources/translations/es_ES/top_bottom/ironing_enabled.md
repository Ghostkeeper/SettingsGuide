Habilitar alisado
====
El alisado hace que la impresora haga otra pasada sobre la superficie superior para hacerla más suave. Esta pasada extra tiene un ancho de línea muy pequeño y se imprime muy lentamente.

<!--screenshot {
"image_path": "ironing_enabled_disabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": false
},
"colours": 64
}-->
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
![Una impresión normal, vista desde la parte superior](../images/ironing_enabled_disabled.png)
![Con el alisado activado, observe las finas líneas de la parte superior](../images/ironing_enabled_enabled.png)

El alisado imprimirá un patrón de líneas en la parte superior de la superficie de su impresión. Esto tiene dos efectos benéficos principales:
* Derrite la superficie superior de nuevo al pasar por encima de ella varias veces con una boquilla caliente. De ahí viene el nombre de "planchado". Como la velocidad de movimiento es tan baja y el ancho de línea es tan pequeño, la boquilla calentará la superficie de forma significativa. A continuación, la parte plana de la boquilla la alisa.
* Rellena los huecos de la superficie. El movimiento de alisado se realiza a la misma altura que la propia capa. Tiene menos flujo que una capa completa, pero sigue teniendo algo de flujo. En teoría, este flujo no tiene adónde ir, pero en la práctica mantendrá la presión dentro de la cámara de la boquilla. Siempre que la boquilla pase por un desnivel en la superficie, el material de la boquilla fluirá hacia ese hueco.

Sin embargo, el planchado también tiene algunas desventajas:
* Aumenta considerablemente el tiempo de impresión.
* Si el patrón de planchado tiene interrupciones (porque tiene que viajar a diferentes partes), dejará una línea visible entre la parte que se planchó antes y la que se planchó después. Esto puede evitarse a veces ajustando el [Patrón de planchado](ironing_pattern.md) a un patrón diferente, como por ejemplo Concéntrico.
* Las superficies inclinadas, o las superficies superiores con muchos detalles, pueden plancharse también, lo que aumenta el efecto de topografía. Los bordes entre las capas se vuelven más pronunciados. Esto puede evitarse activando [Planchar sólo la capa más alta] (ironing_only_highest_layer.md).