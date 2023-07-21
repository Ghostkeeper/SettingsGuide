Relatieve Z-naad
====
Als de naad op een aangepaste locatie wordt geplaatst volgens de instelling [Uitlijning Z-naad](z_seam_type.md), kunt u coördinaten invoeren voor de locatie van de naad. Meestal geven deze coördinaten een locatie op de platform aan, b.v. de achterkant van de printer. Als deze instelling is geactiveerd, worden deze coördinaten genomen ten opzichte van de positie van het model.

<!--screenshot {
"image_path": "z_seam_relative_disabled.png",
"modellen": [
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(-30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(30)", "translateY(20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(-30)", "translateY(20)"]
    },
    {
        "script": "cilinder.scad",
        "transformatie": ["schaal(0.25)"]
    }
],
"camerapositie": [0, 0, 250],
"instellingen": {
    "z_seam_type": "terug",
    "z_seam_x": 500,
    "z_seam_y": 500,
    "z_seam_relative": false
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "z_seam_relative_enabled.png",
"modellen": [
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(-30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(30)", "translateY(-20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(30)", "translateY(20)"]
    },
    {
        "script": "rod_holder.scad",
        "transformatie": ["translateX(-30)", "translateY(20)"]
    },
    {
        "script": "cilinder.scad",
        "transformatie": ["schaal(0.25)"]
    }
],
"camerapositie": [0, 0, 250],
"instellingen": {
    "z_seam_type": "terug",
    "z_seam_x": 500,
    "z_seam_y": 500,
    "z_seam_relative": waar
},
"kleuren": 64
}-->
![Uitgeschakeld: de coördinaten wijzen naar een absolute positie in het midden van de platform, dus alle witte strepen wijzen naar het midden](../../../articles/images/z_seam_relative_disabled.png)
![Ingeschakeld: De coördinaten zijn relatief ten opzichte van het model, dus elk model heeft de witte strepen in dezelfde hoek.](../../../articles/images/z_seam_relative_enabled.png)

Wanneer een mesh op de platform wordt gedupliceerd, zorgt deze instelling ervoor dat de naad voor elk van de duplicaten op exact dezelfde plaats wordt geplaatst, in plaats van naar hetzelfde punt op de platform te wijzen. Hierdoor kunt u elk exemplaar op exact dezelfde manier printen, ongeacht de positie op de platform.