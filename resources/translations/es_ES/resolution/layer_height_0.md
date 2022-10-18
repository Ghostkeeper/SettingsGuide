Altura de capa inicial
====
Este ajuste define el grosor de la primera capa de su impresión. La capa inicial se imprime normalmente más gruesa que el resto para crear una mayor adherencia con la placa de impresión. Con este ajuste, se puede aumentar el grosor de la capa inicial sin reducir la resolución del resto de la impresión.

<!--screenshot {
"image_path": "layer_height_0.png",
"models": [
    {
        "script": "rolling_blind_spacer.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [39, 28, 5],
"settings": {"layer_height_0": 0.3},
"colours": 32
}-->
![La capa inicial es más gruesa que el resto de las capas](../images/layer_height_0.png)

Aumentar el grosor de la capa inicial hace que la boquilla extruya más material en la misma distancia. Esto requiere una fuerza extra, ya que el material se extiende hacia los lados para llenar todo el ancho de la línea. Esta fuerza adicional hace que el material se adhiera mejor a la placa de impresión. Además, la capa más gruesa captará cualquier irregularidad en la planicidad de la superficie. Si la placa de impresión está ligeramente doblada, la variabilidad será absorbida por el grosor de la primera capa, mientras que de otro modo la boquilla podría rasparla en la segunda capa.

Tener una capa inicial demasiado gruesa hace que la primera capa se hunda más, lo que provoca patas de elefante. El ajuste [Expansión horizontal de la capa inicial](../shell/xy_offset_layer_0.md) puede evitar esto dándole un pequeño valor negativo.