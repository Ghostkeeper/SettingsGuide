Costuras relativas en Z
====
Cuando la costura se coloca en una ubicación especificada por el usuario de acuerdo con el ajuste [Alineación de la costura en Z](z_seam_type.md), se pueden introducir coordenadas para el lugar donde debe situarse la costura. Normalmente esas coordenadas especifican alguna ubicación en la placa de impresión, como la parte trasera de la impresora. Si este ajuste está activado, esas coordenadas se tomarán en relación con la posición del modelo.

<!--screenshot {
"image_path": "z_seam_relative_disabled.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(-30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(30)", "translateY(20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(-30)", "translateY(20)"]
    },
    {
        "script": "cylinder.scad",
        "transformation": ["scale(0.25)"]
    }
],
"camera_position": [0, 0, 250],
"settings": {
    "z_seam_type": "back",
    "z_seam_x": 500,
    "z_seam_y": 500,
    "z_seam_relative": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "z_seam_relative_enabled.png",
"models": [
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(-30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(30)", "translateY(20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformation": ["translateX(-30)", "translateY(20)"]
    },
    {
        "script": "cylinder.scad",
        "transformation": ["scale(0.25)"]
    }
],
"camera_position": [0, 0, 250],
"settings": {
    "z_seam_type": "back",
    "z_seam_x": 500,
    "z_seam_y": 500,
    "z_seam_relative": true
},
"colours": 64
}-->
![Desactivado: Las coordenadas apuntan a una posición absoluta en el centro de la placa de construcción, por lo que todas las rayas blancas apuntan hacia el centro](../images/z_seam_relative_disabled.png)
![Habilitado: Las coordenadas son relativas al modelo, por lo que todos los modelos tendrán las rayas blancas en la misma esquina](../images/z_seam_relative_enabled.png)

Cuando se duplica una malla en la placa de impresión, este ajuste hace que la costura se sitúe exactamente en el mismo lugar para cada uno de los duplicados, en lugar de que apunten hacia el mismo punto de la placa de impresión. Esto le permite imprimir cada copia exactamente de la misma manera, independientemente de sus posiciones en la placa de construcción.