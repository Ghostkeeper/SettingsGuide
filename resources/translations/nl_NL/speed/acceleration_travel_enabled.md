Bewegingsacceleratie inschakelen
====
Als deze parameter is geactiveerd, hebben de bewegingen hun eigen acceleratiesnelheid. De parameter [Bewegingsacceleratie](acceleration_travel.md) regelt vervolgens de snelheid van acceleratie tijdens het verplaatsen.

De waarde van de acceleratie tijdens de beweging zal de waarde aannemen van de lijn die zal worden geprint op de bestemming van de beweging. Als u bijvoorbeeld naar infill beweegt, is de acceleratie tijdens het verplaatsen [Vulacceleratie](acceleration_infill.md). Wanneer het richting de buitenwand gaat, is de acceleratie [Buitenwandacceleratie](acceleration_wall_0.md). Op deze manier zal het gevoeligere structuren met een beetje meer voorzichtigheid benaderen dan andere structuren.

Deze instelling is standaard ingeschakeld, zodat u de acceleratie tijdens het verplaatsen kunt regelen. Dit is in de meeste situaties een goede zaak, omdat een grotere verplaatsingsversnelling tijd kan besparen, terwijl een dergelijke hoge acceleratie [Rimpellen](../troubleshooting/ringing.md) zou veroorzaken wanneer het wordt gebruikt om zelf printen.

Er zijn echter twee redenen waarom u het misschien wilt uitschakelen:

* Om de snelheid van verplaatsingsversnellingen te veranderen, verandert Cura de acceleratie in beide richtingen heel vaak. Het schakelt vaak van extruderen naar verplaatsen, vooral bij bepaalde vulpatronen en bij kleine wanddetails. De controller moet deze commando's verwerken en kan de benodigde berekeningen mogelijk niet volgen. Het uitschakelen van bewegingsversnellingen vermindert dit probleem.
* Toenemende verplaatsingsversnellingen zorgen ervoor dat de printer veel gaat trillen. Deze trillingen zijn nog niet volledig gestopt aan het einde van de verplaatsing wanneer de print moet beginnen. Het kan ook een rimpeling veroorzaken aan het einde van een lijn. Door de verplaatsingsversnelling uit te schakelen, zal nozzle gevoelige structuren in de print (zoals de buitenwand) voorzichtiger benaderen dan minder gevoelige structuren (zoals de vulling).