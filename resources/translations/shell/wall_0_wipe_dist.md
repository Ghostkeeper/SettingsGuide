Distancia de pasada de la pared exterior
====
Con este ajuste, al final de cada pared exterior, la boquilla se desplazará un poco más sin extrusión, limpiando el contorno cerrado.

<!--screenshot {
"image_path": "wall_0_wipe_dist.png",
"models": [
    {
        "script": "thin_cylinder.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 0, 50],
"settings": {
    "wall_0_wipe_dist": 4
},
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"minimum_layer": 2,
"layer": 2,
"colours": 16
}-->
![Un pequeño desplazamiento después de completar la pared exterior](../images/wall_0_wipe_dist.png)

El objetivo de esta función es reducir la visibilidad de la costura. Cuando la pared se completa normalmente, el cordón sigue estando ligeramente por detrás de la boquilla. Este pequeño movimiento de desplazamiento conecta el cordón con el inicio del contorno, de modo que la costura se cierra.

La costura seguirá siendo visible, pero el resultado debería ser ligeramente mejor con una pequeña distancia de barrido. Aumentar demasiado este ajuste no tiene más efecto, ya que la boquilla se desplaza más allá de la costura, y puede causar algo de subextrusión más tarde, ya que la cámara de la boquilla se vacía rezumando en la pared exterior.

Este efecto es básicamente el opuesto al de [depósito por inercia](../experimental/coasting_enable.md), que detendrá la extrusión ligeramente antes de terminar el contorno.