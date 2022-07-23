Habilitar depósito por inercia
====
Si este ajuste está activado, la boquilla dejará de extruir material ligeramente antes de cerrar un contorno de pared. La idea es que la cámara de la boquilla pueda entonces vaciarse en el último trozo de línea que hay, lo que reduce la presión sobre la boquilla y permite que se bloquee al inicio del contorno. Esto produce entonces menos costura en el lugar donde se inicia el contorno y reduce el encordamiento en el movimiento de desplazamiento posterior.

<!--screenshot {
"image_path": "coasting_enable.png",
"models": [{"script": "phone_holder.scad"}],
"camera_position": [0, -215, 117],
"minimum_layer": 1,
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
    "coasting_enable": true,
    "coasting_volume": 0.06,
    "z_seam_position": "backright"
},
"colours": 32
}-->
![En la vista de capas, la costura es fácil de ver si se activa el arrastre, porque entonces hay un movimiento de desplazamiento allí](../images/coasting_enable.png)

La activación del depósito por inercia tiene por objeto reducir la visibilidad de la costura en las paredes. Si normalmente tienes costuras grandes y gruesas, habilitar esto puede reducir ese efecto. Es básicamente lo contrario de lo que hace la [Distancia de barrido de la pared exterior](../shell/wall_0_wipe_dist.md), por lo que es una buena idea intentar reducir el barrido primero antes de intentar el arrastre.

En teoría, la reducción de la anchura de banda siempre produce una infraextrusión. Si esto es visible en la impresión real o no depende de las circunstancias. El arrastre por inercia tiende a ser algo más eficaz con las impresoras de accionamiento directo. Si su impresora tiene un accionamiento directo, querrá reducir el [volumen de coasting](coasting_volume.md) a un valor más bajo que cuando se utilizan tubos Bowden o ejes de accionamiento flexibles, porque la reacción del caudal es mucho más rápida entonces. Con los sistemas de alimentación tipo Bowden también será mucho más difícil controlar la cantidad de arrastre para reducir eficazmente la visibilidad de la costura.