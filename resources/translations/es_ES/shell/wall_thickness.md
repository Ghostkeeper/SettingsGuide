Espesor de pared
====
Este ajuste determina el grosor de la pared alrededor de la impresión. En última instancia, ajusta el número de paredes interiores para conseguir el grosor deseado.

<!--screenshot {
"image_path": "wall_thickness_0.8.png",
"models": [
    {
        "script": "rotary_tumbler_lid.scad",
        "transformation": ["scale(0.4)"]
    }
],
"camera_position": [50, 50, 124],
"settings": {
    "skin_outline_count": 0,
    "wall_line_count": 2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "wall_thickness_1.6.png",
"models": [
    {
        "script": "rotary_tumbler_lid.scad",
        "transformation": ["scale(0.4)"]
    }
],
"camera_position": [50, 50, 124],
"settings": {
    "skin_outline_count": 0,
    "wall_line_count": 4
},
"colours": 32
}-->
![Paredes de 0,8 mm de grosor](../images/wall_thickness_0.8.png)
![Paredes de 1,6 mm de grosor](../images/wall_thickness_1.6.png)

El grosor de la pared debe ser un múltiplo del ancho de la línea de la pared. Si no lo es, se redondeará para que sea un múltiplo exacto. Tenga en cuenta que una de las paredes será una pared exterior, y el resto serán paredes interiores. Estas paredes pueden tener diferentes anchos de línea.

El grosor de las paredes es un factor importante para la solidez de la impresión. Dado que las paredes son adyacentes, pueden reforzarse mutuamente, dando lugar a una parte más fuerte. Para impresiones más grandes, esta puede ser una manera mucho más efectiva de obtener un objeto fuerte que ajustando el relleno, dependiendo de la forma.

Aumentar el grosor de la pared hará:
Aumentar el grosor de la pared: * Aumentar la fuerza de la impresión.
* Reducir el efecto de brillo donde el patrón de relleno es visible en el exterior.
* Mejorar los voladizos, ya que las líneas de la pared suelen estar más orientadas hacia su punto de apoyo más cercano.
* Hacer que el modelo sea más hermético.
* Aumentar en gran medida el tiempo de impresión y el uso de material de la impresión.