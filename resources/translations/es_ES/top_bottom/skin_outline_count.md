Recuento de paredes adicionales de forro
====
Al imprimir la parte superior e inferior con el patrón de líneas, el borde exterior de las zonas de piel puede seguir imprimiéndose con unas líneas concéntricas. Esto es diferente a la impresión de una pared extra, porque la pared extra del forro también se pone entre el forro y el relleno.

<!--screenshot {
"image_path": "skin_outline_count_0.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 0},
"layer": 115,
"colours": 64
}-->
<!--screenshot {
"image_path": "skin_outline_count_2.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 2},
"layer": 115,
"colours": 64
}-->
![Sin contornos de forro adicionales](../images/skin_outline_count_0.png)
![Dos líneas de forro adicionales](../images/skin_outline_count_2.png)

Normalmente las líneas de forro pueden terminar dentro del relleno disperso. Sus puntos finales se hundirán un poco entonces. Si hay paredes de forro adicionales, la impresora imprimirá primero un perímetro alrededor del forro al que se pueden unir las líneas de forro normales. Entonces la piel no se combará tanto en los puntos finales. Al final, esto tiende a mejorar un poco la calidad de las superficies superiores.