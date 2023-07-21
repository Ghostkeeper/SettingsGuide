Spaghetti Vulling
====
Als deze instelling is geactiveerd, zal Cura alle vullingen van meerdere lagen tegelijk naar een hogere laag extruderen. Dit is een extreme vorm van de [Infill dikte](../infill/infill_sparse_thickness.md) methode, maar zonder het doel om de sterkte van de infill te behouden. Het heeft enige functionaliteit om de extreme hoeveelheden extrusie aan te kunnen.

Deze functie is niet geschikt voor normale materialen. Meestal wilt u ofwel de stevigheid van normale opvulpatronen, of u laat de opvulling helemaal weg. Er zijn echter twee use-cases voor deze functie.

Gebruiks gevallen
----
Met flexibele materialen kan deze techniek zeer zachte texturen produceren. Spaghettivulling zorgt meestal voor losse ringen die niet goed aan elkaar plakken. Deze ringen zijn in alle richtingen even zacht. Om dit effect te bereiken mag de dichtheid van de vulling echter niet te laag zijn, anders komt alle spaghetti op de onderkant van de print terecht. Het is raadzaam om een [spaghettistroom](spaghetti_flow.md) tussen 30% en 60% te gebruiken, afhankelijk van de lijnbreedte en laaghoogte. Het resultaat is een vulling die in alle richtingen even stijf en redelijk zacht is.

Het andere gebruik voor de spaghettivulling is gieten. Als u een printer heeft met een puntstorthulpmiddel, kunt u deze functie gebruiken om uw model redelijk gelijkmatig te vullen met gecontroleerde afzettingen van materiaal. In dit geval moet de [vloeidichtheid](spaghetti_flow.md) waarschijnlijk rond de 100% liggen, afhankelijk van de krimp/expansieverhouding van het gietmateriaal.

Pas andere instellingen voor spaghettivulling aan
----
Beide toepassingen vereisen een zeer speciale behandeling van de vulling. Hier zijn enkele instellingen die u waarschijnlijk moet aanpassen aan uw behoeften:
* De [infill printsnelheid](../speed/speed_infill.md) moet enorm worden verlaagd. Als de nozzle de infill van 10 lagen tegelijk moet extruderen, moet u de printsnelheid met minimaal een factor 8 verlagen.
* Stel de [Dikte van opvulling](../infill/infill_sparse_thickness.md) in op de hoogte van de laag.
* Verhoog de [printtemperatuur](../material/material_print_temperature.md) iets (voor de extruder die de vulling print). Hierdoor kan het materiaal goed uit de nozzle stromen en wordt de extrusie versneld.
* Stel de [Z Seam Alignment](../shell/z_seam_type.md) in op willekeurig om de textuur willekeurig te maken.

**In Cura's laagweergave wordt de vulling weergegeven als zeer dikke lijnen. Dat komt omdat Cura ervan uitgaat dat het materiaal op dezelfde laag blijft en zich daar uitspreidt. In werkelijkheid zal het naar beneden vallen.**

**Als spaghetti-invulling wordt gebruikt, heeft de instelling [Infill line width](../resolution/infill_line_width.md) geen effect meer. De lijnbreedte wordt aangepast aan de vereisten van de instellingen [Infill Line Distance](../infill/infill_line_distance.md) en [Spaghetti Flow](spaghetti_flow.md).**