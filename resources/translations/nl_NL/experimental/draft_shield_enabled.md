Tochtscherm Inschakelen 
====
Als deze instelling is ingeschakeld, bouwt de printer een scherm rond uw print die de print beschermt tegen luchtstromen uit de omgeving.

<!--screenshot {
"image_path": "draft_shield_enabled.png",
"modellen": [{"script": "headphone_hook.scad"}],
"camerapositie": [-56, 139, 305],
"instellingen": {
    "draft_shield_enabled": true
},
"kleuren": 32
}-->
![Er is een scherm om het model geprint](../../../articles/images/draft_shield_enabled.png)

Sommige printers en printmaterialen zijn erg gevoelig voor de omgeving waarin ze worden geprint. printen op verschillende delen van de platvorm kan verschillende resultaten opleveren, omdat ze kwetsbaarder zijn voor stromingen van buitenlucht. Als de print 's nachts wordt uitgevoerd en de kamer kouder wordt, kan dit een aanzienlijke invloed hebben op de print. Het windscherm is ontworpen om dit effect te verminderen door een klein, geïsoleerd volume rond de print te creëren. Dit dient als een geïmproviseerde "verwarmingskamer" om de print warm te houden en te beschermen tegen koude tocht van buitenaf.

Het schild wordt geprint terwijl het model wordt geprint. Als er meerdere extruders bij de print betrokken zijn, wordt het windscherm geprint met de extruder die de laag start. Dit gebeurt afwisselend van laag tot laag.

Windscherm heeft verschillende belangrijke effecten op het printen:
* Het houdt de temperatuur van de print constanter. Dit is het beoogde effect van het windscherm. Dientengevolge moet streepvorming als gevolg van temperatuurveranderingen in de kamer worden verminderd.
* Over het algemeen is de temperatuurbinnen het tochtscherm hoger dan zonder tochtscherm. Dit komt omdat de warmte moeilijker kan ontsnappen en er geen convectiestromen kunnen opstijgen met de hete lucht uit de druk. Dit heeft invloed op alle aspecten van de print. Met name is er meer draden en verslapping.
* De ventilatoren op de printkop worden minder effectief. Ook daar verstoort het schild de luchtstroom. Om de effectiviteit van de ventilatoren op de printkop te vergroten, kan de [Tochtscherm X/Y-afstand](draft_shield_dist.md) worden vergroot.
* Het windscherm kan functioneren als [Uitloopscherm](../dual/ooze_shield_enabled.md). Wanneer er verplaatsbewegingen worden gemaakt naar een object dat wordt beschermd door een windscherm, wordt het materiaal dat op nozzle achterblijft op het blad afgeveegd.
* Het windscherm kan dienen als [Primepijler](../dual/prime_tower_enable.md). Omdat het voor het object wordt geprint, is het printen van het windscherm een ​​manier om het materiaal door te spoelen en goed te laten vloeien. Dit is echter alleen effectief met 2 extruders, aangezien niet alle met meer dan 2 extruders worden gespoeld.