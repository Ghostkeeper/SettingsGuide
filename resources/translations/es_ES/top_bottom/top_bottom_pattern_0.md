Capa inferior de la capa inicial
====
Este ajuste configura el patrón que se utilizará para la parte inferior del modelo donde se apoya directamente en la placa de impresión o en la balsa. El patrón para esta capa se configura por separado del resto de las capas inferiores.

<!--screenshot {
"image_path": "top_bottom_pattern_0.gif",
"models": [
    {
        "script": "gear_hollow.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [40, -40, 110],
"settings": {"top_bottom_pattern_0": "concentric"},
"layer": [1, 2, 3],
"colours": 64
}-->
![La capa inicial se imprime con un patrón concéntrico, pero el resto es el patrón de líneas](../images/top_bottom_pattern_0.gif)

El patrón concéntrico tiende a adherirse mucho mejor a la plataforma de impresión que otros patrones, porque la tensión de las líneas cuando se contraen se reparte en todas las direcciones. Esto evita la deformación y mejora la fiabilidad de la impresión. Otros patrones se contraen en una sola dirección.

Cuando se imprime con una balsa, el uso del patrón de líneas tiende a dar una pieza ligeramente más fuerte. Además, las líneas se orientan de forma que salvan bien los espacios entre las líneas de la balsa, creando una parte inferior más lisa.