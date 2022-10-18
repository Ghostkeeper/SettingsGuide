Habilitar techo del soporte
====
El techo del soporte es una estructura intermedia entre el soporte y el modelo, donde el modelo se apoya en el soporte. Se puede utilizar para proporcionar más o mejor soporte para el modelo sin afectar significativamente el tiempo de impresión. El techo del soporte suele imprimirse con mayor densidad o más lentamente.

<!--screenshot {
"image_path": "support_roof_enable.png",
"models": [{"script": "f3.scad"}],
"camera_position": [0, 134, 20],
"settings": {
    "support_enable": true,
    "support_roof_enable": true
},
"colours": 64
}-->
![El techo del soporte está coloreado en un tono más oscuro de azul](../images/support_roof_enable.png)

Por defecto, el techo del soporte es más denso que el soporte normal. Esto proporciona un voladizo de mejor calidad, ya que el modelo no necesita salvar grandes distancias. Sin embargo, será mucho más difícil quitar el soporte.

El techo del soporte también puede imprimirse con un extrusor diferente al del resto del soporte. Algunos materiales destinados a la impresión del soporte pueden ser muy caros y lentos de imprimir. De esta manera, la mayor parte del soporte se sigue imprimiendo con el material más barato o más rápido, pero el techo donde se materializa el uso del soporte se imprime con el material más elegante.