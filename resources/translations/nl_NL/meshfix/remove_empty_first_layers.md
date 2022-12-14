Lege eerste lagen verwijderen
====
Als deze functie is ingeschakeld, worden alle lege lagen aan de onderkant van de print verwijderd. De hele print wordt naar beneden geschoven totdat deze op de platvorm rust. In plaats van lege lagen waardoor de print mislukt, zal de print iets lager zijn.

Als Cura de instelling "Automatisch modellen op platvorm plaatsen" heeft ingeschakeld, heeft deze instelling waarschijnlijk weinig effect. Maar ze kan nog steeds een rol spelen. Wanneer modellen automatisch op de platvorm worden geplaatst, worden de modellen nauwkeurig uitgelijnd met de platvorm. Als de eerste laag(en) echter alleen elementen bevatten die te klein zijn om te printen (bijvoorbeeld omdat de onderkant niet helemaal glad is), kan de eerste laag in de uiteindelijke print nog leeg zijn. Deze instelling voorkomt dit door de rest van de lagen één laag naar beneden te verplaatsen.

Na het naar beneden schuiven van de print blijven de instellingen die gelden voor de eerste laag gelden. Dus ook al is de oorspronkelijke eerste laag verwijderd, de [Print Temperatuur van de eertse laag](../material/material_print_temperature_layer_0.md) en vergelijkbare instellingen worden nog steeds toegepast op de nieuwe eerste laag.

Normaal gesproken moet deze instelling altijd worden ingeschakeld om te voorkomen dat printen mislukken omdat de onderkant niet perfect glad is of niet goed is uitgelijnd met de platvorm. U kunt deze instelling echter uitschakelen als u een printtaak in meerdere fasen uitvoert die in de lucht moet beginnen.

Wanneer [Support genereren](../support/support_enable.md) is ingeschakeld, strekt de support zich uit tot aan de platvorm, zodat de eerste paar lagen niet langer leeg zijn. Er worden geen lagen verwijderd en de print beweegt niet naar beneden.

Als de instelling [Slicetolerantie](../experimental/slicing_tolerance.md) is ingesteld op "Exclusive", zal de eerste laag altijd leeg zijn. Als deze instelling niet is ingeschakeld, is de eerste laag leeg en zal de print hoogstwaarschijnlijk mislukken.