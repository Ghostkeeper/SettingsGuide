Geprinte delen mijden tijdens bewegingen
====
Als u deze instelling inschakelt, raakt de printkop geen andere objecten aan terwijl deze door de print beweegt. In plaats daarvan zal hij een kleine omweg maken. Als een omweg mogelijk is zonder andere objecten te raken, wordt deze niet ingetrokken tenzij de lengte van het pad de instelling [Max. combing-afstand zonder intrekken](retraction_combing_max_distance.md) overschrijdt.

<!--screenshot {
"image_path": "travel_avoid_other_parts_disabled.png",
"modellen": [{"script": "spike_curve.scad"}],
"camerapositie": [0, 0, 116],
"structuren": ["reizen", "helpers", "shell", "infill", "starts"],
"instellingen": {
    "retraction_enable": false,
    "travel_avoid_other_parts": false
},
"minimum_laag": 549,
"laag": 550,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "travel_avoid_other_parts_enabled.png",
"modellen": [{"script": "spike_curve.scad"}],
"camerapositie": [0, 0, 116],
"structuren": ["reizen", "helpers", "shell", "infill", "starts"],
"instellingen": {
    "retraction_enable": false,
    "travel_avoid_other_parts": true
},
"minimum_laag": 549,
"laag": 550,
"kleuren": 64
}-->
![Indien uitgeschakeld, kunnen verplaatsingen door andere delen gaan](../../../articles/images/travel_avoid_other_parts_disabled.png)
![Indien geactiveerd, vermijden de verplaatsingen andere delen](../../../articles/images/travel_avoid_other_parts_enabled.png)

Naast het vermijden van andere delen, proberen de verplaatsingen ook zo dicht mogelijk bij de wanden te blijven. Dit betekent dat wanneer nozzle een onderdeel door een wand verlaat of binnengaat, het loodrecht op de wand zal uitgaan of binnenkomen.

Deze instelling heeft de neiging om de oppervlaktekwaliteit van de print te verbeteren, omdat nozzle niet zo vaak door de wanden gaat. Het oversteken van wanden laat een kras op de wand achter, die moet worden vermeden.

Deze instelling verhoogt echter de hoeveelheid druppelen omdat er meer beweging wordt gemaakt zonder intrekken de reis langer is. Voor materialen die sterk druipen, kan het raadzaam zijn om het omzeilen van andere onderdelen uit te schakelen.

De printtijd kan door de langere verplaatsafstanden iets toenemen, maar dit wordt meestal volledig gecompenseerd door het resulterende lagere aantal intrekkingen.