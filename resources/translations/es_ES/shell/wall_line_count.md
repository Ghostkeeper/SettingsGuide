Recuento de líneas de pared
====
Este ajuste determina cuántos contornos se dibujarán alrededor de la impresión en cada capa.

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
![Dos paredes](../images/wall_thickness_0.8.png)
![Cuatro paredes](../images/espesor_de_pared_1.6.png)

Sólo una de las paredes será una pared exterior, imprimiéndose con la configuración de la pared exterior. El resto de las paredes se imprimirán con la configuración de la pared interior.

El número de paredes es un factor importante en la fuerza de la impresión. Dado que las paredes son adyacentes, pueden reforzarse mutuamente, dando lugar a una parte más fuerte. Para impresiones más grandes, esto puede ser una manera mucho más efectiva de obtener un objeto fuerte que ajustando el relleno, dependiendo de la forma.

Aumentar el número de paredes hará:
Aumentar el número de paredes: * Aumentar en gran medida la fuerza de la impresión.
* Reducir el efecto de brillo donde el patrón de relleno es visible en el exterior.
* Mejorar los voladizos, ya que las líneas de las paredes suelen estar más orientadas hacia su punto de apoyo más cercano.
* Hacer que el modelo sea más hermético.
* Aumentar en gran medida el tiempo de impresión y el uso de material de la impresión.