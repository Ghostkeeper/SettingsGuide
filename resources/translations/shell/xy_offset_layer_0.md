Expansión horizontal de la capa inicial
====
Este ajuste expande sólo la capa inicial que se apoya en la placa de construcción (o en la balsa). De forma similar a [Expansión Horizontal](xy_offset.md), un valor positivo hará que la capa inicial sea más ancha, mientras que un valor negativo encogerá la capa inicial.

<!--screenshot {
"image_path": "xy_offset_layer_0_original.png",
"models": [
    {
        "script": "d1.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"settings": {"xy_offset_layer_0": 0},
"colours": 16
}-->
<!--screenshot {
"image_path": "xy_offset_layer_0_enabled.png",
"models": [
    {
        "script": "d1.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"settings": {"xy_offset_layer_0": -0.6},
"colours": 16
}-->
![El modelo original](../images/xy_offset_layer_0_original.png)
![La capa inicial se encoge](../images/xy_offset_layer_0_enabled.png)

La capa inicial suele imprimirse en una placa de impresión calentada, lo que la mantiene en un estado ligeramente líquido para mejorar la adhesión a la placa de impresión. La capa inicial suele ser también mucho más gruesa que el resto de las capas. Esto permite que haya tiempo y material suficiente para que la capa se hunda lateralmente, creando un fenómeno llamado "pata de elefante" en el que la parte inferior de la impresión tiene un labio ligeramente más ancho. Este ajuste puede compensar la pata de elefante haciendo que la capa inicial sea más delgada de antemano. Dé a este ajuste un pequeño valor negativo para compensar la pata de elefante.

También puede dar a este ajuste un valor grande para crear un pseudo-borde alrededor de su impresión que se puede combinar con otras técnicas de adhesión como la balsa. Tenga en cuenta que esto hará que la piel se expanda también, por lo que habrá piel por debajo de las paredes de la segunda capa.

**Combinar esta configuración con un borde es ineficaz, ya que el borde producirá un gran borde alrededor de la capa inicial de todos modos.**