Densidad de la piel del puente
====
Este ajuste controla la densidad de la parte inferior de la impresión donde se hace un puente. Con una densidad del 100%, las líneas se colocan directamente adyacentes. A densidades más bajas, las líneas están más separadas.

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
<!--screenshot {
"image_path": "bridge_skin_density_50.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 50,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![Con una densidad del 100%, las líneas se sitúan directamente junto a otras](../images/bridge_skin_density_100.png)
![Con una densidad del 50%, hay cierto espacio entre las líneas](../images/bridge_skin_density_50.png)

Hay dos efectos principales en juego cuando se ajusta esta configuración: La adhesión entre líneas y el enfriamiento.

Cuando se espacian las líneas de piel directamente adyacentes entre sí, se pegarán unas a otras. Esto hará que la parte inferior del hueco puenteado tenga un aspecto más bonito, ya que la superficie será continua en lugar de encordada. Además, la segunda línea puede apoyarse un poco en la primera mientras hace el puente, lo que hace que el puente se hunda un poco menos.

Sin embargo, hay otro efecto: el enfriamiento. Cuando las líneas están más separadas, pueden enfriarse más rápido y entonces tampoco se comban tanto. Por supuesto, esto sólo se aplica cuando el ventilador está encendido, así que para los materiales de alta temperatura esta estrategia no va a funcionar.

Cuál de estos efectos es más fuerte depende de la viscosidad del material, de lo rápido que se solidifique y de la velocidad del ventilador. Siempre es necesario hacer algún tipo de ajuste.

**Si el [Flujo de la piel del puente](bridge_skin_material_flow.md) es inferior al 100%, también habrá algún espacio entre las líneas aunque la densidad sea del 100%, porque las líneas serán más finas entonces.**