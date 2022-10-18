Sin forro en huecos en Z
====
Si su modelo tiene una pequeña hendidura horizontal, más pequeña que el grosor del forro superior/inferior, este ajuste no se molesta en rellenar la parte superior e inferior por encima/debajo completamente con forro. Esto ahorra tiempo de corte e impresión, pero puede exponer el relleno al aire.

<!--screenshot {
"image_path": "skin_no_small_gaps_heuristic_disabled.png",
"models": [
    {
        "script": "small_z_gap.scad",
        "scad_params": ["gap_size=0.06"]
    }
],
"camera_position": [-21, -62, 25],
"settings": {
    "wall_line_count": 0,
    "skin_no_small_gaps_heuristic": false
},
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_no_small_gaps_heuristic_enabled.png",
"models": [
    {
        "script": "small_z_gap.scad",
        "scad_params": ["gap_size=0.06"]
    }
],
"camera_position": [-21, -62, 25],
"settings": {
    "wall_line_count": 0,
    "skin_no_small_gaps_heuristic": true
},
"colours": 32
}-->
![Normalmente hay forro alrededor de la pequeña hendidura horizontal](../images/skin_no_small_gaps_heuristic_disabled.png)
![Si está activado, no cierra correctamente el forro](../images/skin_no_small_gaps_heuristic_enabled.png)

La intención principal de este ajuste es reducir el tiempo de corte. Este ajuste reduce efectivamente la resolución con la que Cura muestrea dónde debe colocarse el forro. Dependiendo de la forma del modelo, esto podría ahorrar entre un 5% y un 30% del tiempo de corte. También ahorrará tiempo de impresión si hay pequeños huecos, porque en lugar de piel imprimirá relleno.

Si el modelo no tiene huecos horizontales más pequeños que el grosor del forro, el único efecto será la reducción del tiempo de corte.

Si el modelo tiene tales huecos horizontales, habrá relleno expuesto en el hueco. Sin embargo, si el hueco es lo suficientemente pequeño, el voladizo hará que las paredes se hundan lo suficiente como para que no sea visible de todos modos.