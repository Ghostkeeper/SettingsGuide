Direcciones de la línea superior/inferior
====
Este ajuste le permite cambiar la dirección en la que se imprimen las líneas de la parte superior e inferior. Puede especificar una lista de ángulos separados por comas (en grados), y las líneas alternarán las direcciones por capa.

<!--screenshot {
"image_path": "skin_angles.gif",
"models": [
    {
        "script": "microwave_hook.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 48, 70],
"settings": {"skin_angles": "[0, 60, 120]"},
"layer": [76, 77, 78],
"colours": 128
}-->
![Patrón de líneas con ángulos de 0°, 60° y 120° alternados](../images/skin_angles.gif)

Por defecto, el patrón de líneas se imprime en las dos direcciones diagonales. Para los sistemas de pórtico cartesiano esto es lo más preciso, porque la impresora puede utilizar los motores X e Y para acelerar la boquilla al girar para la siguiente línea.

Puede haber varias razones para cambiar estas direcciones:
* Para conseguir un efecto óptico.
* Para optimizar la resistencia. La impresión será normalmente más resistente cuando se somete a empujes y tirones paralelos a las líneas de forro (y de relleno).
* Para reducir los salientes. Si una impresión es muy fina en una dirección, hacer que el forro haga de puente en esa dirección puede ser una forma eficaz de ahorrar material en el relleno. No será necesario el relleno para salvar el hueco. Del mismo modo, también puede elegir una dirección perpendicular al relleno para minimizar el voladizo sobre el relleno. De este modo se puede conseguir una mejor calidad de la superficie superior.
* Para optimizar la precisión si su impresora no tiene un motor para la dirección X y otro para la dirección Y, como una impresora con un pórtico en H o una impresora delta.

Se pueden introducir varios números para cambiar la dirección en cada capa. Por ejemplo, introducir `[0, 30, 60]` hace que se altere entre 0 grados de distancia del eje X, 30 grados de distancia y 60 grados de distancia.