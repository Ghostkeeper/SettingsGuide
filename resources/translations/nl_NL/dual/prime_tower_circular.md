Circulaire Prime Tower
====
Als deze instelling is ingeschakeld, krijgt de prime-toren de vorm van een cilinder. Als het is uitgeschakeld, is de hoofdtoren vierkant.

<!--screenshot {
"image_path": "prime_tower_circular_enabled.png",
"modellen": [
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 0
        }
    },
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 1
        },
        "transformatie": ["translateX(40)"]
    }
],
"camerapositie": [470, -384, 150],
"camera_lookat": [470, -470, 5],
"instellingen": {
    "prime_tower_enable": waar,
    "prime_tower_min_volume": 3
},
"kleuren": 16
}-->
![Vierkante primepijler](../../../articles/images/prime_tower_circular_disabled.png)
![Ronde primepijler](../../../articles/images/prime_tower_circular_enabled.png)

In beide gevallen is de hoofdtoren nog steeds hol. De ronde prime-toren is strikt kleiner dan de vierkante prime-toren (omdat de hoeken zijn afgesneden). Het [Minimumvolume primepijler](prime_tower_min_volume.md) zal nog steeds correct zijn.

Als het materiaal de neiging heeft om te kromtrekken, heeft de vierkante prime-toren vier hoeken die los kunnen komen van de platvorm. Hierdoor is de kans groter dat hij omvalt, in vergelijking met de ronde prime-toren. Er zijn ook grotere versnellingen betrokken bij het printen van een vierkante prime-toren. Deze versnellingen maken de doorvoer inconsistent, en dat is niet wat je zou willen om het materiaal te primen.

De ronde prime-toren is in bijna elk aspect beter. Daarom wordt de instelling verwijderd in nieuwere versies van Cura. Die versies zullen altijd een ronde prime-toren hebben.