Minimale Breedte Conische Supporttructuur
====
Wanneer conische support is ingeschakeld en de supportsstructuur moet krimpen, bepaalt deze instelling de minimale breedte waartoe conische support de support zal verkleinen. De support wordt niet dunner tenzij het overhangende gebied dat support nodig heeft, al dunner wordt.

<!--screenshot {
"image_path": "support_conical_enabled.png",
"modellen": [
    {
        "script": "wide_overhang.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [91, -95, 19],
"instellingen": {
    "support_enable": waar,
    "support_conical_enabled": waar,
    "support_conical_angle": 30
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_conical_min_width_20.png",
"modellen": [
    {
        "script": "wide_overhang.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [91, -95, 19],
"instellingen": {
    "support_enable": waar,
    "support_conical_enabled": waar,
    "support_conical_angle": 30,
    "support_conical_min_width": 20
},
"kleuren": 64
}-->
![Een minimale breedte van 5 mm](../../../articles/images/support_conical_enabled.png)
![Een minimale breedte van 20 mm](../../../articles/images/support_conical_min_width_20.png)

Wanneer een groot volume support op een kleine supportpijler rust, is die support erg gevoelig voor kantelen. Verhoging van de minimale breedte vergroot de breedte van de basiskolom van de support die de kegel kan vastgrijpen. Dit verhoogt de betrouwbaarheid van de print, maar kost extra materiaal. Al met al zal de conische support minder effectief zijn in het verminderen van de printtijd.