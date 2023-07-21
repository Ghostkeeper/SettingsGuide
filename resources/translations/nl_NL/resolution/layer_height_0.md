Hoogte Eerste Laag
====
Deze instelling bepaalt de dikte van de eerste laag van je print. De eerste laag wordt meestal dikker geprint dan de rest om een sterkere hechting op de platform te verkrijgen. Met deze instelling kan de dikte van de eerste laag worden vergroot zonder de resolutie van de rest van de print te verminderen.

<!--screenshot {
"image_path": "layer_height_0.png",
"modellen": [
    {
        "script": "rolling_blind_spacer.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [39, 28, 5],
"instellingen": {"layer_height_0": 0.3},
"kleuren": 32
}-->
![De eerste laag is dikker dan de andere lagen](../../../articles/images/layer_height_0.png)

Naarmate de dikte van de eerste laag toeneemt, moet het nozzle meer materiaal op dezelfde afstand extruderen. Dit vereist extra kracht omdat het materiaal zich naar de zijkanten uitspreidt om de hele lijnbreedte te vullen. Door deze extra kracht hecht het materiaal beter aan de platform. Daarnaast absorbeert de dikkere laag eventuele oneffenheden in het oppervlak. Als de platform licht gebogen is, zal de dikte van de eerste laag de oneffenheden opvangen, anders zou het nozzle  in de tweede laag kunnen afschrapen.

Een te dikke beginlaag zorgt ervoor dat de eerste laag meer meegeeft, met olifantenpoten als gevolg. De instelling [Eerste Laag Horizontale uitbreiding](../shell/xy_offset_layer_0.md) kan dit voorkomen door een kleine negatieve waarde op te geven.