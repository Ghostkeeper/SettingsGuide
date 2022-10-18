Imagen de Densidad de Relleno Cruzado para Soporte
====
En este ajuste, puede proporcionar una imagen que especifique la densidad en varios lugares del soporte. La densidad del soporte variará en ciertos lugares dependiendo del brillo de la imagen. Esto sólo funciona para el [Patrón cruzado](../soporte/patrón_soporte.md), ya que ese patrón es capaz de ajustar su densidad sin cortar las líneas, lo que daría lugar a un flujo interrumpido y a una fuerza reducida.

<!--screenshot {
"image_path": "cross_support_density_image.png",
"models": [{"script": "wide_bridge.scad"}],
"camera_position": [0, 0, 120],
"layer": 79,
"settings": {
    "support_enable": true,
    "support_pattern": "cross",
    "support_infill_rate": 100,
    "cross_support_density_image": "{root}/resources/articles/images/cross_support_density_image_mask.png"
},
"colours": 32
}-->
![La densidad de apoyo es mayor en los lados](../images/cross_support_density_image.png)
![El archivo de imagen utilizado para crear ese patrón](../images/cross_support_density_image_mask.png)

La ruta de la imagen se proporciona como una ruta local, por ejemplo `C:\Projects\3D Printing\support_density.png` en Windows o `/home/ghostkeeper/3d_printing/support_density.png` en Unix. Los formatos de archivo admitidos son JPG, PNG, TGA, BMP, PSD, GIF, HDR y PIC. La imagen se escala sobre la impresión de forma que se ajuste exactamente a la caja delimitadora de la escena impresa. El brillo de la imagen determina la densidad del soporte:
* Cuando la imagen es negra, se utiliza la [densidad de soporte](../support/support_infill_rate.md).
* Si la imagen es blanca, la densidad de apoyo se aproximará al 0%.

La densidad de soporte nunca superará el valor especificado por la [distancia de la línea de soporte](../support/support_line_distance.md). Sólo puede reducirse. El patrón también está limitado en cuanto a dónde puede reducir su densidad. Aunque intenta aproximarse lo más posible a la densidad de soporte deseada, esto no siempre es posible. Si la densidad del soporte es realmente baja, habrá muy pocas oportunidades de ajustar la densidad del soporte, lo que hará que la impresión siga la imagen de forma muy floja. En los lugares donde la densidad del soporte es alta, la imagen se seguirá muy de cerca. La densidad elegida también está muy cuantificada. La densidad sólo puede duplicarse o reducirse a la mitad, pero Cura [dither](https://en.wikipedia.org/wiki/Dither) el patrón para lograr una mayor precisión efectiva.

Con este ajuste, puede personalizar mucho su soporte. Si ciertas partes de su impresión son propensas a la flacidez o necesitan ser impresas con mucha precisión, puede aumentar localmente la densidad allí para apoyarlas mejor, sin tener que tomar un gran golpe en el tiempo de impresión o hacer más difícil sacar el apoyo.  

**Esta configuración no se transferirá bien a través de los archivos de proyecto de Cura. El archivo de proyecto almacenará la ruta de acceso a la imagen como valor de ajuste, pero no almacenará la imagen. Si el archivo de proyecto se abre en un ordenador diferente, la imagen de densidad probablemente no se restaurará.**