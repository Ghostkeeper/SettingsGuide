Expansión horizontal de la interfaz del soporte
====
Este ajuste hace que la interfaz del soporte se expanda en todas las direcciones horizontalmente hacia el resto del soporte.

<!--screenshot {
"image_path": "support_interface_offset.png",
"models": [{"script": "f.scad"}],
"camera_position": [45, 45, 133],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_offset": 2,
    "support_interface_offset": 1
},
"colours": 64
}-->
![La interfaz de soporte se expande en el soporte](../images/support_interface_offset.png)

Hay dos casos de uso para este mecanismo.
* Si la interfaz de soporte termina directamente en el borde del voladizo que necesita ser soportado, el material de impresión puede hundirse sobre el borde. Hacer que la interfaz se expanda un poco más evitará esto.
* Algunos materiales típicamente utilizados para imprimir soporte con extrusión son malos a bajas velocidades de flujo o necesitan algún tiempo para ponerse en marcha. Las áreas pequeñas de la interfaz del soporte no encajan bien con esos materiales. Este ajuste puede literalmente hacer las áreas más grandes para que haya más espacio para extruir estos materiales.

Debido a limitaciones técnicas, la interfaz del soporte no puede ampliarse más allá del propio soporte.