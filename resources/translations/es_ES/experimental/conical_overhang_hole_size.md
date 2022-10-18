Superficie máxima de los agujeros en voladizo
====
Debido a que [Hacer imprimible el voladizo](conical_overhang_enabled.md) elimina cualquier tipo de voladizo, cualquier puente se bajará automáticamente, cerrando el voladizo debajo de él. Sin embargo, si el voladizo está cerrado por todos los lados, seguirá bajando hasta que el voladizo cerrado se llene por completo. Efectivamente, cualquier agujero orientado hacia abajo se llenará completamente, incluso si el voladizo que necesita ser eliminado es sólo un pequeño punto en la parte superior.

Para evitar este efecto, este ajuste permite que el voladizo permanezca abierto si está cerrado por todos los lados y es más pequeño que un área determinada. Esto sólo se aplica a los agujeros. El voladizo normal en el exterior del modelo se sigue extendiendo hacia abajo para mantener un ángulo razonablemente imprimible.

<!--screenshot {
"image_path": "conical_overhang_hole_size.png",
"models": [{"script": "plopper.scad"}],
"camera_position": [-86, 29, -85],
"settings": {
    "conical_overhang_enabled": true,
    "conical_overhang_hole_size": 20
},
"colours": 64
}-->
![Se permite que un pequeño punto en la parte superior sobresalga, para que este agujero no se llene](../images/conical_overhang_hole_size.png)

En la mayoría de los modelos es bastante seguro fijar este ajuste a varias decenas de milímetros cuadrados. Si se establece demasiado bajo, el modelo se modificará más, para soportar voladizos que son realmente demasiado pequeños para necesitar ningún apoyo. Sin embargo, si se fija demasiado alto, habrá zonas de voladizo importantes que podrían ser difíciles de salvar.

Si hay grandes áreas de voladizo debido a esta configuración, es una buena idea mirar primero en [afinar el puente](bridge_settings_enabled.md) antes de tratar de modificar el modelo para eliminar el voladizo.