Z-naadpositie
====
Als de positie van de naad is ingesteld op "Aangepast" in de instelling [Uitlijning Z-naad](z_seam_type.md), wordt de naad geplaatst in de richting gespecificeerd door de instelling.

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
![De naad zit aan de linkerkant](../../../articles/images/z_seam_x_left.png)
![De naad zit aan de achterkant](../../../articles/images/z_seam_y_back.png)
![De naad zit aan de rechterkant.](../../../articles/images/z_seam_x_right.png)
![De naad zit aan de voorkant](../../../articles/images/z_seam_y_front.png)

Er zijn acht verschillende richtingen beschikbaar voor de positie van de naad. Het is het beste om een ​​positie voor de naad te kiezen die moeilijk te zien is in het uiteindelijke object, dus het hangt sterk af van het ontwerp van uw model. Het is meestal het beste om een ​​positie van de naad te kiezen die zich in een binnenhoek bevindt, maar als zo'n hoek niet beschikbaar is, kunt u ook een positie kiezen die na het printen gemakkelijk met een mes kan worden weggesneden.

**De naad wordt zo dicht mogelijk bij de positie geplaatst die is opgegeven door de instellingen [Z-Naad X](z_seam_x.md) en [Z-Naad Y](z_seam_y.md). Dit is een eenvoudige instelling die de coördinaten intuïtiever instelt.**