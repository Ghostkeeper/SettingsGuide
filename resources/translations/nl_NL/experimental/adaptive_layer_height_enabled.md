Adaptieve lagen gebruiken
====
Aanpassingslagen past de laaghoogte van uw print lokaal aan om de printtijd en -kwaliteit te optimaliseren op basis van de oppervlaktekenmerken van het model. De lagen worden dunner gemaakt als er vlakke hellingen zijn, of dikker als de wanden steil zijn. Het doel is om snel te printen waar het kan, maar gedetailleerd waar het moet.

<!--screenshot {
"image_path": "adaptive_layer_height_enabled.png",
"modellen": [{"script": "barn.scad"}],
"camerapositie": [-108, -229, 118],
"instellingen": {
    "adaptive_layer_height_enabled": waar,
    "layer_height": 0.2
},
"color_scheme": "laaghoogte",
"kleuren": 128
}-->
![Met het "laaghoogte" kleurenschema kun je zien dat het dunnere lagen blauw kleurt en dikkere lagen geel](../../../articles/images/adaptive_layer_height_enabled.png)

De laaghoogte wordt zo aangepast dat de horizontale afstand tussen de randen van de lagen constant blijft. Voor vlakke oppervlakken is er een grote horizontale verplaatsing met een kleine verticale verplaatsing, dus een kleine verticale verplaatsing wordt toegepast om de horizontale verplaatsing constant te houden. Op steile vlakken is er een kleine horizontale verplaatsing met een grote verticale verplaatsing, dus er wordt een grote verticale verplaatsing gemaakt om de horizontale verplaatsing constant te houden. Op deze manier wordt het topografische effect van de lagen constant gehouden. De maximale afstand tussen twee aangrenzende lagen wordt op een constante afstand gehouden van de instelling [Topografieformaat aanpasbare lagen](adaptive_layer_height_threshold.md).

Als het model zowel vlakke vlakken als steile vlakken op dezelfde hoogte heeft, wordt aangenomen dat de laaghoogte de kleinste van de twee lagen is. Dit maakt de hoogte van de laag soms onnodig klein omdat er een horizontaal vlak naast ligt. Dit is te zien in de bovenstaande schermafbeelding, evenals de halve hoogte van de silo aan de linkerkant.

Overeenkomende lagen zijn streng beperkt om de printkwaliteit te verbeteren. De hoogte van de laag mag niet meer afwijken dan een bepaalde [Maximale variatie adaptieve lagen](adaptive_layer_height_variation.md) van de oorspronkelijke [Laag Hoogte](../resolution/layer_height.md) instelling. Het verschil in laaghoogte tussen twee aangrenzende lagen mag niet meer zijn dan een bepaalde [Stapgrootte variatie adaptieve lagen](adaptive_layer_height_variation_step.md). Dit zorgt ervoor dat de laaghoogte geleidelijk overgaat, in plaats van plotseling van de ene laag naar de andere te halveren.

Met adaptieve lagen kan de printtijd aanzienlijk worden verkort zonder dat dit ten koste gaat van de printkwaliteit, in sommige gevallen zelfs met verbeterde kwaliteit. De effecten van het aanpassen van de laaghoogte zijn immens. In de meeste gevallen zal het gebruik van dikkere lagen op plaatsen waar het model verticaal staat de printtijd aanzienlijk verkorten. De [Topografie](../troubleshooting/topography.md) wordt ook verminderd omdat de lagen horizontaal dichter bij elkaar liggen.

Deze functie kan echter ook met een aantal problemen gepaard gaan.
* Bij het wijzigen van de laaghoogte moeten meestal ook enkele andere instellingen worden aangepast, b.v. de nozzletemperatuur. Aanpassingslagen passen deze niet automatisch aan. Dit kan leiden tot b.v. B. Overhangen die beter zouden printen bij een lagere printtemperatuur worden niet optimaal geprint.
* Als de slice-hoogte wordt gewijzigd voor een klein kenmerk ergens in een klein deel van de slice in de slice, zijn strepen zichtbaar in de rest van de slice.
* Hiermee worden ook onbedoeld de verticale afstanden aangepast. Dit kan de printkwaliteit negatief beïnvloeden. De [Dikte Boven-/Onderkant](../top_bottom/top_bottom_thickness.md) wordt bijvoorbeeld meestal lager omdat Cura de instelling [Bovenlagen](../top_bottom/top_layers.md) als true aanneemt en de lagen dunner worden. Dit kan leiden tot pillowing. Getroffen instellingen die mogelijk niet langer correct zijn, zijn onder meer:
  * [Dikte Bovenkant](../top_bottom/top_thickness.md)
  * [Bodemdikte](../top_bottom/bottom_thickness.md)
  * [Max skinhoek voor uitbreiding](../top_bottom/max_skin_angle_for_expansion.md)
  * [Staphoogte Geleidelijke Vulling](../infill/gradual_infill_step_height.md)
  * [Geleidelijke supportvulling hoogte traptreden](../support/gradual_support_infill_step_height.md)
  * [Dikte Vullaag](../infill/infill_sparse_thickness.md)
  * [Dikte vullaag supportvulling](../support/support_infill_sparse_thickness.md)
  * [Z-afstand Supportstructuur](../support/support_z_distance.md)
  * [Dikte Supportdak](../support/support_roof_height.md)
  * [Dikte supportvloer](../support/support_bottom_height.md)
  * [Overhanghoek Supportstructuur](../support/support_angle.md)
  * [Hoogte Traptreden Supportstructuur](../support/support_bottom_stair_step_height.md)
  * [Hoek van Pijlerdak](../support/support_tower_roof_angle.md)
  * [Hoek Uitloopscherm](../dual/ooze_shield_angle.md)
  * [Maximale Modelhoek](../experimenteel/conical_overhang_angle.md)