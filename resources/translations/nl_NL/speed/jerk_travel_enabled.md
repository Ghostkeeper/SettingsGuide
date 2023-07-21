Bewegingsschok inschakelen
====
Als deze instelling is ingeschakeld, hebben verplaatsingsbewegingen hun eigen acceleratienelheid. De parameter [Bewegindsschok](jerk_travel.md) bepaalt vervolgens hoe snel de verplaatsingen om de beurt kunnen zijn.

De waarde van de schok tijdens de verplaatsing zal de waarde aannemen van de lijn die zal worden geprint op de bestemming van de verplaatsing. Als u bijvoorbeeld naar vulling beweegt, is de schok tijdens het verplaatsen de [Vulschok](jerk_infill.md). Wanneer het naar de buitenwand beweegt, zal de schok de [Schok Buitenwand](jerk_wall_0.md) zijn. Op deze manier zal het gevoeligere structuren met een beetje meer voorzichtigheid benaderen dan andere structuren.

Deze instelling is standaard ingeschakeld, waardoor u controle heeft over schokken tijdens het bewegen. Dit is in de meeste situaties een goede zaak, omdat een verhoging van de verplaatsingssnelheid tijd kan besparen, terwijl zulke hoge draaisnelheden [Rrimpellen](../troubleshooting/ringing.md ) zouden veroorzaken bij gebruik voor printen.

Er zijn echter twee redenen waarom u het misschien wilt uitschakelen:

* Om de snelheid van acceleratie voor verplaatsingen te wijzigen, wijzigt Cura heel vaak de snelheid van schok in beide richtingen. Het schakelt vaak van extruderen naar bewegen, vooral bij bepaalde vulpatronen en bij kleine wanddetails. De controller moet deze commando's verwerken en kan de benodigde berekeningen mogelijk niet volgen. Het uitschakelen van bewegingsschok vermindert dit probleem.
* Toenemende bewegingschok zorgt ervoor dat de printer veel trilt. Deze trillingen zijn nog niet volledig gestopt aan het einde van de verplaatsing wanneer de print moet beginnen. Het kan ook een rimpeling veroorzaken aan het einde van een lijn. Als je de "Bewegingsschok"-functie uitschakelt, zal nozzle gevoelige structuren in de print (zoals de buitenwand) voorzichtiger benaderen dan minder gevoelige structuren (zoals de vulling).