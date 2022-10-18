Densidad Máxima del Relleno Esparcido del Puente
====
Si está imprimiendo con una densidad de relleno muy baja, la piel superior tiende a hundirse, causando [pillowing](../troubleshooting/pillowing.md) y, en general, superficies irregulares en la parte superior de la impresión. Opcionalmente, las técnicas de puenteo pueden aplicarse también a la piel superior. Este ajuste configura a qué velocidad de relleno se empezará a aplicar la técnica de puenteo.

<!--screenshot {
"image_path": "bridge_sparse_infill_max_density.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"layer": 108,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_sparse_infill_max_density": 100
},
"camera_position": [58, 27, 104],
"colours": 64
}-->
![La piel hace un puente sobre el relleno](../images/bridge_sparse_infill_max_density.png)

Este ajuste se configura como un umbral, para permitir que los perfiles contengan un único valor. Mientras el usuario ajusta la densidad de relleno todo el tiempo, el puente para la piel se activará o desactivará automáticamente.

El puenteado para la piel superior suele producir una superficie superior más suave con índices de relleno muy bajos. Sin embargo, asegúrese de que si se utiliza, hay suficientes [capas superiores] (../top_bottom/top_layers.md) para cerrar adecuadamente la superficie sin aplicar la técnica de puenteado en las capas más altas. La técnica de puente, especialmente con un [ancho de línea] reducido (bridge_skin_material_flow_3.md) no cerrará la superficie completamente. Si la piel superior no tiene suficientes capas, terminará con agujeros en la impresión y una resistencia comprometida.