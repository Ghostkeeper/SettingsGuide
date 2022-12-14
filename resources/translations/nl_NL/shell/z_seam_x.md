Z-naad X
====
Als de positie van de naad is ingesteld op "Aangepast" in de instelling [Uitlijning Z-naad](z_seam_type.md), wordt de naad gemaakt in de buurt van de positie die is ingesteld met de Z Seam X en [Z-naad Y](z_seam_y .md ) opgegeven positie.

<!--screenshot {
"image_path": "z_seam_x_left.png",
"modellen": [
    {
        "script": "rod_holder.scad",
        "transformatie": ["roterenZ(-90)"]
    }
],
"camerapositie": [-55, 128, 40],
"instellingen": {
    "z_seam_type": "terug",
    "z_seam_position": "links"
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "z_seam_x_right.png",
"modellen": [
    {
        "script": "rod_holder.scad",
        "transformatie": ["roterenZ(-90)"]
    }
],
"camerapositie": [55, 128, 40],
"instellingen": {
    "z_seam_type": "terug",
    "z_seam_position": "rechts"
},
"kleuren": 64
}-->
![De naad zit aan de linkerkant](../../../articles/images/z_seam_x_left.png)
![De naad zit aan de rechterkant.](../../../articles/images/z_seam_x_right.png)

Deze instelling specificeert een absolute positie op de platvorm wanneer [Relatieve Z-naad](z_seam_relative.md) is uitgeschakeld, of een positie ten opzichte van het midden van het model wanneer Z Seam Realism is ingeschakeld. Als de positie absoluut is, bevindt de coördinaat zich in het g-code-coördinatensysteem, dat verschilt van de coördinaten die Cura weergeeft voor objectplaatsing.

Het is logisch om een ​​plek voor de naad te kiezen die nauwelijks zichtbaar is wanneer je print wordt aangebracht. Als zo'n plek niet beschikbaar is of na het printen kan worden bewerkt, kun je de naad op een plek leggen waar deze gemakkelijk met een mes kan worden afgesneden of geschuurd.