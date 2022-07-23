Volumen del arrastre
====
Este ajuste determina cuánto tiempo antes del final del contorno el alimentador dejará de alimentar material. Sin embargo, la duración del arrastre está configurada en un volumen de material. Está más relacionado con el volumen dentro de la cámara de la boquilla.

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
<!--screenshot {
"image_path": "coasting_volume_0_03.png",
"models": [{"script": "phone_holder.scad"}],
"camera_position": [0, -215, 117],
"minimum_layer": 1,
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
    "coasting_enable": true,
    "coasting_volume": 0.03,
    "z_seam_position": "backright"
},
"colours": 32
}-->
[Arrastre de 0,06mm³ de material](../images/coasting_enable.png)
![Arrastre de 0.03mm³ de material](../images/coasting_volume_0_03.png)

Aumentar el volumen de arrastre hace que la boquilla deje de extruir más lejos antes de terminar el contorno. El resultado es que tendrá más subextrusión hacia el final. La función del coasting es compensar el blob cuando el contorno se cose, por lo que aumentar el volumen de coasting puede compensar blobs más grandes.

Sin embargo, si se aumenta demasiado el volumen de la costura, se producirá una fuerte subextrusión hacia el final del contorno. Incluso puede provocar cierta subextrusión en lo que se imprima después del contorno, ya que la presión en la boquilla sigue siendo baja en ese momento.