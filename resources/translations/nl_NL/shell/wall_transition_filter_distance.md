Filterafstand wandovergang
====
Sommige modellen hebben dunne elementen die rond de drempel liggen waar verschillende aantallen wanden worden gebruikt. Dit kan ertoe leiden dat het aantal wanden wisseld, zelfs als de werkelijke breedte van het stuk niet veel varieert. Deze wijziging verslechtert de printkwaliteit omdat er veel doorstroom veranderingen nodig zijn en er meer verplaatsings bewegingen moeten worden toegevoegd. Deze functie verwijdert overgangen wanneer ze binnen een bepaalde afstand heen en weer zouden zijn gegaan.

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
![Zonder een filter, overgangen tussen 2 en 3 wanden](../../../articles/images/wall_transition_filter_off.png)
![Met filter wodt niet meer gewijzigd](../../../articles/images/wall_transition_filter_on.png)

Wanneer een overgang wordt verwijderd, kunnen sommige lijnen tijdelijk te breed of te dun worden, waardoor de minimum breedte wandlijn](min_wall_line_width.md) wordt overschreden. Uiteindelijk was er een overgang die beter aansluit bij de breedte van het onderdeel. Zonder deze overgang zal het minder of meer wanden gebruiken dan ideaal zou zijn, en de breedte van die wanden zal dienovereenkomstig worden aangepast. Dit is toegestaan ​​tot aan de [Filtermarge wandovergang](wall_transition_filter_deviation.md). Als de breedte van de wanden te veel varieert, wordt de overgang niet verwijderd.

Dit filter is bedoeld om een ​​veelvoorkomend probleem in dunne delen op te lossen met 3D-mazen met een lage resolutie. Het 3D-model, dat bestaat uit platte driehoeken, kan een kromme niet exact weergeven, maar benadert deze alleen. De curve heeft randen met platte oppervlakken ertussen. Bij het modelleren van een gebogen onderdeel met een constante breedte is het belangrijk dat de buitenranden overeenkomen met de binnenranden. Als dit niet het geval is, zal de breedte van de wand iets variëren, wat kan leiden tot het hierboven getoonde effect. Als dit het geval is, moet het overgangsfilter voorkomen dat het effect te sterk wordt.

Door de afstand te vergroten, worden in sommige gevallen kleine lijnsegmenten voorkomen. Hierdoor kan er sneller geprint worden en kan het oppervlak er gladder uitzien. Het resulteert echter ook in een groter deel van de print met extreme lijnbreedtes die mogelijk niet goed uit de nozzle komen. Bij het printen van modellen met een lage resolutie met dunne onderdelen, kan het vergroten van de afstand de kwaliteit verbeteren. Bij moeilijke materialen kun je beter aan de veilige kant blijven.

**Deze instelling is momenteel niet zichtbaar voor de gebruiker. Het filter kan alleen worden aangepast via de [Filtermarge wandovergang](wall_transition_filter_deviation.md). Het beïnvloedt niet alleen normale wanden, maar ook wanden met extra skinen, supportwanden, vullingen en concentrische patronen.**