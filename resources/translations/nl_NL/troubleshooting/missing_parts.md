Missende onderdelen
====
Soms lijkt het bij het controleren van de slice-weergave (of, als u pech heeft, bij het printen) dat er delen van de print ontbreken. Dit kan verschillende redenen hebben. Dit artikel somt een aantal mogelijkheden op.

Niet-gesloten netwerken
----
Sommige rasters hebben gaten in het oppervlak of een extra geometrie aan de binnenkant. Dit brengt Cura in verwarring omdat niet meer duidelijk is welke delen van het volume tot het interieur behoren en welke niet. Als je naar een dwarsdoorsnede van het model kijkt, telt Cura van buiten naar binnen. Het eerste oppervlakgezicht dat het doorkruist, betekent dat het in het model gaat. Het tweede gebied betekent dat het weer naar buiten gaat. Het derde vlak dat het kruist, betekent dat het er weer in gaat, enzovoort. Als delen van de oppervlakte ontbreken, of als er extra losse oppervlaktes in het midden zijn, wordt het interieur dubbelzinnig, afhankelijk van van welke kant je ernaar kijkt.

![Met gesloten mazen is het duidelijk waar het interieur van het model ligt](../../../articles/images/manifold_correct.svg)
![Bij niet-gesloten meshes is het volume van de mesh niet uniek](../../../articles/images/manifold_incorrect.svg)

Meshes die zulke ontbrekende vlakken of extra delen hebben, worden non-manifold genoemd omdat ze in de echte wereld niet kunnen bestaan. Cura probeert ze in te vullen door kleine gaten op te vullen, maar als een oppervlak niet kan worden ingevuld, wordt het niet geprint (tenzij de [Surface Mode](../blackmagic/magic_mesh_surface_mode.md) erop is ingesteld). De ontbrekende of extra geometrie wordt ook weergegeven in de 3D-scène met een gestippeld patroon, of in rood in de voorbereidingsfase wanneer röntgenweergave wordt gebruikt. Het oppervlak is anders gekleurd als het tot een oneven aantal oppervlakken behoort, wat alleen het geval is als de mesh niet divers is. Zo kunt u problemen met uw netwerk identificeren.

![In de röntgenweergave worden niet-gesloten mazen weergegeven met rode delen.](../../../articles/images/x_ray.png)

Hoewel Cura er meestal van uitgaat dat de mesh divers is, kan het in sommige gevallen het model corrigeren. Dit zijn enkele dingen die u kunt proberen:
* [Uitgebreid Hechten](../meshfix/meshfix_extensive_stitching.md) kan beter omgaan met gevallen waarin extra geometrie aan de buitenkant van een model is bevestigd, hoewel het wat meer tijd kost om te snijden.
* [Oderbroken Oppervlakken Behouden](../meshfix/meshfix_keep_open_polygons.md) sluit alle open lussen met een rechte lijn. Hierdoor worden kleine openingen zeer goed gesloten. Dit kan er echter ook voor zorgen dat het model er heel vreemd uitziet als het grote gaten bevat.
* Als laatste redmiddel kan [Oppervlaktemodus](../blackmagic/magic_mesh_surface_mode.md) worden gebruikt om delen met gaten te printen, net als een enkele wand, zonder enige inhoud. Omdat het niet bekend is waar de binnenkant van dit deel is, zal er geen vulling of skin zijn, maar de omtrek kan in ieder geval worden geprint. In sommige gevallen kan dit ertoe leiden dat de print er nog redelijk uitziet.

Als deze opties niet de gewenste print opleveren, moet u deze handmatig corrigeren met behulp van 3D-modelleringstoepassingen.

Dunne delen
----
Als het model hele fijne details heeft, is niet alles te tekenen met de dikke lijnen die uit je 3D-printer komen. Cura past de lijnen aan de vorm aan die door je mesh wordt geschetst. Als dit niet mogelijk is, wordt er niets geprint. In dit geval kan het lijken alsof er delen van de print ontbreken.

Er zijn een paar manieren om dit te veranderen:
* Verklein de [Lijnbreedte](../resolution/line_width.md). Als u iets printt met dunne wanden of randen, zorg er dan voor dat de lijnbreedte iets kleiner is dan de minimale breedte van het betreffende onderdeel. Als u de lijnbreedte echter te veel verkleint, kunt u [Onder-extrusie](underextrusion.md) krijgen vanwege onvoldoende doorstroming. Om de lijnbreedte verder te verkleinen, moet u een kleinere nozzle gebruiken.
* Voeg een [Horizontale Uitbreiding](../shell/xy_offset.md) toe aan de print. Hierdoor wordt het hele model aan alle kanten breder, ook de dunne delen. Hierdoor zijn ze minder dun waardoor ze nu geprint kunnen worden. Dit verpest natuurlijk ook de maatnauwkeurigheid en detail van de print naarmate alles dikker wordt.
* Schakel de instelling [Dunne wanden printen](../shell/fill_outline_gaps.md) in. Hiermee wordt geprobeerd de dunne delen te vullen met zeer kleine lijnen zonder de lijnbreedte van de rest van het model te verminderen. Dit veroorzaakt echter grote veranderingen in de doorvoer van het materiaal en vult de wanden mogelijk niet altijd met mooie, gelijkmatige lijnen.
*Vergeet niet om het model aan te passen aan de print door elk onderdeel minstens zo dik te maken als je lijndikte.