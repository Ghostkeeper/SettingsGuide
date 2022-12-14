Brim vervangt de supportstructuur
====
Als deze instelling is ingeschakeld, blijft de brim het model onder de support volgen in plaats van rond de support te gaan. De drager wordt dan in de volgende laag over de brim geprint. Er zal nog steeds een brim rond de support worden geprint.

<!--screenshot {
"image_path": "brim_replaces_support_disabled.png",
"modellen": [{"script": "kasteel.scad"}],
"camerapositie": [0, 100, -136],
"instellingen": {
    "adhesion_type": "brim",
    "support_enable": waar,
    "brim_replaces_support": false
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "brim_replaces_support_enabled.png",
"modellen": [{"script": "kasteel.scad"}],
"camerapositie": [0, 100, -136],
"instellingen": {
    "adhesion_type": "brim",
    "support_enable": waar,
    "brim_replaces_support": true
},
"kleuren": 64
}-->
![Uitgeschakeld, de brim gaat om de support](../../../articles/images/brim_replaces_support_disabled.png)
![Ingeschakeld, de brim loopt onder de support](../../../articles/images/brim_replaces_support_enabled.png)

Door deze instelling in te schakelen, kan de brim het model beter volgen. Hierdoor wordt het model beter op de platvorm gehouden, waardoor kromtrekken wordt voorkomen.

In sommige gevallen vermindert dit de totale breedte van de brim voor sommige delen van de support. In deze gevallen ligt de support echter zo dicht bij het model dat de brim overgaat in het model, zodat hier nauwelijks hechtingsproblemen optreden.