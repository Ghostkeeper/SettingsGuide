X de la Costura Z
====
Si la ubicación de la costura se establece como "Especificada por el usuario" en el ajuste [Alineación de la costura Z](z_seam_type.md), la costura se coloca cerca de la ubicación especificada con los ajustes de la X de la Costura Z e [Y de la Costura Z](z_seam_y.md).

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
![La costura se encuentra en el lado izquierdo](../images/z_seam_x_left.png)
![La costura se encuentra en el lado derecho](../images/z_seam_x_right.png)

Este ajuste indica una posición absoluta en la placa de impresión si [Costuras relativas en Z](z_seam_relative.md) está desactivado, o una posición relativa al centro del modelo si Costuras relativas en Z está activado. Cuando la posición es absoluta, la coordenada está en el sistema de coordenadas de g-code, que es diferente de las coordenadas que Cura muestra para la colocación de objetos.

Es útil elegir una ubicación para la costura que sea apenas visible en la aplicación de su impresión. Si no se dispone de tal ubicación o se puede hacer algún tipo de post-procesamiento después de la impresión, puede optar por colocar la costura en un lugar donde pueda ser fácilmente cortada con un cuchillo o lijada.