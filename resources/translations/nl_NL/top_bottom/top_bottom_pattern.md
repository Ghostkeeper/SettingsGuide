Patroon Boven-/Onderkant
====
Met deze instelling kunt u specificeren hoe de boven- en onderkant met materiaal moeten worden gevuld. Er zijn verschillende printpatronen beschikbaar, maar de patronen zijn hier beperkter dan bij de vulling. Alleen patronen die dichte lagen creëren, zijn beschikbaar.

<!--screenshot {
"image_path": "top_bottom_pattern_lines.png",
"modellen": [{"script": "ring_5mm.scad"}],
"camerapositie": [0, 0, 100],
"instellingen": {"top_bottom_pattern": "lijnen"},
"kleuren": 64
}-->
Lijnen
----
![lijnen](../../../articles/images/top_bottom_pattern_lines.png)

Het basispatroon Lijnen trekt rechte lijnen over het oppervlak. Standaard zijn deze lijnen zo georiënteerd dat ze goed worden ondersteund door de vulling en support. De richting van de lijnen wisselt tussen lagen.
* Zorgt voor een mooie afwerkingskwaliteit.
* Zeer rigide in de richtingen waarin de lijnen worden getrokken.
* Hecht sterk aan de wanden waardoor relatief sterke delen ontstaan.

<!--screenshot {
"image_path": "top_bottom_pattern_concentric.png",
"modellen": [{"script": "ring_5mm.scad"}],
"camerapositie": [0, 0, 100],
"settings": {"top_bottom_pattern": "concentrisch"},
"kleuren": 64
}-->
Concentrisch
----
![Concentric](../../../articles/images/top_bottom_pattern_concentric.png)

Het concentrische patroon gaat verder in het model en tekent contouren.
* Even sterk in alle richtingen.
* Voorkomt de vorming van luchtbellen en kieren. Met dit patroon is het makkelijker om waterdichte objecten te maken.
* Uitstekende overhangkwaliteit, omdat de lijnen zeer goed overbrugd kunnen worden.
* Als het onderdeel cirkelvormig is, kan er een lelijke plek in het midden zijn waar de contouren samenkomen.
* De oppervlaktekwaliteit is niet ideaal.

<!--screenshot {
"image_path": "top_bottom_pattern_zigzag.png",
"modellen": [{"script": "ring_5mm.scad"}],
"camerapositie": [0, 0, 100],
"settings": {"top_bottom_pattern": "zigzag"},
"kleuren": 64
}-->
Zigzag
----
![Zigzag](../../../articles/images/top_bottom_pattern_zigzag.png)

Het zigzagpatroon lijkt erg op het lijnpatroon, maar in plaats van de lijnen in de wanden te beëindigen, blijven ze extruderen naar de dichtstbijzijnde skin.
* Biedt een geweldige oppervlaktekwaliteit.
* Zeer rigide in de richtingen waarin de lijnen worden getrokken.
* Houdt de extrusiesnelheid consistenter en verbetert de oppervlakteconsistentie op materialen die moeilijker te extruderen zijn.
* Plakt niet zo goed aan de wanden als aan het lijnenpatroon. Het effect [Overlappercentage Skin](skin_overlap.md) wordt verminderd. Dit verzwakt het onderdeel en vermindert de kwaliteit van de overhangen.