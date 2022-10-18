Tipo de adherencia de las placas de impresión
====
Hay tres tipos de adhesión de la placa de construcción: falda, borde y balsa. También puede desactivar fácilmente los tipos de adherencia estableciéndolos como Ninguno.

<!--screenshot {
"image_path": "adhesion_type_skirt.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 128, 53],
"settings": {"adhesion_type": "skirt"},
"colours": 64
}-->
<!--screenshot {
"image_path": "adhesion_type_brim.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 128, 53],
"settings": {"adhesion_type": "brim"},
"colours": 64
}-->
<!--screenshot {
"image_path": "adhesion_type_raft.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 128, 53],
"settings": {"adhesion_type": "raft"},
"colours": 64
}-->
![Falda](../images/adhesion_type_skirt.png)
![Borde](../images/adhesion_type_brim.png)
![Balsa](../images/adhesion_type_raft.png)

Falda
----
Una falda es una línea única que rodea su impresión. No contribuirá directamente a la adhesión de la placa. Sin embargo, si usted no quiere utilizar los otros métodos de adhesión, este método todavía sirve para dos funciones.
* Hace que su boquilla se cebe antes de comenzar la impresión de su modelo real, para asegurarse de que el material está fluyendo correctamente.
* Le permite ver si su placa de impresión está bien nivelada.

Borde
----
Un borde es un área plana de una sola capa alrededor de la base de su modelo. Su propósito es mantener los bordes de su impresión hacia abajo y hacer el área de contacto entre su impresión y la placa de construcción más grande.
* El área de superficie más grande permite que su impresión se adhiera mejor a la placa de construcción. Esto es útil para casi cualquier impresión de más de unos pocos centímetros.
* Este borde también mantendrá los bordes de su impresión hacia abajo. Los materiales que se encogen mucho al enfriarse (como el ABS) tienden a deformarse mucho durante la impresión. Tener un borde con suficiente anchura puede mantener las esquinas en su lugar, evitando este alabeo.

Balsa
----
Una balsa es una placa gruesa entre el modelo y la placa de construcción. Esta balsa protege su impresión del calor de la placa de construcción. También tendrá una gran superficie para pegarse a la placa de construcción. La impresión se pone encima de esta balsa, donde puede pegarse mucho mejor. Sin embargo, tenga cuidado con las impresiones finas, ya que puede ser difícil de quitar la balsa sin dañar la impresión.