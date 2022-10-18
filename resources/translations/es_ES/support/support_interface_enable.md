Habilitar la interfaz de soporte
====
Una "interfaz de soporte" es una estructura intermedia entre el soporte normal y el modelo. Esta estructura puede ajustar las propiedades de cómo el soporte interactúa con el modelo sin afectar mucho a la mayor parte del soporte.

<!--screenshot {
"image_path": "support_interface_enable.png",
"models": [{"script": "trash_bin_lid.scad"}],
"camera_position": [93, 188, 87],
"settings": {
    "support_enable": true,
    "support_interface_enable": true
},
"colours": 64
}-->
![La interfaz de soporte se muestra en un tono más oscuro de azul](../images/support_interface_enable.png)

Por defecto, las capas de la interfaz son más densas que el soporte normal. Esto consigue una mejor superficie de voladizo sin necesidad de mucho material extra y tiempo de impresión. Sin embargo, será más difícil quitar el soporte.

La interfaz del soporte también puede imprimirse con un extrusor diferente al del resto del soporte. Algunos materiales destinados a la impresión del soporte pueden ser muy caros y lentos de imprimir. De esta manera, la mayor parte del soporte se sigue imprimiendo con el material más barato o más rápido, pero la interfaz donde se materializa el uso del soporte se imprime con el material más elegante.