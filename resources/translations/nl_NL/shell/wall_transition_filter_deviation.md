Filtermarge wandovergang
====
Sommige modellen hebben dunne elementen die rond de drempel liggen waar verschillende aantallen wanden worden gebruikt. Dit kan ertoe leiden dat het aantal wanden heen en weer gaat, zelfs als de werkelijke breedte van het stuk niet veel varieert. Deze wijziging verslechtert de printkwaliteit omdat er veel stroomveranderingen nodig zijn en er meer verplaatsingsbewegingen moeten worden toegevoegd. Deze functie verwijdert overgangen waar ze heen en weer zouden zijn gegaan.

Wanneer een overgang wordt verwijderd, kunnen sommige lijnen tijdelijk te breed of te dun worden. Deze instelling filtert de overgangen uit door te beperken hoeveel breder of dunner de lijn mag zijn.

<!--screenshot {
"image_path": "wall_transition_filter_off.png",
"modellen": [{"script": "signet.scad"}],
"camerapositie": [0, 11, 106],
"instellingen": {
	"wall_transition_filter_distance": 0,
	"wall_transition_filter_margin": 0,
	"wall_line_count": 3
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "wall_transition_filter_on.png",
"modellen": [{"script": "signet.scad"}],
"camerapositie": [0, 11, 106],
"instellingen": {
	"wall_transition_filter_distance": 100,
	"wall_transition_filter_margin": 0.2,
	"wall_line_count": 3
},
"kleuren": 64
}-->
![Met een klein bereik schommelt het tussen 2 en 3 wanden](../../../articles/images/wall_transition_filter_off.png)
![Met een hogere spanwijdte verandert het niet meer](../../../articles/images/wall_transition_filter_on.png)

Om precies te zijn, de lijnen mogen met dit bereik dunner worden dan de [Minimumbeedte wandlijn](min_wall_line_width.md) als dit het heen en weer schakelen tussen verschillende wandtellingen verhindert. Evenzo mogen lijnen met deze marge iets breder zijn, zelfs als een extra wand met de minimale wandlijnbreedte ook had gepast.

Dit filter is bedoeld om een veelvoorkomend probleem in dunne delen op te lossen met 3D-mazen met een lage resolutie. Het 3D-model, dat uit platte driehoeken bestaat, kan een kromme niet exact weergeven, alleen bij benadering. De curve heeft randen met platte oppervlakken ertussen. Bij het modelleren van een gebogen onderdeel met een constante breedte is het belangrijk dat de buitenranden overeenkomen met de binnenranden. Als dit niet het geval is, zal de breedte van de ring iets variëren, wat kan leiden tot het hierboven getoonde effect. Als dit het geval is, moet het overgangsfilter voorkomen dat het effect te sterk wordt.

Het vergroten van de marge verhindert soms het ontstaan van kleine lijnsegmenten. Hierdoor kan er sneller geprint worden en kan het oppervlak er gladder uitzien. Het maakt echter ook extremere lijnbreedten mogelijk die mogelijk niet goed uit de nozzle extruderen. Bij het printen van modellen met een lage resolutie met dunne onderdelen, kan het vergroten van de marge de kwaliteit verbeteren. Bij moeilijke materialen kun je beter aan de veilige kant blijven.

**Deze instelling is niet alleen van toepassing op normale wanden, maar ook op wanden met extra skinen, supportwanden, vullingen en concentrische patronen.**