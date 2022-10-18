Modo de superficie
====
Normalmente, Cura creará secciones transversales de todos los triángulos de su malla. Estos segmentos de línea se cosen juntos para formar bucles. Cualquier bucle que no esté cerrado será descartado.

Este ajuste controla lo que se hará con estos bucles no cerrados. Si se ajusta a "Normal", se descartan. Si se ajusta a "Superficie", todas las secciones transversales se imprimen como contornos. Si se ajusta a "Ambos", los contornos cerrados se imprimen normalmente, pero los no cerrados se imprimen por separado como paredes adicionales.

<!--screenshot {
"image_path": "magic_mesh_surface_mode_normal.png",
"models": [{"script": "extra_surface.py"}],
"camera_position": [66, 129, 124],
"settings": {
    "magic_mesh_surface_mode": "normal"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "magic_mesh_surface_mode_surface.png",
"models": [{"script": "extra_surface.py"}],
"camera_position": [66, 129, 124],
"settings": {
    "magic_mesh_surface_mode": "surface"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "magic_mesh_surface_mode_both.png",
"models": [{"script": "extra_surface.py"}],
"camera_position": [66, 129, 124],
"settings": {
    "magic_mesh_surface_mode": "both"
},
"colours": 32
}-->
![El modo normal deja fuera la única superficie no cerrada de la derecha](../images/magic_mesh_surface_mode_normal.png)
![El modo superficie sólo imprime las superficies sin tratarlas como volúmenes cerrados](../images/magic_mesh_surface_mode_surface.png)
![Imprimiendo tanto los volúmenes como la superficie extra no cerrada de la derecha](../images/magic_mesh_surface_mode_both.png)

Las superficies extra que se imprimen sólo incluirán las superficies verticales como líneas simples. No hay técnica de relleno para las superficies horizontales, ya que las superficies no son polígonos cerrados. No se pueden rellenar ya que no tienen interior. No puede haber partes superiores, inferiores, rellenos o soportes. Sólo líneas simples.

Las superficies adicionales se imprimirán como si fueran paredes exteriores, por lo que se verán afectadas por la velocidad de impresión de las paredes exteriores, el ancho de línea, etc. También imprimirá estas superficies utilizando una línea centrada precisamente en la superficie, en lugar de alinear la línea a lo largo del interior del modelo. Esto significa que se extiende con medio ancho de línea a cada lado de la superficie. Esto ocurre porque es ambiguo qué lado de la superficie es el interior del modelo. Su impresión no será dimensionalmente precisa. Si, como en la captura de pantalla anterior, la superficie extra está alineada con una superficie normal y sólida, y está utilizando la opción "Ambos" para completar las paredes que faltan, entonces las capas no se alinearán correctamente.

**Si imprimes tanto los volúmenes normales como las superficies extra, ten en cuenta que los volúmenes se imprimirán con la pared exterior completamente dentro del volumen. Las superficies extra se imprimen con la línea centrada en la superficie, con la mitad del ancho de la línea a cada lado. Si una superficie extra se alinea con la superficie de un volumen cerrado, como en las imágenes anteriores, la superficie se desplazará medio ancho de línea. Al fin y al cabo, la superficie extra no tiene un interior hacia el que desplazarse.**
