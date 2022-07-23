Expansión horizontal del soporte
====
Este ajuste hace que el soporte se ensanche ligeramente, expandiéndose horizontalmente en todas las direcciones.

<!--screenshot {
"image_path": "support_offset.png",
"models": [{"script": "duct.scad"}],
"camera_position": [47, 72, 128],
"settings": {
    "support_enable": true,
    "support_offset": 1.6
},
"colours": 64
}-->
![El soporte es más ancho de lo necesario para soportar el modelo](../images/support_offset.png)

Este ajuste tiene múltiples usos, dependiendo del material utilizado para el soporte y el tipo de modelo que necesita apoyo:
* Aumentar este ajuste hará que el soporte sea más ancho y por lo tanto más robusto. Esto es útil para los modelos altos con pequeñas áreas de voladizo, ya que el voladizo de otro modo se apoyaría con un pilar de soporte muy alto y delgado. Con un poco de expansión horizontal, se convierte en un pilar de soporte muy alto pero ligeramente más ancho.
* El aumento de este ajuste también funciona como una medida de seguridad para asegurarse de que las áreas de soporte tienen una cierta área mínima. Esto es necesario para los materiales que son difíciles de extruir, como el PVA.
* Reducir este ajuste reducirá el uso de material y el tiempo de impresión del soporte. Aumentarlo incrementará el material requerido y el tiempo de impresión, por supuesto. Vea también la función [soporte cónico](../experimental/support_conical_enabled.md), que reduce el ancho del soporte sin comprometer el área que éste soporta.
* Configurar este ajuste a un valor negativo también puede eliminar por completo los pilares delgados del soporte. Si ese soporte no se imprimiría de todos modos, puede ser mejor dejarlo fuera por completo. Un método para eliminar el soporte sin comprometer la calidad del voladizo del resto del modelo es la herramienta de bloqueo de soporte.