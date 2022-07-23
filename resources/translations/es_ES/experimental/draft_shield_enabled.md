Habilitar parabrisas
====
Cuando esta opción está activada, la impresora construirá un caparazón alrededor de su impresión que la protegerá de las corrientes de aire del entorno.

<!--screenshot {
"image_path": "draft_shield_enabled.png",
"models": [{"script": "headphone_hook.scad"}],
"camera_position": [-56, 139, 305],
"settings": {
    "draft_shield_enabled": true
},
"colours": 32
}-->
![Se imprime un parabrisas alrededor del modelo](../images/draft_shield_enabled.png)

Algunas impresoras y materiales de impresión son muy sensibles al entorno en el que se imprimen. La impresión en diferentes lugares de la placa de construcción puede conducir a resultados diferentes, ya que son más susceptibles a las corrientes de aire desde el exterior. Si la impresión se deja en marcha durante la noche y la habitación se enfría, esto podría afectar significativamente a la impresión. El parabrisas pretende reducir este efecto creando un pequeño volumen aislado alrededor de la impresión. Sirve de "cámara caliente" improvisada para mantener la impresión caliente y protegerla de las corrientes de aire frío del exterior.

El escudo se imprime sobre la marcha mientras se imprime el modelo. Si hay varios extrusores implicados en la impresión, el parabrisas se imprimirá con el extrusor que inicie la capa. Esto se alternará de capa a capa.

El parabrisas tiene varios efectos importantes en la impresión:
* Mantendrá la temperatura de la impresión más constante. Este es el efecto previsto del parabrisas. Como resultado, las bandas debidas a los cambios de temperatura en la sala deberían reducirse.
* Generalmente la temperatura dentro del parabrisas será más alta que si no hay parabrisas. Esto se debe a que el calor tiene más dificultades para escapar y no puede haber corrientes de convección que suban con el aire caliente de la impresión. Esto tiene un efecto en todos los aspectos de la impresión. En particular, habrá más encordamiento y hundimiento.
* Los ventiladores del cabezal de impresión serán menos eficaces. El escudo también interrumpe el flujo de aire allí. Para aumentar la eficacia de los ventiladores en el cabezal de impresión, se puede aumentar la [distancia] (draft_shield_dist.md) del parabrisas.
* El parabrisas puede duplicarse como un [Escudo contra el rezume](../dual/ooze_shield_enabled.md). Si se realizan movimientos de desplazamiento hacia un objeto que está protegido por un escudo contra corrientes de aire, cualquier exudado que quede en la boquilla se limpiará en el escudo.
* El parabrisas puede doblarse como una [Torre de purga](../dual/prime_tower_enable.md). Dado que se imprime antes del objeto, la impresión del parabrisas es una forma de conseguir que el material se purgue y fluya correctamente. Sin embargo, esto sólo es efectivo con 2 extrusores, ya que no todos los extrusores se purgarán si hay más de 2.