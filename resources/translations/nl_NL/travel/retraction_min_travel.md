Minimale Afstand voor Intrekken
====
Deze instelling verhindert dat het materiaal over zeer korte verplaatsingsafstanden wordt ingetrokken. Tijdens dit verplaatsen heeft het materiaal toch maar heel weinig tijd om nozzle te verlaten, dus naar binnen trekken zou meer kwaad dan goed doen.

<!--screenshot {
"image_path": "retraction_min_travel.png",
"modellen": [{"script": "spike_curve.scad"}],
"camerapositie": [0, -31, 79],
"structuren": ["reizen", "helpers", "shell", "infill", "starts"],
"instellingen": {"retraction_min_travel": 12},
"minimum_laag": 303,
"laag": 550,
"lijnen": 337,
"kleuren": 64
}-->
![Met de korte verplaatsafstand in het midden, is er geen terugtrekking.](../../../articles/images/retraction_min_travel.png)

Het terugtrekken van het materiaal is bedoeld om stringing te voorkomen. Zeer korte verplaatsingen leiden niet tot stringing omdat het materiaal nog niet uit de nozzle heeft kunnen stromen. Bij extreem korte verplaatsingen van ongeveer één lijnbreedte overlappen de lijnen elkaar zelfs volledig, zodat er geen ruimte meer is om te stringing. Bij het intrekken daarentegen staat de nozzle korte tijd stil terwijl het materiaal in beweging is. Hierdoor kan wat materiaal stromen en ontstaat er een klodder. Om deze redenen is het beter om niet in te verplaatsen op korte routes, ook al bevinden deze routes zich op zichtbare delen van het model.

Als u deze instelling te veel verhoogt, resulteert dit in stringing in zeer gedetailleerde delen van het model of waar delen dicht bij elkaar staan.