Problemen met (print)bed hechting
====
Een van de meest voorkomende soorten fouten bij 3D-printen is dat de print losraakt van het platform terwijl deze nog wordt geprint. In dit artikel worden enkele instellingen besproken die u kunt maken om dit te voorkomen.

Als de print van de platform is verdwenen, zie je meestal veel losse draden over de hele platform. Als je geluk hebt, kan het zich gewoon manifesteren als [Laagverschuivingt](layer_shift.md) (en er is minder op te ruimen). Hoe dan ook, de print is verpest.

Methoden van bedadhesie
----
Cura biedt verschillende methoden om de bedhechting te verbeteren. U kunt tussen deze methoden kiezen met de instelling [Type Hechting aan Platform](../platform_adhesion/adhesion_type.md). De volgende opties zijn beschikbaar.
* Brim, de meest gebruikte techniek, voegt een brim toe rond de onderkant van de print, waardoor het oppervlak groter wordt zodat de print beter hecht aan de platform.
* Een raft is een plaat onder de totale druk. Ook deze plaat krijgt een groter oppervlak zodat deze goed hecht. Als het raft is geprint met een materiaal dat goed hecht aan de print (bijvoorbeeld hetzelfde materiaal) dan houdt dit de print op zijn plaats.
* Een skirt zit niet vast aan de print, maar omsluit hem. Deze lijn zorgt ervoor dat het materiaal stroomt voordat de eigenlijke print begint, dus er is geen onder-extrusie in de eerste laag die de hechting zou kunnen bederven.
* U kunt ook geen (aanvullende) aansprakelijkheid hebben door "Geen" te selecteren. Dit bespaart tijd en materiaal en voorkomt andere negatieve effecten van bovenstaande methoden. Gebruik dit alleen als uw printer een andere vultechniek heeft, zoals: een emmer.

Brim and Raft zijn de meest effectieve technieken om de hechting te vergroten, omdat ze speciaal voor dit doel zijn ontworpen. Voor de meeste printen van redelijk formaat is een van deze twee technieken vereist.

Als brim wordt gebruikt, kunt u de hechting verder vergroten door [Breedte Brim](../platform_adhesion/brim_width.md) te vergroten. U kunt ook een brim toevoegen aan de [Supportbrim inschakelen](../support/support_brim_enable.md) en de [Brim primepijler](../dual/prime_tower_brim_enable.md) en tussen de [Brim vervangt supportstructuur](../platform_adhesion/brim_replaces_support.md) en de [Brim alleen aan Buitenkant](../platform_adhesion/brim_outside_only.md) van het model.

Wanneer Raft in gebruik is, kunt u de hechting verder vergroten door [Extra Marge Raft](../platform_adhesion/raft_margin.md) te vergroten. Het raft wordt echter altijd onder alles geprint, omdat de lagen moeten passen. Als hechting tussen het model en het raft een probleem is, overweeg dan om de [Luchtruimte Raft](../platform_adhesion/raft_airgap.md) tussen het raft en het model te verkleinen. U kunt ook overwegen om de [Lijnbreedte Grondvlak Raft](../platform_adhesion/raft_base_line_width.md) te vergroten.

Kromtrekken voorkomen
----
Wanneer uw print last heeft van kromtrekken, wordt het contactgebied tussen de print en de platform sterk verminderd. Om dit te voorkomen, zie het artikel over [Kromtrekken](warping.md). Samengevat zijn dit enkele instellingen die u kunt maken om kromtrekken te voorkomen.
* Zet het [Eerste laag patroon onderkant](../top_bottom/top_bottom_pattern_0.md) op concentrisch.
* Verlaag [Platformtemperatuur](../materiaal/materiaal_bed_temperatuur.md) en verhoog [Temperatuur werkvolume](../materiaal/bouwvolume_temperatuur.md).
* Pas het model zo aan dat er minder scherpe buitenhoeken zijn op de eerste laag.

Diverse aanpassingen
----
Deze instellingen kunnen ook worden aangepast wanneer normale bedadhesiemethoden niet voldoende zijn.
* Verhoog de [Hoogte Eerste Laag](../resolution/layer_height_0.md). Dit geeft wat meer ruimte voor fouten als de platform niet perfect vlak is. Het verhoogt ook de kracht waarmee materiaal uit nozzle en op de platform wordt geduwd.
* Verhoog de [Lijnbreedte eerste laag](../resolution/initial_layer_line_width_factor.md). Hierdoor wordt het materiaal ook met meer kracht naar buiten geduwd en hecht het goed aan de platform.
* Het verhogen van de [Printtemperatuur van de eerste laag](../material/material_print_temperature_layer_0.md) zorgt ervoor dat het materiaal meer op de platform vloeit en het contactoppervlak vergroot.
* Net als bij het verhogen van de temperatuur, kunt u ook de [Startsnelheid ventilator](../cooling/cool_fan_speed_0.md) verlagen of de [Normale Ventilatorsnelheid op Hoogte](../cooling/cool_fan_full_at_height.md) verhogen om te behouden het beeldmateriaal langer soepel te houden.
* Verlaag op dezelfde manier de [Snelheid Eerste Laag](../speed/speed_layer_0.md). Het verlagen van de [Printsnelheid Eerste Laag](../speed/speed_print_layer_0.md) zorgt ervoor dat het materiaal meer uitvloeit omdat de hete nozzle het materiaal langer vloeibaar houdt. Door de [Bewegingssnelheid Eerste Laag](../speed/speed_travel_layer_0.md) te verlagen, wordt de kans kleiner dat een traverse eerder geprinte lijnen van de platform trekt. Evenzo moet u de [Acceleratie Eerste laag](../speed/acceleration_layer_0.md) en [Schok Eerste Laag](../speed/jerk_layer_0.md) aanpassen.
* Verhoog het [Aantal lagen met lagere Printsnelheid](../speed/speed_slowdown_layers.md). Dit vermindert de kans op snelle bewegingen die de vorige lagen afpellen.

Panelen bouwen
----
Naast een goede print is een goede platform ook belangrijk voor de hechting. Een goede platform moet zijn:
* ...schoon zijn! Het is erg belangrijk dat de platform geen vet (bijvoorbeeld van uw vingers) en stof bevat. Reinigen onder een hete kraan is zeer effectief. Het gebruik van wat ontsmettingsalcohol, isopropanol en een microvezeldoek is ideaal.
* ...ook al! Als de platform te dicht bij nozzle staat, zal de filamentstroom uit nozzle ongelijkmatig zijn, wat resulteert in hobbels die nozzle de volgende keer zal afscheuren. Als de platform te ver van nozzle staat, wordt het materiaal niet goed op de platform geduwd, waardoor het oppervlak aanzienlijk wordt verkleind. Op de meeste printers kan de platform worden aangepast met een paar duimschroeven. Zorg er dus voor dat deze perfect waterpas staat en op de juiste afstand van nozzle.
* ...ruw! Met een licht opgeruwde platform is het contactoppervlak tussen de platform en de print enorm vergroot in vergelijking met een perfect gladde platform. Om deze reden zijn sommige printers uitgerust met mat glas of geanodiseerd metaal.

Ook het materiaal van de platform heeft een grote invloed op de lijmeigenschappen. Dit kan heel verschillend zijn voor verschillende printmaterialen. Gebruikelijke platformmaterialen zijn glas, acryl, aluminium, staal of geanodiseerd aluminium. Elk van deze materialen hecht aan andere materialen. Kunststof platformen kunnen zich chemisch aan uw materiaal hechten. Andere materialen vertrouwen op een ruw oppervlak om het contactoppervlak te vergroten.

Er zijn ook aanvullende bedadhesiemethoden die u op elke platform kunt toepassen:
* Algemene papierlijmsticks werken erg goed. Hoewel de lijm snel droogt, creëert het een ruw oppervlak met een grotere printvoetprint.
* Masking tape heeft een soortgelijk effect omdat het een ruw oppervlak van papier heeft, maar in tegenstelling tot papier blijft het perfect plat op de platform. De dikkere soorten afplaktape voor buitengebruik zijn het meest effectief.
*Haarlak werkt op dezelfde manier als lijm, omdat het een fijnkorrelig ruw oppervlak op de platform achterlaat. Het is heel eenvoudig om dit gelijkmatig aan te brengen.
* Breng voorzichtig wat schuurpapier aan op de platform om deze op te ruwen en het contactoppervlak te vergroten. Maar ruw ze niet te veel op, anders krijg je een oneffen oppervlak om op te printen. Gebruik hiervoor zeer fijn schuurpapier met een korrel van 500 of meer.
* Veel 3D-printerfabrikanten bieden speciale "plakvellen" aan die over de platform kunnen worden gespannen. Ze werken op dezelfde manier als plakband, maar zijn ontworpen om langer mee te gaan. Sommige zijn gemaakt van een plastic dat ook chemisch hecht aan het geprinte materiaal.