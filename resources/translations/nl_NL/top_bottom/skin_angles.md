Lijnrichtingen boven-/onderkant
====
Met deze instelling kunt u de richting wijzigen waarin de bovenste en onderste lijnen worden geprint. U kunt een door komma's gescheiden lijst van hoeken opgeven (in graden) en de lijnen worden per laag in een andere richting geprint.

<!--screenshot {
"image_path": "skin_angles.gif",
"modellen": [
    {
        "script": "microwave_hook.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 48, 70],
"instellingen": {"skin_angles": "[0, 60, 120]"},
"laag": [76, 77, 78],
"kleuren": 128
}-->

![lijnenpatroon met afwisselende hoeken van 0°, 60° en 120°](../../../articles/images/skin_angles.gif)

Standaard wordt het lijnpatroon in de twee diagonale richtingen geprint. Bij Cartesiaanse portaalsystemen is dit het meest nauwkeurig omdat de printer zowel de X- als de Y-motor kan gebruiken om de nozzle te versnellen bij het verplaatsen voor de volgende regel.

Er kunnen verschillende redenen zijn om deze richtingen te wijzigen:
* Om een optisch effect te creëren.
* Om kracht te optimaliseren. De print is meestal stabieler wanneer hij parallel aan de lijnen van de buitenskin (en opvulling) wordt geduwd en getrokken.
* Om de overhang te verminderen. Als een print in één richting erg dun is, kan de buitenskin die richting overbruggen om materiaal voor de vulling te sparen. Er is geen vulling nodig om de kloof te overbruggen. Op dezelfde manier kunt u ook een richting kiezen die loodrecht op de vulling staat om de overhang over de vulling te minimaliseren. Op deze manier kunt u een betere kwaliteit van het oppervlak bereiken.
* Om de nauwkeurigheid te optimaliseren als uw printer geen motor in X-richting en motor in Y-richting heeft, zoals: een printer met een H-bridge portal of een deltaprinter.

Als u bijvoorbeeld '[0, 30, 60]' invoert, schakelt de richting tussen 0 graden vanaf de x-as, 30 graden vanaf en 60 graden vanaf.