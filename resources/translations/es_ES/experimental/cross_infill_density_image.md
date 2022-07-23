Imagen de densidad de relleno transversal
====
En este ajuste, puede proporcionar una imagen que especifique la densidad en varios lugares a través del relleno. La densidad del relleno variará en ciertos lugares dependiendo del brillo de la imagen. Esto sólo funciona para el patrón [Cross (3D)](../infill/infill_pattern.md), ya que ese patrón es capaz de ajustar su densidad sin cortar las líneas, lo que daría lugar a un flujo interrumpido y una fuerza reducida.

<!--screenshot {
"image_path": "cross_infill_density_image.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross_3d",
    "infill_sparse_density": 101,
    "cross_infill_density_image": "{root}/resources/articles/images/cross_infill_density_image_mask.png"
},
"colours": 32
}-->
![La densidad de relleno varía a través del objeto](../images/cross_infill_density_image.png)
![El archivo de imagen utilizado para crear ese patrón](../images/cross_infill_density_image_mask.png)

La ruta de acceso a la imagen se proporciona como una ruta local, por ejemplo `C:\Projects\3D Printing\\density.png` en Windows o `/home/ghostkeeper/3d_printing/infill_density.png` en Unix. Los formatos de archivo admitidos son JPG, PNG, TGA, BMP, PSD, GIF, HDR y PIC. La imagen se escala sobre el objeto de manera que se ajuste exactamente al cuadro delimitador del objeto. El brillo de la imagen determina la densidad del relleno:
* Cuando la imagen es negra, se utiliza la [densidad de relleno](../infill/infill_sparse_density.md).
* Si la imagen es blanca, la densidad de relleno se acercará al 0%.

La densidad de relleno nunca superará el valor especificado por la [distancia de línea de relleno](../infill/infill_line_distance.md). Sólo puede reducirse. El patrón también está limitado en cuanto a dónde puede reducir su densidad. Aunque intenta aproximarse lo más posible a la densidad de relleno deseada, esto no siempre es posible. Si la densidad de relleno es realmente baja, habrá muy pocas oportunidades de ajustar la densidad de relleno, lo que hará que la impresión siga la imagen de forma muy imprecisa. En los lugares donde la densidad de relleno es alta, la imagen se seguirá muy de cerca. La densidad elegida también está muy cuantificada. La densidad sólo puede duplicarse o reducirse a la mitad, pero Cura [dither](https://en.wikipedia.org/wiki/Dither) el patrón para lograr una mayor precisión efectiva.

Con esta configuración, se puede personalizar mucho el relleno. Dado que los patrones de Relleno Cruzado tienen la mayor parte de su uso con materiales flexibles, este ajuste se utiliza para lograr restricciones muy específicas de suavidad o dureza. Por ejemplo, se podría imprimir una suela de zapato con una suavidad personalizada para que se adapte mejor a los pies, o un dispositivo mecánico que tenga que doblarse en partes específicas. 

**Esta configuración no se transferirá bien a través de los archivos de proyecto de Cura. El archivo de proyecto almacenará la ruta de acceso a la imagen como valor de ajuste, pero no almacenará la imagen. Si el archivo de proyecto se abre en un ordenador diferente, la imagen de densidad probablemente no se restaurará.**