Plaatsing Supportstructuur
====
Met deze instelling kunt u aangeven waar de support geplaatst kan worden.

<!--screenshot {
"image_path": "support_type_everywhere.png",
"modellen": [{"script": "duct.scad"}],
"camerapositie": [56, 127, 60],
"instellingen": {
    "support_enable": waar,
    "support_type": "overal"
},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "support_type_touching_buildplate.png",
"modellen": [{"script": "duct.scad"}],
"camerapositie": [56, 127, 60],
"instellingen": {
    "support_enable": waar,
    "support_type": "platvorm"
},
"kleuren": 32
}-->
![support wordt gegenereerd voor alle overhangende oppervlakken](../../../articles/images/support_type_everywhere.png)
![support wordt alleen gegenereerd waar deze op de platvorm kan rusten](../../../articles/images/support_type_touching_buildplate.png)

Als de supporten ergens worden geplaatst, is het betrouwbaarder voor de support. Eventuele uitsteeksels die zouden doorzakken, worden goed ondersteund. De support kan echter ook een litteken achterlaten waar ze op het model rusten. Dit verslechtert de visuele kwaliteit en oppervlaktegladheid van het model nadat de support is verwijderd.

Als u de support alleen bevestigt waar deze de platvorm raakt, kan de support niet op het model rusten. Dit kan er echter toe leiden dat sommige delen van het model niet worden ondersteund.

**Als je alleen support op de platvorm gebruikt, schakel dan als truc de [Conische supportstructuur inschakelen](../experimental/support_conical_enabled.md) in en geef de [Hoek Conische Supportstructuur](../experimental/support_conical_angle.md ) een negatieve waarde. Hierdoor kan de support rond het model groeien en toch het grootste deel van het raster ondersteunen zonder op het model te rusten. Als alternatief kunt u de boomsupportstructuur gebruiken.**