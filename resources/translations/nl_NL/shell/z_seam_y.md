Z-naad Y
====
Wanneer de positie van de naad is ingesteld op "Aangepast" in de [Uitlijning Z-naad](z_seam_type.md) instelling, komt de naad dicht bij die met de [Z-naad X](z_seam_x.md) en Z Seam instellingen Y gespecificeerd positie.

<!--screenshot {
"image_path": "z_seam_y_back.png",
"modellen": [
    {
        "script": "rod_holder.scad",
        "transformatie": ["roterenZ(-90)"]
    }
],
"camerapositie": [0, -77, 130],
"instellingen": {
    "z_seam_type": "terug",
    "z_seam_position": "terug"
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "z_seam_y_front.png",
"modellen": [
    {
        "script": "rod_holder.scad",
        "transformatie": ["roterenZ(-90)"]
    }
],
"camera_positie": [0, 77, 130],
"instellingen": {
    "z_seam_type": "terug",
    "z_seam_position": "voorkant"
},
"kleuren": 64
}-->
![De naad zit aan de voorkant](../../../articles/images/z_seam_y_front.png)
![De naad zit aan de achterkant](../../../articles/images/z_seam_y_back.png)

Deze instelling specificeert een absolute positie op de platform wanneer [Relatieve Z-naad](z_seam_relative.md) is uitgeschakeld, of een positie ten opzichte van het midden van het model wanneer Z Seam Relatief is ingeschakeld. Als de positie absoluut is, bevindt de coördinaat zich in het g-code-coördinatensysteem, dat verschilt van de coördinaten die Cura weergeeft voor objectplaatsing.

Het is logisch om een plek voor de naad te kiezen die nauwelijks zichtbaar is wanneer je print wordt gemaakt. Als zo'n plek niet beschikbaar is of na het printen kan worden bewerkt, kun je de naad op een plek printen waar deze gemakkelijk met een mes kan worden afgesneden of geschuurd.