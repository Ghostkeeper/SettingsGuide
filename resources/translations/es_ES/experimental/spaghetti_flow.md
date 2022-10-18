Flujo de espaguetis
====
Esta configuración ajusta directamente la densidad del relleno de espaguetis.

Normalmente, mientras se imprime el relleno, el ajuste [densidad de relleno](../relleno/infiltro_sparse_densidad.md) sólo afecta a la [distancia entre líneas de relleno](../relleno/infiltro_línea_distancia.md). Debido a que el [ancho de la línea de relleno](../resolution/infill_line_width.md) se mantiene igual pero las líneas están más espaciadas, el aumento de la densidad de relleno tiene el efecto de que una mayor parte del volumen de relleno se llena con material al final.

Esto funciona de forma diferente si se activa [spaghetti infill](spaghetti_infill_enabled.md). La distancia de la línea de relleno no sólo ajusta la distancia entre las líneas de relleno, sino que el ancho de la línea también se ajustará para lograr la densidad deseada según lo especificado por este ajuste. Este ajuste especifica exactamente la fracción del volumen total de relleno que se va a rellenar con material. Aumentar este ajuste hará que las líneas sean más anchas.

Cuando se utiliza el relleno de espagueti para producir un relleno flexible, este ajuste determina esencialmente lo rígido que va a ser el material de relleno. Reducir el flujo producirá un relleno más suave, mientras que aumentar el flujo hará que el relleno sea más rígido. Sin embargo, si se reduce demasiado el caudal, se impide que el relleno se extienda por igual. Tendrá tendencia a caer hacia el fondo del volumen y producirá montones de espaguetis que no aportarán rigidez a la parte superior. 

Cuando se utiliza el relleno de espaguetis para fundir material, este ajuste debería estar cerca del 100% con el fin de llenar el modelo completamente con material. Sin embargo, puede ajustarlo ligeramente si su material tiene una tendencia a encogerse o expandirse mientras se asienta.

**Este ajuste todavía se multiplica por el ajuste [infill flow](../material/infill_material_flow.md).