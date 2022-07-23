Posición de costura en Z
====
Si la ubicación de la costura se establece como "especificada por el usuario" en el ajuste [Alineación de la costura en Z](z_seam_type.md), la costura se colocará en la dirección especificada por este ajuste.

<!--screenshot {
"image_path": "z_seam_x_left.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [-55, 128, 40],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "left"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_y_back.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [0, -77, 130],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "back"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_x_right.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [55, 128, 40],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "right"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_y_front.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["rotateZ(-90)"]
    }
],
"camera_position": [0, 77, 130],
"settings": {
    "z_seam_type": "back",
    "z_seam_position": "front"
},
"colours": 64
}-->
![La costura se encuentra en el lado izquierdo](../images/z_seam_x_left.png)
![La costura se encuentra en la parte trasera](../images/z_seam_y_back.png)
![La costura se encuentra en el lado derecho](../images/z_seam_x_right.png)
![La costura está situada en la parte delantera](../images/z_seam_y_front.png)

Hay ocho direcciones ordinales disponibles para la posición de la costura. Es mejor elegir una ubicación para la costura que sea difícil de ver en el objeto final, por lo que depende en gran medida del diseño de su modelo. Normalmente es mejor elegir una posición de la costura que esté en una esquina interior, pero si dicha esquina no está disponible también puede elegir una posición que sea fácil de cortar con un cuchillo después de la impresión.

**La costura se coloca lo más cerca posible de la posición indicada por los ajustes [X de la costura Z](z_seam_x.md) e [Y de la costura Z](z_seam_y.md). Este es un ajuste conveniente que establece esas coordenadas de manera más intuitiva.**