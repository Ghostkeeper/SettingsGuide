Costeado del muro del puente
====
Cuando se hace un puente con líneas de pared, justo antes de que se imprima un puente, la alimentación de material se detiene por un momento. Durante este tiempo, el material restante dentro de la cámara de la boquilla se deja fluir hacia fuera, para reducir la presión dentro de la cámara de la boquilla. Esta técnica se llama [coasting](coasting_enable.md). Con este ajuste, la cantidad de coasting puede ser controlada. Esencialmente, esto controla la distancia por delante de un puente que el material dejará de fluir.

Una vez completado el puente, el material que no fue extruido será expulsado de todos modos. La cantidad total de extrusión de material seguirá siendo la misma. Esto restablece la presión en la boquilla, lo que evita la subextrusión.

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![Sin extrusión en un lado del puente, y con extrusión extra en el otro](../images/bridge_skin_density_100.png)

La unidad de este ajuste no pretende ser intuitiva. La distancia por delante del puente en la que el material dejará de fluir depende de varios factores:
* La longitud del muro hasta el puente. Cuanto más larga sea la pared, más puede costear.
* La tasa de flujo que sale de la boquilla durante la pared normal, que depende de la [velocidad](../velocidad/velocidad_pared.md), [ancho de línea](../resolución/ancho_de_línea_pared.md), [tasa de flujo](../material/flujo_material_pared.md) y [altura de capa](../resolución/altura_de_capa.md) de esas paredes. Cuanto mayor sea la tasa de flujo en las paredes normales, mayor será la distancia de costa.
* La tasa de flujo que sale de la boquilla durante la pared con puente, que depende de la [velocidad](bridge_wall_speed.md) y [flow rate](bridge_wall_material_flow.md) de esas paredes. Cuanto mayor sea el caudal en las paredes con puente, menor será la distancia de deslizamiento.

Este ajuste es un factor multiplicador sobre la longitud final.

El propósito de este inercia es reducir la presión dentro de la cámara de la boquilla. Esto es necesario, ya que cualquier presión restante en la cámara de la boquilla hará que el material baje a chorros una distancia considerable antes de solidificarse tan pronto como desaparezca la contrapresión. Este chorro de material hacia abajo da lugar a un pandeo. Esencialmente, las líneas que sobresalen son empujadas hacia abajo por el resto del material que aún está dentro de la boquilla. Si la presión dentro de la cámara de la boquilla se reduce, esta fuerza también se reducirá y habrá menos pandeo.

Aumentar la cantidad de inercia reducirá la presión dentro de la cámara de la boquilla para el momento en que el puente necesita ser impreso, lo que reducirá la cantidad de pandeo. La impresión será más precisa. Sin embargo, si se incrementa demasiado la cantidad de inercia, se producirá un periodo de subextrusión justo antes de que se imprima el puente. Como esta subextrusión está en las paredes de la impresión, será muy visible en el lado de la impresión.