Distancia del borde
====
Este ajuste hace que aparezca un hueco entre el modelo y el borde. Las líneas del borde ya no están firmemente adyacentes al modelo.


<!--screenshot {
"image_path": "brim_gap.png",
"models": [
    {
        "script": "arrow.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [-22, 32, 133],
"settings": {
    "adhesion_type": "brim",
    "brim_gap": 1
},
"colours": 32
}-->
![El borde se mantiene a cierta distancia del modelo](../images/brim_gap.png)

El objetivo de este hueco es facilitar la retirada del borde del modelo. Al colocar las líneas del borde ligeramente separadas del modelo real (del orden de la mitad de la anchura de la línea), la conexión entre el borde y el modelo es más débil que una capa, lo que ayuda a arrancar el borde con la mano. También reducirá la cicatriz o pata de elefante que deja el borde tras su retirada. Esto es especialmente efectivo con una mayor [altura de capa inicial] (../resolution/layer_height_0.md), ya que el borde grueso tiende a ser más difícil de quitar entonces.

Por otro lado, esto también reduce la eficacia del borde para mantener el modelo pegado a la placa de construcción. Con un área de contacto más fina, el borde no podrá ejercer mucha fuerza sobre el modelo para mantenerlo abajo contra el efecto del [alabeo](../troubleshooting/warping.md).