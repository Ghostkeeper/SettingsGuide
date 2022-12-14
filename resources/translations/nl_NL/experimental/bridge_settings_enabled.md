Bruginstellingen inschakelen
====
Als uw model een overhang heeft die aan beide zijden wordt ondersteund, zal Cura dit herkennen en het overhangende gedeelte van de skin aanpassen om beter te kunnen printen. Als deze instelling is ingeschakeld, kunt u de detectie van deze overhangen en het resulterende gedrag afstemmen om ze beter te overbruggen.

<!--screenshot {
"image_path": "bridge_settings_enabled_default.png",
"modellen": [
    {
        "script": "rack_straight.scad",
        "scad_params": ["lengte=40"]
    }
],
"camerapositie": [0, 74, -137],
"kleuren": 32
}-->
<!--screenshot {
"image_path": "bridge_settings_enabled_enabled.png",
"modellen": [
    {
        "script": "trappenhuis.scad",
        "scad_params": ["stappen=4", "breedte=10", "hoogte=20"]
    }
],
"laag": 275,
"instellingen": {
    "bridge_settings_enabled": true
},
"camerapositie": [-12, 28, 63],
"kleuren": 64
}-->

![Wanneer een brug wordt gedetecteerd, worden de skinlijnen uitgelijnd om de opening zo goed mogelijk te overbruggen.](../../../articles/images/bridge_settings_enabled_default.png)
![Als bridge-instellingen zijn ingeschakeld, worden de bridge-lijnen geprint met verschillende instellingen](../../../articles/images/bridge_settings_enabled_enabled.png)

Normaal gesproken gebruikt Cura een vrij rudimentaire overbruggingstechniek. Cura detecteert overhangende delen van de skin die aan meerdere kanten worden ondersupportd. De [Lijnrichtingen boven-/onderkant](../top_bottom/skin_angles.md) wordt aangepast om deze gebieden automatisch te overbruggen. Dit zorgt ervoor dat zoveel mogelijk van de overhang op meerdere lagen wordt ondersteund en verbetert de printkwaliteit.

Als deze instelling echter is ingeschakeld, kunt u dit gedrag verder afstemmen op uw behoeften. Zo kunt u de instellingen aanpassen:
* Printsnelheid
* Doorvoer
* Dichtheid (zelfde als de vulling maar met de lijnen van de skin)
* Ventilator snelheid
* voor de wanden ook de uitloop.

Deze instellingen kunnen afzonderlijk worden aangepast voor zowel de skin die een kloof overbrugt als de wanden. Als [Brug heeft meerdere lagen](bridge_enable_more_layers.md) is ingeschakeld, kunnen ze ook afzonderlijk worden ingesteld voor de tweede en derde laag boven de overbrugde opening. U kunt ook instellen welke delen van de print als overbruggingszones worden beschouwd door de [Drempelwaarde voor brgskinsupport](bridge_skin_support_threshold.md) en [Minimale brugwandlengte](bridge_wall_min_length.md) in te stellen.

Door overbruggingsinstellingen in te schakelen, krijgt u meer controle over hoe overbrugging wordt verwerkt in uw print. Als u de overbruggingsparameters heel goed instelt, kunt u de kwaliteit van uw uitsteeklengten en de nauwkeurigheid in verticale richting aanzienlijk verbeteren. Het enige nadeel is dat als u de bridge-instellingen voor uw printer niet aanpast, de print ook kan verslechteren.