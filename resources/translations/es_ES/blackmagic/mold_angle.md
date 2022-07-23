Ángulo del molde
====
Similar a la función [Make Overhang Printable](../experimental/conical_overhang_enabled.md), este ajuste modifica la forma de los moldes para que pueda imprimirse sin soporte. Sólo se modifica la forma exterior del molde, por lo que la forma de su molde no se verá afectada.

<!--screenshot {
"image_path": "mold_angle.png",
"models": [
    {
        "script": "star_podium.scad",
        "transformation": ["mirrorZ"]
    }
],
"camera_position": [81, 129, 45],
"settings": {
    "mold_enabled": "True"
},
"colours": 48
}-->
![Un ángulo de 40 grados permite que la parte inferior de este molde se imprima sin necesidad de soporte](../images/mold_angle.png)

Si se reduce este ángulo, se reducirá el extremo de los voladizos. Esto hará que la impresión sea más fiable. Sin embargo, también hará que la base de la impresión sea más ancha, lo que aumenta considerablemente la duración de la impresión y aumenta la cantidad de material que utilizará.

Para algunas formas, modificar la forma exterior del molde no es suficiente para que se imprima correctamente. Seguirá necesitando soporte. Puede conseguir un efecto similar activando [Soporte cónico](../experimental/support_conical_enabled.md).

<!--screenshot {
"image_path": "mold_needs_support.png",
"models": [{"script": "basic_overhang.scad"}],
"camera_position": [20, 183, 97],
"settings": {
    "mold_enabled": "True"
},
"colours": 32
}-->
![Este molde aún necesita soporte](../images/mold_needs_support.png)