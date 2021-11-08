Realitvwert der Z-Naht
====
Wenn die Naht gemäß der Einstellung [Justierung der Z-Naht](z_seam_type.md) an einer benutzerdefinierten Stelle platziert wird, können Sie Koordinaten für die Position der Naht eingeben. Normalerweise geben diese Koordinaten eine Stelle auf der Bauplatte an, z. B. die Rückseite des Druckers. Wenn diese Einstellung aktiviert ist, werden diese Koordinaten relativ zur Position des Modells genommen.

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
![Deaktiviert: Die Koordinaten zeigen auf eine absolute Position in der Mitte der Bauplatte, so dass alle weißen Streifen in die Mitte zeigen](../../../articles/images/z_seam_relative_disabled.png)
![Aktiviert: Die Koordinaten sind relativ zum Modell, so dass jedes Modell die weißen Streifen in der gleichen Ecke hat.](../../../articles/images/z_seam_relative_enabled.png)

Wenn ein Mesh auf der Bauplatte dupliziert wird, bewirkt diese Einstellung, dass die Naht für jedes der Duplikate genau an der gleichen Stelle positioniert wird, anstatt dass sie auf den gleichen Punkt auf der Bauplatte zeigen. Auf diese Weise können Sie jedes Exemplar unabhängig von seiner Position auf der Bauplatte auf genau dieselbe Weise drucken.